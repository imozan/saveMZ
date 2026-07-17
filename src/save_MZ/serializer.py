import json   

def reads(string):
  data = json.loads(string)
  return data
        

def writes(data, indent):
      json.dumps(data,indent=indent,ensure_ascii=False)
