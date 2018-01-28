from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os
import binascii


class monogo(object):

    db = None

    def Init():
        client = MongoClient("flasktest", host='127.0.0.1', port=27017)

        if client in None:
            raise Exception('no mongo')

        monogo.db = client.flasktest

    def AddChatLog(sender, text):
        log = {'id': binascii.b2a_hex(os.urandom(
            15)), 'sender': sender, 'text': text}
        monogo.db.chatlog.insert_one(log)

    def Getlast20():
        output = ""
        rows = db.chatlog.find().sort({x: -1}).limit(20)
        for Item in rows:
            output += '<li>' + Item['sender'] + ':' + Item['sender'] + '</li>'
        return output
