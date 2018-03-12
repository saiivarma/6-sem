# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 23:15:37 2018

@author: pravin
"""

#ELIZA
from nltk import word_tokenize
import random

def Eliza():
    print("    *Say 'bye' to exit*\n")
    print(">Hello, I am Eliza.")
    in1=input().lower()
    rep=in1
    words=word_tokenize(in1)
    f=0
    for x in ['hello','hi']:
        if x in words:
            f=1
            break
    if f==0:
        print(">Don't you ever say Hello?")
    else:
        print(">How are you today.. What would you like to discuss?")
        in1=input().lower()
        print(">Tell me more...")
    neg_replies=['Are you sure?','Are you saying no just to be negative?','Why not?','You are being a bit negative']
    rep_replies=["Do you expect a different answer by repeating yourself?","Please don't repeat yourself!","Why did you repeat yourself?"]
    wh_replies=['Does that question interest you?','What answer would please you the most?','What else comes to mind when you ask that?',\
                'Have you asked such questions before?','Have you asked anyone else?',\
                'Are such questions often on your mind?','Why do you ask?','What is it that you really want to know?']
    while(1):
        in1=input().lower()
        if f==2:
            print("Tell me more...")
            f=0
        elif rep==in1:
            num=random.randint(0,2)
            print(">"+rep_replies[num])
        else:
            rep=in1
            words=word_tokenize(in1)
            if words[0]=='no':
                num=random.randint(0,4)
                print(">"+neg_replies[num])
            elif words[0] in ['who','what','where','when','how','why']:
                num=random.randint(0,8)
                print(">"+wh_replies[num])
                f=2
            elif 'bye' in words:
                print("Good talk. Bye :)")
                break                
            else:
                print(">Tell me more...")
            
Eliza()
        