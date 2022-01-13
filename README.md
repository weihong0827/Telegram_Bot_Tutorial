# Telegram Bot Workshop

Telegram is a free and open source, cross-platform, cloud-based instant messaging software. The service also provides end-to-end encrypted video calling, VoIP, file sharing and several other features.

---

# Pre-workshop Instructions

Hello and welcome to the telegram bot workshop notes! Don't be intimidated by the length of the notes, we'll go through every part step-by-step with a lot of the codes provided to you! 

Before the workshop on 21 Jan, we require you to have these installed on your computer: 

- [Heroku](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Python](https://www.python.org/downloads/)

That's all! Thank you and see y'all on Friday 🙂

---

# What is Telegram Bot?

Telegram is a popular chat platform, you should be familiar with it! 

![Untitled](Telegram%20Bot%20Workshop%207e22ca98485740be98a3405865118a62/Untitled.png)

One of the many amazing features of Telegram is their bots. Bots are third-party applications that run inside Telegram. Users can interact with bots by sending them messages, commands and inline requests. You control your bots using HTTPS requests to the Telegram Bot API.

Here are some popular examples of telegram bots used in Singapore: 

![Untitled](Telegram%20Bot%20Workshop%207e22ca98485740be98a3405865118a62/Untitled%201.png)

![Untitled](Telegram%20Bot%20Workshop%207e22ca98485740be98a3405865118a62/Untitled%202.png)

Bus Uncle: show bus timings for your bus stop           Werewolf: use it to play the game with friends!

---

# Get started: Basics

First, head over to your telegram app and find [BotFather](http://t.me/BotFather) (the Bot that controls all Bots). Interact with him using `/start` and you should receive this long list of commands (feel free to try them out yourselves when you're free!): 

![Telegram%20Bot%20Workshop%207e22ca98485740be98a3405865118a62/Untitled%203.png](Telegram%20Bot%20Workshop%207e22ca98485740be98a3405865118a62/Untitled%203.png)

Let's start with `/newbot` and follow the command to create a new bot. Feel free to name it whatever you'd like, but we'll be creating a bus timing bot (similar to @sgbusunclebot above). Do note that the bot username has to be unique and creative as many may have already been taken by other bots.

![Telegram%20Bot%20Workshop%207e22ca98485740be98a3405865118a62/Untitled%204.png](Telegram%20Bot%20Workshop%207e22ca98485740be98a3405865118a62/Untitled%204.png)

Upon completion, you will get the access token for your bot, which in this case is `1896366196:AAH7L1bQzfYljesEMwDrNzfr0gSg-gHveUk` , and you can start chatting with your bot using the link `[t.me/<nameOfYourBot>](http://t.me/<nameOfYourBot>)` which is also given in the message. Your bot won't reply you now because it's empty but it will soon! You can also take a look at the documentation link that they provide you for more information. 

Now you can use HTTP request to access your bot and code it to whatever you want. This can be done in many different languages such as Python and Java, so you can integrate telegram bot to your future projects easily. You can also use your web browser directly or Postman for better experience. 

## Getting the basic info of your Bot

`https://api.telegram.org/bot<YourBotToken>/getMe`

For Postman, it beautifies the json code that the telegram server returns (helps you read it better). 

The response of this request gives the basic info of the bots that you have just created using bot father.

![Telegram%20Bot%20Workshop%207e22ca98485740be98a3405865118a62/Untitled%205.png](Telegram%20Bot%20Workshop%207e22ca98485740be98a3405865118a62/Untitled%205.png)

The following image shows what you get when you use a web browser (possible, but harder to read). We'll use Postman for this workshop for better readability. 

![Telegram%20Bot%20Workshop%207e22ca98485740be98a3405865118a62/Untitled%206.png](Telegram%20Bot%20Workshop%207e22ca98485740be98a3405865118a62/Untitled%206.png)

## Interacting with the Bot

### Receiving Message from User

Use the link `https://api.telegram.org/bot<YourBotToken>/getUpdates` to get the message that users send to the bot. You can see all the parameters that you can pass to this method [here](https://core.telegram.org/bots/api#update).

![Telegram%20Bot%20Workshop%207e22ca98485740be98a3405865118a62/Untitled%207.png](Telegram%20Bot%20Workshop%207e22ca98485740be98a3405865118a62/Untitled%207.png)

You can see that after the message `Hi` the bot receives it with no problem and provides you with essential information like `id` of the user for you to identify the sender.

### Sending Message

Use the link `[https://api.telegram.org/bot<YourBotToken>/sendMessage](https://api.telegram.org/bot<YourBotToken>/sendMessage)` to send messages out from the bot to the user. To respond to the input message from the user, we can draft a reply.

![Telegram%20Bot%20Workshop%207e22ca98485740be98a3405865118a62/Untitled%208.png](Telegram%20Bot%20Workshop%207e22ca98485740be98a3405865118a62/Untitled%208.png)

To send out this message to the specific message sent by the user, send this link: `https://api.telegram.org/bot1896366196:AAH7L1bQzfYljesEMwDrNzfr0gSg-gHveUk/sendMessage?chat_id=623050671&text=welcome%20to%20the%20workshop`

The parameters are passed using [URL Query String](https://en.wikipedia.org/wiki/Query_string), but telegram also supports `application/x-www-form-urlencoded`, `application/json (except for uploading files)` and `multipart/form-data (use to upload files)`

The full list of parameters for this method can be found [here](https://core.telegram.org/bots/api#sendmessage).

## Available methods

The list of available methods for the telegram bot api can be found [here](https://core.telegram.org/bots/api#available-methods).

We will not go through everything, so do read up on the documentation on your own for the methods that suits your individual projects.

---

# Python Telegram Bot

The above method of making http requests manually is very slow and inefficient so we will want to automate it using scripts and [Python Telegram Bot](https://github.com/python-telegram-bot/python-telegram-bot)  is a very good library for use to interact with the telegram bot API since it wraps most of the methods in python and make our lives much easier.

## Set up

### Set up a virtual environment:

This is for better package management

`python -m venv env`

On Windows, run:

`env\Scripts\activate.bat`

On Unix or MacOS, run:

`source env/bin/activate`

### Install library

You can install or upgrade python-telegram-bot with:

`pip install python-telegram-bot --upgrade`

## **Use of a text editor**

- Here are some of the recommendations
- [Visual Studio Code](https://code.visualstudio.com/download)
- [Sublime Text](https://www.sublimetext.com/3)
- [PyCharm](https://www.jetbrains.com/pycharm/download)

Open the folder you just created using a text editor. 

## What we are making

We will be making a telebot similar to the @sgbusunclebot, where it will take do the following: 

1. Say hello on `/start`
2. Give bus stops near you (based on location input)
3. Give buses in chosen bus stop 
4. Give upcoming bus timings for chosen bus number 
5. Say bye on `/done`

## Coding your bot: Send message on `/start`

Create a file `bot.py`

***Some of the content below are taken from the telegram bot library documentation.***

The `Updater` class continuously fetches new updates from telegram and passes them on to the `Dispatcher` class. If you create an `Updater` object, it will create a `Dispatcher` for you and link them together with a `Queue`. You can then register handlers of different types in the `Dispatcher`, which will sort the updates fetched by the `Updater` according to the handlers you registered, and deliver them to a callback function that you defined.

![Telegram%20Bot%20Workshop%207e22ca98485740be98a3405865118a62/updaterdispatcher.png](Telegram%20Bot%20Workshop%207e22ca98485740be98a3405865118a62/updaterdispatcher.png)

So, *let's get started!* Again, please fire up a Python command line if you want to follow this tutorial.

First, you have to create an `Updater` object. Replace `'TOKEN'` with your Bot's API token.

```python
from telegram.ext import Updater
updater = Updater(token='TOKEN', use_context=True)
```

For quicker access to the `Dispatcher` used by your `Updater`, you can introduce it locally:

```python
dispatcher = updater.dispatcher
```

Now, you can define a function that should process a specific type of update:

```python
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
```

The goal is to **have this function called every time the Bot receives a Telegram message that contains the `/start` command**. To accomplish that, you can use a `CommandHandler` (one of the provided `Handler` subclasses) and register it in the dispatcher:

```python
from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
```

And that's all you need. To start the bot, run:

```python
updater.start_polling()
updater.idle()
```

`start_polling` constantly fetches the data from the API to see whether there is any updates coming in to the bot, you can define parameters like `interval` and `timeout`, more can be found [here](http://python-telegram-bot.readthedocs.io/en/latest/telegram.ext.updater.html#telegram.ext.updater.Updater.start_polling).

Use the `MessageHandler`, another `Handler` subclass, to echo all text messages:

```python
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

from telegram.ext import MessageHandler, Filters #add to import list at the top 
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)
```

**Related docs:** `[telegram.ext.MessageHandler](http://python-telegram-bot.readthedocs.io/en/latest/telegram.ext.messagehandler.html)`, `[telegram.ext.filters](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.filters.html)`

Only those messages that passes the filters that you have defined will enter the function.

The filters works pretty much like python `if,else` logic so should be pretty easily to handle, they also offer a lot of different filter types like `file type` ,`regular expression`, etc.

After running it, you should see something like this: 

![Untitled](Telegram%20Bot%20Workshop%207e22ca98485740be98a3405865118a62/Untitled%209.png)

## Coding your bot: Fetching nearby bus stops from location input

To do this, we will integrate a publicly available dataset of bus timings, which can be found [here](https://datamall.lta.gov.sg/content/datamall/en/dynamic-data.html). We've already compiled the code to retrieve the bus timings here, and you may download it and add it to your project folder. Follow up by importing this file in your main.py file. 

[bus_api.py](Telegram%20Bot%20Workshop%207e22ca98485740be98a3405865118a62/bus_api.py)

Basically what this code does is have the nearby bus stops fetched from a location input using the function `get_bus_stops(my_cord)`, and `get_bus_arrival(busStopCode)` helps to fetch the buses at the chosen bus stop, along with their arrival timings. 

For this file to work, you will need to install an external library to calculate the distance between two coordinates

```python
pip install git+https://github.com/MartinThoma/mpu.git
```

Now jump back to your main .py file. The goal of this step is to **show the nearby bus stops based on the location input.** The interaction should show something like this: 

![Untitled](Telegram%20Bot%20Workshop%207e22ca98485740be98a3405865118a62/Untitled%2010.png)

We have to make a function that will fetch the location input (update), data from the `bus_api.py` file, and send a message back with the `context.bot.send_message`. As we provided the code to compile the bus timings, here's the code to pull the bus stop information: 

```python
def nearest_busstop(update, context):
    location = update.message.location
    result = get_bus_stops((location['latitude'], location['longitude']))
    buttons = []
    for data in result:
        buttons.append([InlineKeyboardButton(text=data['Description'], callback_data=data['BusStopCode'])])
    keyboard = InlineKeyboardMarkup(buttons)
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Base on your location, " +
             "here are the bus stops nearest to you, " +
             "which one are you at", reply_markup=keyboard)
		#this return will come into play later
    return BUSSTOPINFO
```

Remember to add the handler to the dispatcher so the bot will know to respond the location input with this output. 

```python
location_handler = MessageHandler(Filters.location, nearest_busstop)
dispatcher.add_handler(location_handler)
```

## Coding your bot: Fetching buses at bus stop and timings

The next step would be to **fetch the chosen bus stop based on the user's location, and show the buses at that bus stop.** It should show an output like this (in this case, there's only one bus at this bus stop, but for bus stops with multiple bus stops, there will be multiple options): 

![Untitled](Telegram%20Bot%20Workshop%207e22ca98485740be98a3405865118a62/Untitled%2011.png)

To do this, we make a similar function, this time with the input being a chosen option. 

```python
def busStopInfo(update,context):
    query = update.callback_query
    print('busstop',query)
    query.answer()
    data = query['data']
    print(data)
    context.user_data['bus_stop'] = data
    bus_info = get_bus_arrival(data)
    busList =[]
    busButtton = []
    for bus in bus_info:
        if bus['ServiceNo'] not in busList:
            busList.append(bus['ServiceNo'])
            busButtton.append([InlineKeyboardButton(text=bus['ServiceNo'],callback_data=bus['ServiceNo'])])
    keyboard = InlineKeyboardMarkup(busButtton)
    context.bot.send_message(chat_id = update.effective_chat.id,text='Here are the buses in this bus stop',reply_markup=keyboard)
    return BUSINFO
```

Add the handler to the dispatcher. Have you gotten the hang of it yet? 😉

```python
info_handler = CallbackQueryHandler(busStopInfo)
dispatcher.add_handler(info_handler)
```

The user would next pick the bus they want to see the timings for, so the next step would be to **fetch the bus timings for that bus at that bus stop.** Recall that this data is being pulled from a publicly available dataset that we've already compiled for you in `bus_api.py`. To fetch this data, you can insert another function:

```python
def busInfo(update, context):
    query = update.callback_query
    print('bus', query)
    query.answer()
    data = query['data']
    # get all the bus info in that busstop
    bus_info = get_bus_arrival(context.user_data['bus_stop'])
    print('bus info', bus_info)
    for bus in bus_info:
        # if the bus number match what the user want to find then procceed
        if bus['ServiceNo'] == data:
            now = datetime.now()  # this timing created is a datetime object

            bus1time = bus['NextBus']['EstimatedArrival']  # this timing obtain is just string

            # if we want to find the arrival time, we need to subtract this two timing, however they are of different obj
            # just like you cant subtract a string from an integer we cant subtract a datetime object from a string
            # hence we will need to convert the string to datetime object so that we can subtract both of them to get the difference in time

            delta1 = datetime.strptime(bus1time, '%Y-%m-%dT%H:%M:%S+08:00') - now

            bus2time = bus['NextBus2']['EstimatedArrival']
            delta2 = datetime.strptime(bus2time, '%Y-%m-%dT%H:%M:%S+08:00') - now
            bus3time = bus['NextBus3']['EstimatedArrival']
            delta3 = datetime.strptime(bus3time, '%Y-%m-%dT%H:%M:%S+08:00') - now
            arrival_time = []
            for delta in [delta1, delta2, delta3]:
                minutes, seconds = divmod(delta.seconds, 60)
                arrival_time.append(minutes)
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='The next bus is coming in {} minutes, second bus is in {} minutes and third bus is in {} minutes'.format(
                                         arrival_time[0], arrival_time[1], arrival_time[2]))
            return LOCATIONINFO
```

But wait! Do we still need to add the handler to the dispatcher like what we used to do previously?

```python
busInfo_handler = CallbackQueryHandler(busInfo)
dispatcher.add_handler(busInfo_handler)
```

Note that we now have two `CallbackQueryHandler` added in the dispatcher now, how does the bot know which function to go when a new callback query comes in?

Two solutions:

1. Regular Expression:
    1. The function `CallbackQueryHandler` accepts a `pattern` as a parameter where you can write a regular expression for this particular handler, so only when the message style match this pattern then it will enter the function.
2. Conversation Handler:
    1. This is the approach that we are going to take.
    2. This conversation handler basically describes how the users should interact with the bot with a predetermined flow. (read more about it [here](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.conversationhandler.html)).

```python
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],

    states={
        LOCATIONINFO: [
            MessageHandler(Filters.location, nearest_busstop)
        ],
        BUSSTOPINFO: [
            CallbackQueryHandler(busStopInfo, pattern='')
        ],
        BUSINFO: [
            CallbackQueryHandler(busInfo, pattern='')
        ],
    },
    fallbacks=[CommandHandler('done', done)]
)
```

This is the part where all the chosen option inputs from the individual functions come into play. We also no longer need to register the individual handlers.

Your output should show something like this now: 

![Untitled](Telegram%20Bot%20Workshop%207e22ca98485740be98a3405865118a62/Untitled%2012.png)

## Coding your bot: Final steps

Let's add one more quick function to stop the bot from running and end it with a `/done`command. Very similar to the initial `/start` function we had, let's make one for the `/done` command. 

```python
def done(update,context):
    user_data = context.user_data
    context.bot.send_message(chat_id = update.effective_chat.id,text='Thank you for using us')
    user_data.clear()
    return ConversationHandler.END
```

The output should show something like this: 

![Untitled](Telegram%20Bot%20Workshop%207e22ca98485740be98a3405865118a62/Untitled%2013.png)

Notice the `ConversationHandler.END` at the end of the function code? This basically means the bot has just completed its conversation and will proceed to stop running. 

## Test it out!

Your bot should be done by this point! Try and deploy it and see how it interacts with you. You should get something like this: 

![Untitled](Telegram%20Bot%20Workshop%207e22ca98485740be98a3405865118a62/Untitled%2014.png)

---

## Time to deploy!

This section is created based on [this](https://towardsdatascience.com/how-to-deploy-a-telegram-bot-using-heroku-for-free-9436f89575d2) medium article, but note that some of its code is outdated.

Now that we have finished our bot and it is running successfully in local environment, we should deploy it for everybody to use!

We will use Heroku to deploy our bot. Click [here](https://towardsdatascience.com/how-to-deploy-a-telegram-bot-using-heroku-for-free-9436f89575d2) for a complete guide on how to use it!

## **Creating your Heroku Webapp**

With the three files in the same directory, we will now create the Heroku Webapp.

1. Login / [create](https://signup.heroku.com/dc) a Heroku account.
2. Install the [Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up). If you do not have Git installed, first [install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) before proceeding with the Heroku CLI.
3. Once installed, you can use the *heroku* command in your terminal / command prompt. Go to the same directory as your python files, and type:

```
heroku login
```

A new window will be opened in your browser prompting you to login, so just click on the button.

![https://miro.medium.com/max/1400/1*XlClS5Mu9y5qEDPIB8z8Ng.png](https://miro.medium.com/max/1400/1*XlClS5Mu9y5qEDPIB8z8Ng.png)

4. Once you are logged in, go back to the command line. Type in

```
heroku create
```

to create your new webapp. Here, heroku will assign your webapp a name as well as the link to your webapp, which should be of the format [https://yourherokuappname.herokuapp.com/.](https://yourherokuappname.herokuapp.com/) Paste the URL into the bot.py code, for the line

### **Heroku**

On Heroku using webhook can be beneficial on the free-plan because it will automatically manage the downtime required. The reverse proxy is set up for you and an environment is created. From this environment you will have to extract the port the bot is supposed to listen on. Heroku manages the SSL on the proxy side, so you don't have provide the certificate yourself.

```python
import os

PORT = int(os.environ.get('PORT', '8443'))

#change update.start_polling() to the following
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=Token,
                      webhook_url="https://<appname>.herokuapp.com/" + Token)
updater.idle()
```

### Procfile

The procfile declares the process type followed by the command, in the format <process type>: <command>. Here, we are using the web process type, which receives external HTTP traffic from Heroku’s routers. The command is python3 bot.py, which tells Heroku to execute the python file as you normally would with a python file locally. So your Procfile should contain the line:

```
web: python3 bot.py
```

Make sure that the Procfile does not have any file extension like .txt behind it, because it won’t work.

### requirements.txt

This file is very essential in most if not all of the python project build because the file records the all the external libraries and their versions down so that running this same project on other machines will be much eaiser

Run the following command to create the requirements.txt

```python
pip freeze --> requirements.txt
```

Check your directory, now you should have

```python
bot.py
bus_api.py
Procfile
requirements.txt
```

### Finally

Next, in your command line, type in

```
git init
git add .
git commit -m "first commit"
heroku git:remote -a YourAppName
git push heroku
```

The following should be sample output

![Untitled](Telegram%20Bot%20Workshop%207e22ca98485740be98a3405865118a62/Untitled%2015.png)

### Dashboard

Login to you Heroku account and you should see the app that you have created

![Untitled](Telegram%20Bot%20Workshop%207e22ca98485740be98a3405865118a62/Untitled%2016.png)

Click into the project you should see the project overview, you can try to debug what is wrong in the logs

![Untitled](Telegram%20Bot%20Workshop%207e22ca98485740be98a3405865118a62/Untitled%2017.png)

Last thing to fix! The timezone by default uses UTC+0 but Singapore uses UTC+8. Even the timing we obtained from the `bus_api.py` is in UTC+8, so when we calculate timing difference, there will be a 8 hour difference, which is not what we want.

![Untitled](Telegram%20Bot%20Workshop%207e22ca98485740be98a3405865118a62/Untitled%2018.png)

After adding the Config Vars they should do the trick. The list of timezones can be found [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

## House keeping stuff

Let's not forget our dear BotFather! We can do a lot of stuff with him.

Set description for the bot, set profile for the bot and set command for the bot. Explore and discover it for yourself!

---

# A non-code way?

There are actually non-techncical ways of creating your telegram bot! Although we recommend using Python to practice your coding skills and making it work better, there are some publicly accessible interfaces online you can use to make your telegram bots quicker. We won't be going through them, but here are some resources you may turn to: 

- [SendPulse](https://sendpulse.com/): initiate the same way with BotFather to get the bot access token, then go to SendPulse to sign up and use their UI to build your chatbot using flowcharts. You do have to sign up to access the API though!

![Untitled](Telegram%20Bot%20Workshop%207e22ca98485740be98a3405865118a62/Untitled%2019.png)

- [Azure Bot Service](https://azure.microsoft.com/en-us/services/bot-services/#overview): use Microsoft Azure's UI to build your chatbot. Click [here](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-channel-connect-telegram?view=azure-bot-service-4.0) for a step-by-step tutorial.

---

# Conclusion

We hope this crash course in telegram bot programming was helpful for you to learn the basics of it through a simple bus app example. This material is created with the help from the python telegram bot library's documentations, check it out [here](https://github.com/python-telegram-bot/python-telegram-bot).

If you missed any parts of our work, you can re-watch the workshop on Slack (posted by WTH) or you may refer to our full code [here](https://github.com/weihong0827/Telegram_Bot_Tutorial)

This workshop is brought to you by SUTD's Digital Development & Design Club! Happy hacking!

![Untitled](Telegram%20Bot%20Workshop%207e22ca98485740be98a3405865118a62/Untitled%2020.png)
