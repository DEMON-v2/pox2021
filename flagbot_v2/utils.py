#!/usr/bin/python3

from json import loads

def token_load():
    try:
        with open("./token.json") as token_f:
            token = loads(token_f.read())
            return token['token']
    except:
        print('Token Parsing Error!')