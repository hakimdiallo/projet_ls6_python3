#!/usr/bin/env python3
import os
import re

def extraire_pays(rep,n):
    mail_box = Mailbox(rep)
    d = dict()
    for mail in mail_box.list_mail:
            exp = re.match(r".*?<.*?@.*?\.(.*?)>",mail.origine)
            if exp != None:
                ext = exp.group(0)
                if ext in d:
                    d[ext] = d[ext]+1
                else:
                    d[ext] = 1
    d2 = sorted(d.items(), reverse=True, key=operator.itemgetter(1))[:n]
    for k in d2:
        print(k[0])

if __name__ == '__main__':
