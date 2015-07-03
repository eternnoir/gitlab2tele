# -*- coding: utf-8 -*-
import telebot
import json


class TeleSender():
    def __init__(self, token, chat_id):
        self.bot = telebot.TeleBot(token)
        self.chat_id = chat_id

    def post_project_event(self, json_obj):
        obj = json_obj
        event_type = obj['object_kind']
        if event_type == 'push':
            self.__revice_push(obj)
        if event_type == 'merge_request':
            self.__revice_merge_request(obj)

    def __revice_push(self, json_obj):
        msg = self.__parse_push_event(json_obj)
        self.bot.send_message(self.chat_id, msg)

    def __parse_push_event(self, json_obj):
        push_user = json_obj['user_name']
        commit_count = json_obj['total_commits_count']
        repo_url = json_obj['repository']['homepage']
        repo_name = json_obj['repository']['name']
        ret = '%s push %d commits to %s. %s' % (push_user, commit_count, repo_name, repo_url)
        return ret

    def __revice_merge_request(self, json_obj):
        msg = self.__parse_merge_request(json_obj)
        self.bot.send_message(self.chat_id, msg)

    def __parse_merge_request(self, json_obj):
        request_user = json_obj['user']['name']
        mr_title = json_obj['object_attributes']['title']
        url = json_obj['object_attributes']['url']
        action = json_obj['object_attributes']['action']
        ret = u'%s %s a merge request : %s. %s' % (request_user, action, mr_title, url)
        return ret
