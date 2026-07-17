import json
import os
from typing import Any
from .exceptions import (
   PathNotFoundError,
   InvalidEventError,
   InvalidDataError,
)




class SaveMZ:
    def __init__(self, path: str):
       self.path = path
       self.cache = None 
       self.event = {
          "before_read": set(),
          "after_read": set(),
          "before_write": set(),
          "after_write": set(),
          "before_set": set(),
          "after_set": set(),
          "before_reload": set(),
          "after_reload": set(),
       }

      
         
    
    def file_path(self):
     if os.path.exists(self.path):
         pass
     else:
        with open(self.path,"w",encoding="utf8") as f:
           json.dump({}, f)


    def write(self, data, indent):
        self.emit("before_write", data)
        self.cache = data 
        with open(self.path,"w",encoding="utf8") as f:
          json.dump(self.cache,f,indent=indent,ensure_ascii=False)
        self.emit("after_write", data) 



    def read(self):
        self.emit("before_read")
        if self.cache is None:
          with open(self.path,"r") as d:
             self.cache = json.load(d)
          self.emit("after_read", self.cache)
          print("file")
          return self.cache
        else: 
           print("cache")
           self.emit("after_read", self.cache)
           return self.cache
        


    def get(self, path):
     value = self.read()
     keys = path.split(".")
     for key in keys:
        if key not in value:
           raise PathNotFoundError(f"path {path} was not found.")
        value = value[key]
     return value
   
    def set(self, path: str, data: Any):
       self.emit("before_set", path, data)
       keys = path.split(".")
       obj = self.read()
       value = obj
       for key in keys[:-1]:
          value = value[key]
       value[keys[-1]] = data
       self.write(obj,2)
       self.emit("after_set", path, data)
       

    def delete(self, path: str):
       self.emit("beforee_delete", path)
       keys = path.split(".")
       obj = self.read() 
       value = obj 
       for key in keys[:-1]:
          if key not in value:
           raise PathNotFoundError(f"path {path} was not found.")
          value = value[key]
       del value[keys[-1]]
       self.write(obj,2)
       self.emit("after_delete", path)


    def reload(self):
       self.emit("before_reload")
       self.cache = None
       self.emit("after_reload", self.cache)
       return self.read()
       
    
    def onEvent(self, event_name: str , callback: Any):
       if event_name not in self.event:
          self.event[event_name] = []
       self.event[event_name].add(callback)

    def offEvent(self, event_name: str, callback: Any):
       if event_name in self.event:
          self.event[event_name].discard(callback)


    def emit(self, event_name: str, *args):
       if event_name in self.event:
          for callback in self.event[event_name]:
             callback(*args)
             


