# Function to create JSON messages

import json
from time import time


def get_authenticate_message(username, password):
    if not is_long_name(username):
        return merge_jsons(get_action_json('authenticate'),
                           get_time_json(),
                           get_user_json(username, password))


def get_action_json(action, extend_json=None):
    json_data = {}
    json_data['action'] = action
    if extend_json is not None:
        json_data = {**json_data, **json.loads(extend_json)}
    json_object = json.dumps(json_data)
    return json_object


def get_user_json(username, password):
    user_data = {}
    user_data['account_name'] = username
    user_data['password'] = password
    json_data = {}
    json_data['user'] = user_data
    return json.dumps(json_data)


def get_time_json():
    time_data = {}
    time_data['time'] = time()
    return json.dumps(time_data)


def merge_jsons(*jsons):
    merged_json_data = {}
    for each_json in jsons:
        merged_json_data = {**merged_json_data, **json.loads(each_json)}
    return json.dumps(merged_json_data)


def is_long_name(name):
    return len(name) > 25
