"""
hackthon

2019-11-17
ZYX
"""

from flask import Flask, jsonify, request, make_response, url_for,redirect, render_template, session, Session
from flask_httpauth import HTTPBasicAuth
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
import datetime
import pymysql
import random
import os
import midi

app = Flask(__name__, static_url_path = "")
app.config['SECRET_KEY'] = '123456'
auth = HTTPBasicAuth()

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/")
def main():
    Data1 = []
    Data2 = []
    Data3 = []
    pattern = readMidi()
    on = []
    on1 = []
    on2 = []
    off = []
    off1 = []
    off2 = []
    time = 0
    for i in pattern[1]:
        if isinstance(i, midi.events.TextMetaEvent):
            time += (i.tick//5)
        if isinstance(i, midi.events.NoteOnEvent):
            time += (i.tick//5)
            on.append([time, i.data[0]])
        if isinstance(i, midi.events.NoteOffEvent):
            time += (i.tick//5)
            off.append([time, i.data[0]])
    time = 0
    for i in pattern[2]:
        if isinstance(i, midi.events.TextMetaEvent):
            time += (i.tick//5)
        if isinstance(i, midi.events.NoteOnEvent):
            time += (i.tick//5)
            on1.append([time, i.data[0]])
        if isinstance(i, midi.events.NoteOffEvent):
            time += (i.tick//5)
            off1.append([time, i.data[0]])
    time = 0
    for i in pattern[3]:
        if isinstance(i, midi.events.TextMetaEvent):
            time += (i.tick//5)
        if isinstance(i, midi.events.NoteOnEvent):
            time += (i.tick//5)
            on2.append([time, i.data[0]])
        if isinstance(i, midi.events.NoteOffEvent):
            time += (i.tick//5)
            off2.append([time, i.data[0]])
    i = 0
    while i < len(on):
        a = on[i][0]
        b = (off[i][0] - on[i][0])
        c = (127 - on[i][1]) * 20
        Data1.append([a, b, c])
        i += 1
    i = 0
    while i < len(on):
        a = on1[i][0]
        b = (off1[i][0] - on1[i][0])
        c = (127 - on1[i][1]) * 20
        Data2.append([a, b, c])
        i += 1
    i = 0
    while i < len(on):
        a = on2[i][0]
        b = (off2[i][0] - on2[i][0])
        c = (127 - on2[i][1]) * 20
        Data3.append([a, b, c])
        i += 1
    return render_template("index.html", Data1=Data1, Data2=Data2, Data3=Data3)

def readMidi():
    pattern = midi.read_midifile("19.mid")
    # print(pattern[0][1].data[1])
    return pattern

def test():
    Data = []
    pattern = readMidi()
    on = []
    off = []
    time = 0
    for i in pattern[1]:
        if isinstance(i, midi.events.NoteOnEvent):
            time += i.tick
            on.append([time, i.data[0]])
        if isinstance(i, midi.events.NoteOffEvent):
            time += i.tick
            off.append([time, i.data[0]])
    i = 0
    while i < len(on):
        a = on[i][0] // 50
        b = (off[i][0] - on[i][0]) // 50
        c = on[i][1]
        print(c)
        Data.append([a, b, c])
        i += 1
   

if __name__ == '__main__':   
    app.run(debug = True, host= '0.0.0.0')
    #readMidi()
    #test()
