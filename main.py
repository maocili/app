import requests
import json
import jsonpath
from PIL import Image
from io import *
import re

url='http://www.sslyapphome06.win/mz_pbl/jdly_json.php?st=0&en=50&type=2&mode=1'
head= {'User-Agent':'Apache-HttpClient/UNAVAILABLE (java 1.4)'}
html = requests.get(url,head)
jsoncode = json.loads(html.text)
isrc_list = jsonpath.jsonpath(jsoncode,'$..isrc')
for i in isrc_list:
    print(i)
    img_url = requests.get(i)
    image = Image.open(BytesIO(img_url.content))
    image.save('F:/img2/'+i[-29:])