#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask import Flask, request
import gitlab2tele
import logging

app = Flask(__name__)
app.logger.setLevel(level=0)
app.logger.addHandler(logging.StreamHandler())
TOKEN = os.environ['TOKEN']
CHAT_ID = int(os.environ['CHAT_ID'])
app.logger.info('TOKEN:' + TOKEN)
app.logger.info('CHAT_ID: ' + str(CHAT_ID))


@app.route("/gitlab/project", methods=["PUT", "POST"])
def gitlab_project():
    json_obj = request.get_json()
    app.logger.info(json_obj)
    ts = gitlab2tele.TeleSender(TOKEN, CHAT_ID)
    ts.post_project_event(json_obj)
    return 'OK'


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run('0.0.0.0', port=port, debug=True)
