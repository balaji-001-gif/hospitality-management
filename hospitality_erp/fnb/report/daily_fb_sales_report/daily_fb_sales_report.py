import frappe
from frappe import _

def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	return columns, data

def get_columns():
	return [
		{"fieldname": "name", "label": _("Order ID"), "fieldtype": "Link", "options": "FnB Order", "width": 120},
		{"fieldname": "outlet", "label": _("Outlet"), "fieldtype": "Link", "options": "Outlet", "width": 150},
		{"fieldname": "total_amount", "label": _("Amount"), "fieldtype": "Currency", "width": 100},
		{"fieldname": "status", "label": _("Status"), "fieldtype": "Data", "width": 100},
		{"fieldname": "creation", "label": _("Time"), "fieldtype": "Datetime", "width": 150},
	]

def get_data(filters):
	conditions = ""
	if filters.get("outlet"):
		conditions += " AND outlet = %(outlet)s"
	if filters.get("posting_date"):
		conditions += " AND DATE(creation) = %(posting_date)s"
	
	return frappe.db.sql(f"""
		SELECT 
			name,
			outlet,
			total_amount,
			status,
			creation
		FROM `tabFnB Order`
		WHERE docstatus < 2 {conditions}
		ORDER BY creation DESC
	""", filters, as_dict=True)
