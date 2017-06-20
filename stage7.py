#!/usr/bin/env python
#Learn how this works here: http://youtu.be/pxofwuWTs7c

import urllib2
import json
import requests
import pandas as pd

locu_api = '9fb8cd70cb34cab8e83690473133f51943b5c93f'
key = "AIzaSyBOyKv0q4n3hXQCskLHsw0Pgj6RbonPGHU"
cx = "009251156210194212584:vubvrihoo_m"
url = "https://www.googleapis.com/customsearch/v1"


def locu_search(query):
    api_key = locu_api
    url = 'https://api.locu.com/v1_0/venue/search/?api_key=' + api_key
    locality = query.replace(' ', '%20')
    final_url = url + "&locality=" + locality + "&category=restaurant"
    json_obj = urllib2.urlopen(final_url)
    data = json.load(json_obj)
    for item in data['objects']:
        print item['name']
        print item['phone']
        print item['locality']
        print item['street_address']
        postal= item['postal_code']
        print postal
        print item['website_url']
        print ''
    return postal

def zip_code1(query):
        api_key='d0f10746d9149ac6c50bda24cab178a6'
        url='http://api.openweathermap.org/data/2.5/weather?'
        zip1=query.replace(' ','%20')
        final_url=url+"zip="+zip1 +",us&appid="+api_key
        json_obj=urllib2.urlopen(final_url)
        data=json.load(json_obj)
        temp= data['main']
        temperature= temp['temp']
        temp_in_cel=temperature - 273.15
        print "current temparature is", temp_in_cel
        for item in data['weather']:
                print "description", item['description']

def parameter_input():
	search_results=raw_input("search >")
	parameters = {'q':search_results,
	              "cx": cx,
	              "key": key,
	              }
	page = requests.request("GET",url,params=parameters)
	results = json.loads(page.text)
	results.keys()
	return results
	
def process_search(results):
    link_list = [item["link"] for item in results["items"]]
    df = pd.DataFrame(link_list, columns=["link"])
    df["title"] = [item["title"] for item in results["items"]]
    df["snippet"] = [item["snippet"] for item in results["items"]]
    for num in range(0,4):
        print df['title'][num]
        print df['snippet'][num]
        print df['link'][num]
        print ""
    return df



#zip_code1(postal_code)

def start():
	print "hey whatsapp"
	print "how are u feeling today"
	answer=raw_input("")
	if answer == "good" or answer == "great" or answer =="awesom":
		print "thats great"
		print "do you need any help?"
		answer2=raw_input("")
		if answer2 == "yes":
			print"let me help u"
			results=parameter_input()
			process_search(results)
		else:
			print "let me know if you want somthing"
	elif answer == "not that great":
		print "get some fresh air"
		print "eat somthing healthy"
		print "it just takes one more step"
		city_name = raw_input('Provide the city name>')
		postal_code= locu_search(city_name)
		zip_code1(postal_code)
	else:
		print ""
while(1):
	start()

