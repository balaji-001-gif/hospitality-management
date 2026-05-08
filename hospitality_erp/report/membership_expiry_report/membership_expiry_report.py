import frappe
from frappe import _

def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	return columns, data

def get_columns():
	return [
		{
			"label": _("Membership ID"),
			"fieldname": "name",
			"fieldtype": "Link",
			"options": "Leisure Membership",
			"width": 150
		},
		{
			"label": _("Guest"),
			"fieldname": "guest",
			"fieldtype": "Link",
			"options": "Guest Profile",
			"width": 150
		},
		{
			"label": _("Membership Plan"),
			"fieldname": "membership_plan",
			"fieldtype": "Link",
			"options": "Membership Plan",
			"width": 150
		},
		{
			"label": _("Start Date"),
			"fieldname": "start_date",
			"fieldtype": "Date",
			"width": 100
		},
		{
			"label": _("End Date"),
			"fieldname": "end_date",
			"fieldtype": "Date",
			"width": 100
		},
		{
			"label": _("Status"),
			"fieldname": "status",
			"fieldtype": "Data",
			"width": 100
		},
		{
			"label": _("Amount"),
			"fieldname": "total_amount",
			"fieldtype": "Currency",
			"width": 100
		}
	]

def get_data(filters):
	data = frappe.get_all(
		"Leisure Membership",
		fields=["name", "guest", "membership_plan", "start_date", "end_date", "status", "total_amount"],
		filters={"status": "Active"},
		order_by="end_date asc"
	)
	return data
