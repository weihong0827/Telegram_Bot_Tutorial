from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, ConversationHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from bus_api import *
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

Token = os.getenv('TOKEN')
updater = Updater(token=Token, use_context=True)
dispatcher = updater.dispatcher
LOCATIONINFO, BUSSTOPINFO, BUSINFO = range(3)


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    return LOCATIONINFO

# start_handler = CommandHandler('start', start)
# dispatcher.add_handler(start_handler)


# def echo(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
#
#
# echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
# dispatcher.add_handler(echo_handler)

def nearest_busstop(update, context):
    update_dict = update.to_dict()
    location = update_dict['message']['location']
    result = get_bus_stops((location['latitude'], location['longitude']))
    buttons = []
    for data in result:
        buttons.append([InlineKeyboardButton(
            text=data['Description'], callback_data=data['BusStopCode'])])
    keyboard = InlineKeyboardMarkup(buttons)
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Based on your location, " +
             "here are the bus stops nearest to you! " +
             "Which one are you at? ", reply_markup=keyboard)
    return BUSSTOPINFO

# location_handler = MessageHandler(Filters.location, nearest_busstop)
# dispatcher.add_handler(location_handler)


def busStopInfo(update, context):
    query = update.callback_query

    query.answer()
    data = query['data']
    print(data)
    context.user_data['bus_stop'] = data
    bus_info = get_bus_arrival(data)
    busList = []
    busButtton = []
    for bus in bus_info:
        if bus['ServiceNo'] not in busList:
            busList.append(bus['ServiceNo'])
            busButtton.append([InlineKeyboardButton(
                text=bus['ServiceNo'], callback_data=bus['ServiceNo'])])
    keyboard = InlineKeyboardMarkup(busButtton)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Here are the buses in this bus stop', reply_markup=keyboard)
    return BUSINFO


info_handler = CallbackQueryHandler(busStopInfo)
dispatcher.add_handler(info_handler)


def busInfo(update, context):
    query = update.callback_query
    query.answer()
    data = query['data']
    bus_info = get_bus_arrival(context.user_data['bus_stop'])
    for bus in bus_info:
        if bus['ServiceNo'] == data:
            bus1time = bus['NextBus']['EstimatedArrival']
            delta1 = datetime.strptime(
                bus1time, '%Y-%m-%dT%H:%M:%S+08:00')-datetime.now()
            bus2time = bus['NextBus2']['EstimatedArrival']
            delta2 = datetime.strptime(
                bus2time, '%Y-%m-%dT%H:%M:%S+08:00') - datetime.now()
            bus3time = bus['NextBus3']['EstimatedArrival']
            delta3 = datetime.strptime(
                bus3time, '%Y-%m-%dT%H:%M:%S+08:00') - datetime.now()
            arrival_time = []
            for delta in [delta1, delta2, delta3]:
                minutes, seconds = divmod(delta, 60)
                arrival_time.append(minutes)
            context.bot.send_message(chat_id=update.effective_chat.id, text='The next bus is coming in {} minutes, second bus is in {} minutes and third bus is in {} minutes'.format(
                arrival_time[0], arrival_time[1], arrival_time[2]))


def done(update, context):
    user_data = context.user_data
    context.bot.send_message(
        chat_id=update.effective_chat.id, text='Thank you for using us')
    user_data.clear()
    return ConversationHandler.END


conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        LOCATIONINFO: [
            MessageHandler(Filters.location, nearest_busstop)
        ],
        BUSSTOPINFO: [
            CallbackQueryHandler(busStopInfo)
        ],
        BUSINFO: [
            CallbackQueryHandler(busInfo)
        ],
    },
    fallbacks=[MessageHandler(Filters.regex('^Done$'), done)]
)
dispatcher.add_handler(conv_handler)
updater.start_polling()
updater.idle()
