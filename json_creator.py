# Functions to create JIM messages

import json as json_module
from time import time
from errors import NotMessageError

class JimAction:
    presence = 'presence'  # i am online
    probe = 'probe'  # are you online?
    msg = 'msg'  # i send message
    quit = 'quit'  # i disconnect
    authenticate = 'authenticate'  # sign me in
    join = 'join'  # i join chat
    leave = 'leave'  # i leave


class JimCode:
    standard_notification = 100
    important_notification = 101
    ok = 200
    created = 201
    accepted = 202
    wrong_request = 400
    not_authorized = 401
    wrong_name_pass = 402
    user_forbidden = 403
    user_not_found = 404
    user_conflict = 409
    user_gone = 410
    server_error = 500


class JsonGenerator:
    def __init__(self):
        self.data = {}

    def add_action(self, action):
        self.data['action'] = action

    def add_time(self):
        self.data['time'] = time()

    def add_type(self, type):
        self.data['type'] = type

    def add_user(self, user):
        self.data['user'] = user.data

    def add_account_name(self, account_name):
        self.data['account_name'] = account_name

    def add_status(self, status):
        self.data['status'] = status

    def add_password(self, password):
        self.data['password'] = password

    def add_response(self, response):
        self.data['response'] = response

    def add_alert(self, alert):
        self.data['alert'] = alert

    def add_error(self, error):
        self.data['error'] = error

    def add_to(self, destination):
        self.data['to'] = destination

    def add_from(self, author):
        self.data['from'] = author

    def add_message(self, message):
        self.data['message'] = message

    def get_dict(self):
        return self.data

    def get_json(self):
        return json_module.dumps(self.data)


class MessageBuilder:
    def get_presence_json(self, username, status):
        if is_long_name(username):
            return
        user_data = JsonGenerator()
        user_data.add_account_name(username)
        user_data.add_status(status)

        json_data = JsonGenerator()
        json_data.add_action(JimAction.presence)
        json_data.add_time()
        json_data.add_type('status')
        json_data.add_user(user_data)
        return json_data.get_dict()

    def get_probe_json(self):
        json_data = JsonGenerator()
        json_data.add_action(JimAction.probe)
        json_data.add_time()
        return json_data.get_dict()

    def get_empty_response_json(self, response):
        json_data = JsonGenerator()
        json_data.add_response(response)
        return json_data.get_dict()

    def get_authenticate_json(self, username, password):
        if is_long_name(username):
            return
        user_data = JsonGenerator()
        user_data.add_account_name(username)
        user_data.add_password(password)

        json_data = JsonGenerator()
        json_data.add_action(JimAction.authenticate)
        json_data.add_time()
        json_data.add_user(user_data)
        return json_data.get_dict()

    def get_message(self, send_from, send_to, message):
        jim_data = JsonGenerator()
        jim_data.add_action(JimAction.msg)
        jim_data.add_time()
        jim_data.add_to(send_to)
        jim_data.add_from(send_from)
        jim_data.add_message(message)
        return jim_data.get_dict()

    def get_quit(self):
        jim_data = JsonGenerator()
        jim_data.add_action(JimAction.quit)
        return jim_data.get_dict()

    def get_message_text(self, message_dict):
        if is_message(message_dict):
            return message_dict['message']
        else:
            raise NotMessageError(message_dict)


def is_long_name(name):
    return len(name) > 25


def json(func):
    return json_module.dumps(func)


def dejson(func):
    return json_module.loads(func)
