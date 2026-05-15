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
		{"fieldname": "status", "label": _("Status"), "fieldtype": "Data", "width": 90},
		{"fieldname": "rooms_revenue", "label": _("Rooms Revenue"), "fieldtype": "Currency", "width": 130},
		{"fieldname": "fnb_revenue", "label": _("F&B Revenue"), "fieldtype": "Currency", "width": 120},
		{"fieldname": "spa_revenue", "label": _("Spa Revenue"), "fieldtype": "Currency", "width": 110},
		{"fieldname": "events_revenue", "label": _("Events Revenue"), "fieldtype": "Currency", "width": 120},
		{"fieldname": "other_revenue", "label": _("Other Revenue"), "fieldtype": "Currency", "width": 110},
		{"fieldname": "total_revenue", "label": _("Total Revenue"), "fieldtype": "Currency", "width": 130},
		{"fieldname": "total_invoiced", "label": _("Total Invoiced"), "fieldtype": "Currency", "width": 130},
		{"fieldname": "total_collected", "label": _("Total Collected"), "fieldtype": "Currency", "width": 130},
		{"fieldname": "outstanding", "label": _("Outstanding"), "fieldtype": "Currency", "width": 120},
	]

def get_data(filters):
	conditions = ""
	if filters.get("property"):
		conditions += " AND property = %(property)s"
	if filters.get("audit_date"):
		conditions += " AND audit_date = %(audit_date)s"

	return frappe.db.sql(f"""
		SELECT
			property, audit_date, status,
			rooms_revenue, fnb_revenue, spa_revenue,
			events_revenue, other_revenue, total_revenue,
			total_invoiced, total_collected, outstanding
		FROM `tabNight Audit`
		WHERE docstatus < 2 {conditions}
		ORDER BY audit_date DESC
	""", filters, as_dict=True)
