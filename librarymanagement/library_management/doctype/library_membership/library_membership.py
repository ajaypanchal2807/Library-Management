# Copyright (c) 2022, Ajay and contributors
# For license information, please see license.txt

import frappe
from frappe.model.docstatus import DocStatus
from frappe.model.document import Document

class LibraryMembership(Document):
	def before_save(self):
		# check if library membership for library member is exists or not
		exits = frappe.db.exists('Library Membership',
			{
				'library_member':self.library_member,
				'docstatus':DocStatus.submitted(),
				'to_date':('>=',self.from_date)
			}
		)
		# if library membership exists for library member
		if exits:
			frappe.throw("There is an active Library Membership for this user")
