from pathlib import Path
import asyncio as a
import os
import pandas as pd
import csv
class File():
    p = Path(__file__).parent
    def __init__(self, file):
        self.f = file

    def get(self, name_file) -> None:
        path = os.path.join(self.p, "data", name_file)
        print(path)
        
        if os.path.exists(path):
            read = pd.read_csv(path)
            print(read)
            return
        
        print(f"File Not Found, Created {name_file} !!")
        return
        
    async def post(self, data:dict, name_file = "data.csv"):
        d = os.path.dirname(os.path.join(self.p, self.f))
        
        for i in os.listdir(os.path.dirname(d)):
            path = os.path.join(os.path.dirname(d), i)
            if os.path.isdir(path) and i == "data":
                file_path = os.path.join(path, name_file)
                if not os.path.exists(file_path):
                    with open(file_path, "w", encoding="utf-8", newline="") as w:
                        print("Create File")
                        writer = csv.DictWriter(w, fieldnames=data.keys())
                        writer.writeheader() 
                        writer.writerow(data)
                else:
                    with open(file_path, "a", encoding="utf-8", newline="") as w:
                        print("Add File")
                        writer = csv.DictWriter(w, fieldnames=data.keys())
                        writer.writerow(data)
                        
    @property
    def file(self):
        return self.file
    
    @file.setter
    def file(self, newfile):
        if isinstance(newfile, str):
            self.file = newfile
            return self.file
        
        raise Exception("Pass the value of File!!")
    
    @property
    def path_created(self) -> dict:
        return self.archive_created