import frappe
from frappe import _

def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	return columns, data

def get_columns():
	return [
		{"fieldname": "property", "label": _("Property"), "fieldtype": "Link", "options": "Property", "width": 150},
		{"fieldname": "audit_date", "label": _("Audit Date"), "fieldtype": "Date", "width": 100},
		{"fieldname": "total_occupancy", "label": _("Occupancy %"), "fieldtype": "Percent", "width": 100},
		{"fieldname": "room_revenue", "label": _("Room Revenue"), "fieldtype": "Currency", "width": 120},
		{"fieldname": "fb_revenue", "label": _("F&B Revenue"), "fieldtype": "Currency", "width": 120},
		{"fieldname": "total_revenue", "label": _("Total Revenue"), "fieldtype": "Currency", "width": 120},
	]

def get_data(filters):
	conditions = ""
	if filters.get("property"):
		conditions += " AND property = %(property)s"
	if filters.get("audit_date"):
		conditions += " AND audit_date = %(audit_date)s"

	return frappe.db.sql(f"""
		SELECT property, audit_date, total_occupancy, room_revenue, fb_revenue, total_revenue
		FROM `tabNight Audit`
		WHERE docstatus < 2 {conditions}
		ORDER BY audit_date DESC
	""", filters, as_dict=True)
