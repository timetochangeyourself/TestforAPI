import requests
import webbrowser
import json
import jsonpath
import pytest
from selenium import webdriver

#driver = webdriver.Chrome('E:\Webdriver\chromedriver')
randCat = "http://aws.random.cat/meow"
randDog = "https://random.dog/woof.json"
randFox = "https://randomfox.ca/floof/"

otvetCat = requests.get(randCat)
json_response = json.loads(otvetCat.text)
pagesCat = jsonpath.jsonpath(json_response, 'file')
print(pagesCat[0])


otvetDog = requests.get(randDog)
json_response = json.loads(otvetDog.text)
pagesDog = jsonpath.jsonpath(json_response, 'url')
print(pagesDog[0])

otvetFox = requests.get(randFox)
json_response = json.loads(otvetFox.text)
pagesFox = jsonpath.jsonpath(json_response, 'image')
print(pagesFox[0])

#otvet.split("//")
#print(otvet.content)
#webbrowser.open('https://random.dog/1ae6411b-8f81-438a-a793-7642a3e61128.jpg')