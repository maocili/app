import requests
import json
import jsonpath
from PIL import Image
from io import *
import re
class ssly(object):
    def __init__(self):
        self.st=0
        self.en=50
        self.type=1
        self.filepath='F:/img2/'
        self.head = {'User-Agent':'Apache-HttpClient/UNAVAILABLE (java 1.4)'}

    def search(self):
        self.url = 'http://www.sslyapphome06.win/mz_pbl/jdly_json.php?st=' + str(self.st) + '&en=' + str(self.en) + '&type=' + str(self.type) + '&mode=1'
        html = requests.get(self.url,self.head)
        jsoncode = json.loads(html.text)
        isrc_list = jsonpath.jsonpath(jsoncode,'$..isrc')
        for i in isrc_list:
            print(i)
            img_url = requests.get(i)
            image = Image.open(BytesIO(img_url.content))
            image.save(self.filepath+i[-29:])

sslys=ssly()