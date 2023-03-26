import json

class config:
    def __init__(self):
        conf_file = 'modules/config.json'
    
        with open(conf_file) as f:
            conf = json.loads(f.read())
        self.conf = conf


