from pymongo import MongoClient
import os
import binascii


class monogo(object):

    db = None

    def Init():
        client = MongoClient(port=27020)
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
