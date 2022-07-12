// Copyright (c) 2022, Ajay and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Transaction', {
	// refresh: function(frm) {

	// }
	before_Save(frm){
		frm.trigger('outstanding_debt')
	},
	//validate outstanding_debt is less than 500 or not
	outstanding_debt(frm){
		if (frm.doc.outstanding_debt > 500){
			frappe.msgprint(__("Outstanding Debt is greater than 500"))
			frm.set_value('outstanding_debt','')
		}

	}
});
