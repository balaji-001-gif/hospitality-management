import frappe
from frappe import _

def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	return columns, data

def get_columns():
	return [
		{
			"label": _("Visitor Name"),
			"fieldname": "visitor_name",
			"fieldtype": "Data",
			"width": 150
		},
		{
			"label": _("Phone"),
			"fieldname": "phone",
			"fieldtype": "Phone",
			"width": 120
		},
		{
			"label": _("Purpose"),
			"fieldname": "purpose",
			"fieldtype": "Small Text",
			"width": 200
		},
		{
			"label": _("Check In"),
			"fieldname": "check_in",
			"fieldtype": "Datetime",
			"width": 150
		},
		{
			"label": _("Check Out"),
			"fieldname": "check_out",
			"fieldtype": "Datetime",
			"width": 150
		},
		{
			"label": _("Property"),
			"fieldname": "property",
			"fieldtype": "Link",
			"options": "Property",
			"width": 120
		}
	]

def get_data(filters):
	query_filters = {}
	if filters.get("date"):
		query_filters["check_in"] = ["between", [filters.get("date") + " 00:00:00", filters.get("date") + " 23:59:59"]]
	else:
		query_filters["check_in"] = [">=", frappe.utils.today() + " 00:00:00"]
		
	data = frappe.get_all(
		"Visitor Log",
		fields=["visitor_name", "phone", "purpose", "check_in", "check_out", "property"],
		filters=query_filters,
		order_by="check_in asc"
	)
	return data
