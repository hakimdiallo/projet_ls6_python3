#!/usr/bin/env python3

class Message:
    """Classe Message"""
    def __init__(self,name,origine,dest,date,sujet=None,reply_to=None,received=None,mess_id=None,spam_level=None,spam_score=None):
        self.name = name
        self.origine = origine
        self.dest = dest
        self.date = date
        self.sujet = sujet
        self.reply_to = reply_to
        self.received = received
        self.mess_id = mess_id
        self.spam_level = spam_level
        self.spam_score = spam_score

    def __str__(self):
        return "Name: %s\From: %s\To: %s\nDate: %s\Subject: %s\nReply-To: %s\nReceived: %s\nMessage-id: %s\nX-Spam-Level: %s\nX-Spam-Score: %s\n" %(self.name,self.origine,self.dest,self.date,self.sujet,self.reply_to,self.received,self.mess_id,self.spam_level,self.spam_score)
