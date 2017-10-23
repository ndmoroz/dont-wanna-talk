# Functions to create JIM messages

import json as json_module
from time import time
from errors import \
    NotMessageError, \
    LongUsernameError, \
    WrongResponseCodeError, \
    UnknownMessageFormatError


class Enum:
    def __contains__(self, item):
        return item in {value for attr, value in
                        zip(self.__class__.__dict__.keys(),
                            self.__class__.__dict__.values())
                        if not attr.startswith('__')}


class JimField(Enum):
    action = 'action'  # what to do
    time = 'time'  # current unix-time
    user = 'user'  # who does action
    type = 'type'  # presence message type
    user_name = 'account_name'  # user subfield
    user_password = 'password'  # user subfield
    user_status = 'status'  # user subfield - presence message
    response = 'response'  # server response
    alert = 'alert'  # server warns
    error = 'error'  # server can't do
    sendto = 'to'  # send message to
    sendfrom = 'from'  # who sends message
    encoding = 'encoding'  # encoding of message text
    message = 'message'  # message text
    chatroom = 'room'  # chat room to join or leave


class JimAction(Enum):
    presence = 'presence'  # i am online
    probe = 'probe'  # are you online?
    msg = 'msg'  # i send message
    quit = 'quit'  # i disconnect
    authenticate = 'authenticate'  # sign me in
    join = 'join'  # i join chat
    leave = 'leave'  # i leave chatroom


class JimCode(Enum):
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


def get_presence_message(username, *status):
    if is_long_name(username):
        raise LongUsernameError(username)
    if status:
        user = {JimField.user_name: username,
                JimField.user_status: status[0]}
        message = {JimField.action: JimAction.presence,
                   JimField.time: time(),
                   JimField.type: JimField.user_status,
                   JimField.user: user}
    else:
        user = {JimField.user_name: username}
        message = {JimField.action: JimAction.presence,
                   JimField.time: time(),
                   JimField.user: user}
    return message


def get_probe_message():
    message = {JimField.action: JimAction.probe,
               JimField.time: time()}
    return message


def get_response_message(response_code, **message):
    if (response_code not in JimCode()):
        raise WrongResponseCodeError(response_code)
    if 'alert' in message:
        message = {JimField.response: response_code,
                   JimField.alert: message['alert']}
    elif 'error' in message:
        message = {JimField.response: response_code,
                   JimField.error: message['error']}
    else:
        message = {JimField.response: response_code}

    return message


def get_authenticate_message(username, password):
    if is_long_name(username):
        raise LongUsernameError(username)
    user = {JimField.user_name: username,
            JimField.user_password: password}
    message = {JimField.action: JimAction.authenticate,
               JimField.time: time(),
               JimField.user: user}
    return message


def get_message(send_to, send_from, message, encoding='utf-8'):
    if is_long_name(send_from):
        raise LongUsernameError(send_from)
    if is_long_name(send_to):
        raise LongUsernameError(send_to)
    message = {JimField.action: JimAction.msg,
               JimField.time: time(),
               JimField.sendto: send_to,
               JimField.sendfrom: send_from,
               JimField.encoding: encoding,
               JimField.message: message}
    return message


def get_message_text(message_dict):
    if is_message(message_dict):
        return message_dict['message']
    else:
        raise NotMessageError(message_dict)


def get_message_sendto(message_dict):
    if is_message(message_dict):
        return message_dict['to']
    else:
        raise NotMessageError(message_dict)


def get_message_sendfrom(message_dict):
    if is_message(message_dict):
        return message_dict['from']
    else:
        raise NotMessageError(message_dict)


def get_quit_message():
    message = {JimField.action: JimAction.quit}
    return message


def is_message(message):
    is_action_msg = ('action' in message) and \
                    (message['action'] == JimAction.msg)
    has_to_and_from = ('to' in message) and ('from' in message)
    has_message = 'message' in message
    return is_action_msg and has_to_and_from and has_message


def is_long_name(name):
    return len(name) > 25


def json(func):
    return json_module.dumps(func)


def dejson(func):
    return json_module.loads(func)


def get_message_type(message):
    try:
        return message[JimField.action]
    except:
        raise UnknownMessageFormatError(message)


def get_username(message):
    try:
        user = message[JimField.user]
        return user[JimField.user_name]
    except:
        raise UnknownMessageFormatError(message)
