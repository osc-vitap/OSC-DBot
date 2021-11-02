import json

def commands(message):
    with open ('data.json', 'r') as f:
        data = json.load(f)
    response = "No command found. Use !help for more details"
    prefix = data['prefix']
    
    for temp in data['commands'][0].keys():
        if message == prefix + temp:
            response = data["commands"][0][temp]
            return response
    return ""