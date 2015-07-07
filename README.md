# gitlab2tele
Gitlab webhook integrate with the Telegram

## Install requirements

```
$ pip install -r requirements.txt
```

## Set environment variable and run

```
$ export PORT=8888      #Default is 8080
$ export TOKEN=<TOKEN>
$ export CHAT_ID=<Chat_id_you_want_notify>
$ python runserver.py
```

Get bot token : [https://core.telegram.org/bots](https://core.telegram.org/bots)

* Set webhook in gitlab. http://your.ip:port/gitlab/project
