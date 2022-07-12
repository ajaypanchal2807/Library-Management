// Copyright (c) 2022, Ajay and contributors
// For license information, please see license.txt

frappe.ui.form.on('Import Books', {
	import_books:function(frm){
		//frappe.call for frappe-api's response and add books
		frappe.call({
			method:"librarymanagement.library_management.doctype.books.books.getBooks",
			callback:function(r){
				for(let i = 0 ; i < frm.doc.enter_number_to_import_books ; i++){
					frappe.call({
						method : 'frappe.client.insert',
						args : {
							doc : {
							doctype : "Books",
							bookid : r.message.message[i]["bookID"] ,
							title : r.message.message[i]["title"],
							authors : r.message.message[i]["authors"],
							isbn : r.message.message[i]["isbn"] , 
							publisher : r.message.message[i]["publisher"],
							status : "Available",
							pages : r.message.message[i]["  num_pages"]
							}
						},
						callback:function(r){
						}
					})
					frappe.msgprint(__(r.message.message[i]["title"] + " Imported Successfully"))
				}
			}
		})
	}
});
