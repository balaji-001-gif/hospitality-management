import frappe
from frappe import _

def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	return columns, data

def get_columns():
	return [
		{
			"label": _("Request ID"),
			"fieldname": "name",
			"fieldtype": "Link",
			"options": "Transport Request",
			"width": 120
		},
		{
			"label": _("Guest"),
			"fieldname": "guest",
			"fieldtype": "Link",
			"options": "Guest Profile",
			"width": 150
		},
		{
			"label": _("Transport Type"),
			"fieldname": "transport_type",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Date"),
			"fieldname": "request_date",
			"fieldtype": "Date",
			"width": 100
		},
		{
			"label": _("Time"),
			"fieldname": "request_time",
			"fieldtype": "Time",
			"width": 100
		},
		{
			"label": _("Flight Number"),
			"fieldname": "flight_number",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Vehicle Preference"),
			"fieldname": "vehicle_preference",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Status"),
			"fieldname": "status",
			"fieldtype": "Data",
			"width": 100
		}
	]

def get_data(filters):
	query_filters = {}
	if filters.get("request_date"):
		query_filters["request_date"] = filters.get("request_date")
	else:
		# Default to today
		query_filters["request_date"] = frappe.utils.today()
		
	data = frappe.get_all(
		"Transport Request",
		fields=["name", "guest", "transport_type", "request_date", "request_time", "flight_number", "vehicle_preference", "status"],
		filters=query_filters,
		order_by="request_time asc"
	)
	return data
