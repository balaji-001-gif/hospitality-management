import frappe
from frappe import _
from frappe.utils import getdate, date_diff

def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	return columns, data

def get_columns():
	return [
		{"fieldname": "room", "label": _("Room"), "fieldtype": "Link", "options": "Room", "width": 80},
		{"fieldname": "room_type", "label": _("Room Type"), "fieldtype": "Link", "options": "Room Type", "width": 120},
		{"fieldname": "guest", "label": _("Guest"), "fieldtype": "Link", "options": "Guest Profile", "width": 150},
		{"fieldname": "check_in_date", "label": _("Check-in"), "fieldtype": "Date", "width": 100},
		{"fieldname": "check_out_date", "label": _("Check-out"), "fieldtype": "Date", "width": 100},
		{"fieldname": "nights", "label": _("Nights"), "fieldtype": "Int", "width": 60},
		{"fieldname": "rate_per_night", "label": _("Rate"), "fieldtype": "Currency", "width": 100},
		{"fieldname": "total_amount", "label": _("Total Revenue"), "fieldtype": "Currency", "width": 120},
		{"fieldname": "status", "label": _("Status"), "fieldtype": "Data", "width": 100},
	]

def get_data(filters):
	conditions = ""
	if filters.get("property"):
		conditions += " AND property = %(property)s"
	if filters.get("from_date"):
		conditions += " AND check_in_date >= %(from_date)s"
	if filters.get("to_date"):
		conditions += " AND check_in_date <= %(to_date)s"
	
	return frappe.db.sql(f"""
		SELECT 
			room,
			room_type,
			guest,
			check_in_date,
			check_out_date,
			nights,
			rate_per_night,
			total_amount,
			status
		FROM `tabReservation`
		WHERE status IN ('Confirmed', 'Checked In', 'Checked Out') {conditions}
		ORDER BY check_in_date DESC
	""", filters, as_dict=True)
