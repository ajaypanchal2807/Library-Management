frappe.listview_settings['Books'] = {
    onload(listview) {
        listview.page.set_secondary_action('Insert Books', () => {
          //set route for 'Import Books'
             frappe.set_route('Form', 'Import Books')
        });
  }
}