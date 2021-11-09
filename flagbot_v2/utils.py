#!/usr/bin/python3

from json import loads

def token_load():
    try:
        with open("./token.json") as token_f:
            token = loads(token_f.read())
            return token['token']
    except:
        print('Token Parsing Error!')

def channel_check(channel_id):
    if channel_id == 907406222603464764:
        return True
    else:
        return False