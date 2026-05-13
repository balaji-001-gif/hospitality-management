import frappe
from frappe import _

def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	return columns, data

def get_columns():
	return [
		{"fieldname": "room", "label": _("Room"), "fieldtype": "Link", "options": "Room", "width": 100},
		{"fieldname": "guest", "label": _("Guest"), "fieldtype": "Link", "options": "Guest Profile", "width": 150},
		{"fieldname": "check_in_date", "label": _("Check-in"), "fieldtype": "Date", "width": 100},
		{"fieldname": "check_out_date", "label": _("Check-out"), "fieldtype": "Date", "width": 100},
		{"fieldname": "adults", "label": _("Adults"), "fieldtype": "Int", "width": 80},
		{"fieldname": "children", "label": _("Children"), "fieldtype": "Int", "width": 80},
	]

def get_data(filters):
	property_filter = ""
	if filters.get("property"):
		property_filter = " AND property = %(property)s"

	return frappe.db.sql(f"""
		SELECT room, guest, check_in_date, check_out_date, adults, children
		FROM `tabReservation`
		WHERE status = 'Checked In' {property_filter}
	""", filters, as_dict=True)
