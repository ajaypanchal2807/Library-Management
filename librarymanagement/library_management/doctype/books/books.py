# Copyright (c) 2022, Ajay and contributors
# For license information, please see license.txt

import frappe
import requests
from frappe.model.document import Document

class Books(Document):
	pass

@frappe.whitelist()
def getBooks():
	# frappe-flask api
	api_url = "https://frappe.io/api/method/frappe-library" 
	# get response from api_url using request.get()
	response = requests.get(api_url)
	return (response.json())