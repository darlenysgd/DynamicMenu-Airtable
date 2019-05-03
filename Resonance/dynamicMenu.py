#! python
import requests
import json
from airtable import Airtable
from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

TABLE_NAME = 'Config'
BASE_ID = 'appdqzfZoeTcXC7VD'
AIRTABLE_API_KEY = 'key4hLp2X6ERPO1Am'
menu = {}

@app.route("/menu")
def returnMenu():
	menu.clear()
	load()
	return json.dumps(menu)
@app.route("/test")
def test():
	menu.clear()
	load()
	return render_template("test.html", menu = menu)
@app.route("/")
def home():
	menu.clear()
	load()
	return render_template("menu.html", menu = menu)
def load():
	airtable = Airtable(BASE_ID, TABLE_NAME, AIRTABLE_API_KEY)
	result = airtable.get_all(sort='MainMenu')
	for item in result:
		if 'MainMenu' in item['fields'] and(item['fields']['MainMenu'] not in menu.keys()):
			menu[item['fields']['MainMenu']] = {'Submenu': [], 'action': []}
	for item in result:
		if 'Live' in item['fields'].keys() and item['fields']['Live']==True:

			if'Actions' in item['fields'].keys() and ('Sub-menu') in item['fields'].keys():
				
				if item['fields']['Sub-menu'] not in menu[item['fields']['MainMenu']]['Submenu']:
			   		menu[item['fields']['MainMenu']]['Submenu'].append(item['fields']['Sub-menu'])

				if menu[item['fields']['MainMenu']]['action'] not in menu[item['fields']['MainMenu']]['action']:
					menu[item['fields']['MainMenu']]['action'].append({'Submenu': item['fields']['Sub-menu'], 'name': item['fields']['Actions'], 'url':item['fields']['URL']})

			if 'Actions' in item['fields'].keys() and ('Sub-menu') not in item['fields'].keys():
				menu[item['fields']['MainMenu']]['Submenu'].append(item['fields']['Actions'])
				menu[item['fields']['MainMenu']]['action'].append({'Submenu': item['fields']['Actions'], 'name': item['fields']['Actions'], 'url':item['fields']['URL']})

			if 'URL' in item['fields'].keys() and 'Actions' not in item['fields'].keys():
				menu[item['fields']['MainMenu']]['Submenu'].append(item['fields']['Sub-menu'])
				menu[item['fields']['MainMenu']]['action'].append({'Submenu': item['fields']['Sub-menu'], 'name': item['fields']['Sub-menu'], 'url':item['fields']['URL']})

if __name__=="__main__":
	app.run(debug=True)