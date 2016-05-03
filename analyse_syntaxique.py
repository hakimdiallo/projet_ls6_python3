#!/usr/bin/env python3

class Message:

    def __init__(self,name,origine,dest,date,sujet=None,reply_to=None,received=None,mess_id=None,spam_level=None,spam_score=None):
        self.name = name
        self.origine = origine
        self.dest = dest
        self.date = date
        
