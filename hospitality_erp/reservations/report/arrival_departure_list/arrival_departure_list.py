import frappe
from frappe import _

def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	return columns, data

def get_columns():
	return [
		{"fieldname": "type", "label": _("Type"), "fieldtype": "Data", "width": 100},
		{"fieldname": "guest", "label": _("Guest"), "fieldtype": "Link", "options": "Guest Profile", "width": 150},
		{"fieldname": "room", "label": _("Room"), "fieldtype": "Link", "options": "Room", "width": 100},
		{"fieldname": "check_in_date", "label": _("Check-in"), "fieldtype": "Date", "width": 100},
		{"fieldname": "check_out_date", "label": _("Check-out"), "fieldtype": "Date", "width": 100},
		{"fieldname": "status", "label": _("Status"), "fieldtype": "Data", "width": 100},
	]

def get_data(filters):
	date = filters.get("date")
	property_filter = ""
	if filters.get("property"):
		property_filter = " AND property = %(property)s"

	arrivals = frappe.db.sql(f"""
		SELECT 'Arrival' as type, guest, room, check_in_date, check_out_date, status
		FROM `tabReservation`
		WHERE check_in_date = %(date)s {property_filter}
	""", {"date": date, "property": filters.get("property")}, as_dict=True)

	departures = frappe.db.sql(f"""
		SELECT 'Departure' as type, guest, room, check_in_date, check_out_date, status
		FROM `tabReservation`
		WHERE check_out_date = %(date)s {property_filter}
	""", {"date": date, "property": filters.get("property")}, as_dict=True)

	return arrivals + departures
