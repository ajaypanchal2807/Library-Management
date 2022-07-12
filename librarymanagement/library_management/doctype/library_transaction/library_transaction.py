# Copyright (c) 2022, Ajay and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document,DocStatus

class LibraryTransaction(Document):
	def before_submit(self):
		# validate if book is Available/Issued
		if self.type == 'Issue':
			self.validateIssue()
			books = frappe.get_doc('Books',self.books)
			books.status = "Issued"
			books.save()
		
		elif self.type == 'Return':
		#validate-if book is not available/available
			self.validateReturn()
			books = frappe.get_doc('Books',self.books)
			books.status = 'Available'
			books.save()


	def validateIssue(self):
		#validate if book is Issued or not
		self.validateMembership()
		books = frappe.get_doc('Books',self.books)
		if books.status == 'Issued':
			frappe.throw('Book already issued by another member')

	def validateReturn(self):
		#validate if book is available or not
		books = frappe.get_doc('Books',self.books)
		if books.status == 'Available':
			frappe.throw('Book can not returned without being issued first')

	def validateMembership(self):
		#validate membership ,  if library membership is valid or not
		membership = frappe.db.exists("Library Membership",{
			"library_member":self.library_member,
			"docstatus": DocStatus.submitted(),
			"from_date": ("<", self.date),
			"to_date": (">", self.date),
		})

		if not membership:
			frappe.throw('The member does not have valid membership')