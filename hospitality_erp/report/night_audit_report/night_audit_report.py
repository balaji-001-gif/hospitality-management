import frappe
from frappe import _


def execute(filters=None):
    filters = filters or {}
    columns = [
        {"label": _("Property"), "fieldname": "property", "fieldtype": "Link", "options": "Property", "width": 150},
        {"label": _("Date"), "fieldname": "audit_date", "fieldtype": "Date", "width": 110},
        {"label": _("Rooms Rev"), "fieldname": "rooms_revenue", "fieldtype": "Currency", "width": 120},
        {"label": _("F&B Rev"), "fieldname": "fnb_revenue", "fieldtype": "Currency", "width": 110},
        {"label": _("Spa Rev"), "fieldname": "spa_revenue", "fieldtype": "Currency", "width": 100},
        {"label": _("Total Rev"), "fieldname": "total_revenue", "fieldtype": "Currency", "width": 120},
        {"label": _("Collected"), "fieldname": "total_collected", "fieldtype": "Currency", "width": 110},
        {"label": _("Outstanding"), "fieldname": "outstanding", "fieldtype": "Currency", "width": 110},
        {"label": _("Status"), "fieldname": "status", "fieldtype": "Data", "width": 90},
    ]
    conditions = "WHERE 1=1"
    if filters.get("property"):
        conditions += " AND property = %(property)s"
    if filters.get("from_date"):
        conditions += " AND audit_date >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " AND audit_date <= %(to_date)s"

    data = frappe.db.sql(f"""
        SELECT property, audit_date, rooms_revenue, fnb_revenue, spa_revenue,
               total_revenue, total_collected, outstanding, status
        FROM `tabNight Audit`
        {conditions}
        ORDER BY audit_date DESC
    """, filters, as_dict=True)
    return columns, data
