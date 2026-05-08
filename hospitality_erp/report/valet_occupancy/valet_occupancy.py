import frappe
from frappe import _

def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	return columns, data

def get_columns():
	return [
		{
			"label": _("Vehicle Number"),
			"fieldname": "vehicle_number",
			"fieldtype": "Data",
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
			"label": _("Parking Slot"),
			"fieldname": "parking_slot",
			"fieldtype": "Data",
			"width": 100
		},
		{
			"label": _("Key Tag"),
			"fieldname": "key_tag",
			"fieldtype": "Data",
			"width": 100
		},
		{
			"label": _("Check In"),
			"fieldname": "check_in",
			"fieldtype": "Datetime",
			"width": 150
		}
	]

def get_data(filters):
	data = frappe.get_all(
		"Valet Log",
		fields=["vehicle_number", "guest", "parking_slot", "key_tag", "check_in"],
		filters={"status": "Parked"},
		order_by="check_in asc"
	)
	return data
