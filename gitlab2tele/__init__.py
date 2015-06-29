# -*- coding: utf-8 -*-
import telebot
import json


class TeleSender():
    def __init__(self, token, chat_id):
        self.bot = telebot.TeleBot(token)
        self.chat_id = chat_id

    def post_project_event(self, json_string):
        obj = json_string
        event_type = obj['object_kind']
        if event_type == 'push':
            self.__revice_push(obj)

    def __revice_push(self, json_obj):
        msg = self.__parse_push_event(json_obj)
        self.bot.send_message(self.chat_id, msg)

    def __parse_push_event(self, json_obj):
        push_user = json_obj['user_name']
        commit_count = json_obj['total_commits_count']
        repo_url = json_obj['repository']['homepage']
        reop_name = json_obj['repository']['name']
        ret = '%s push %d commits to %s. %s' % (push_user, commit_count, reop_name, repo_url)
        return ret
