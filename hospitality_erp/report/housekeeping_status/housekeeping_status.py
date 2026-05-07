import frappe
from frappe import _


def execute(filters=None):
    filters = filters or {}
    columns = [
        {"label": _("Room"), "fieldname": "room_number", "fieldtype": "Link", "options": "Room", "width": 100},
        {"label": _("Property"), "fieldname": "property", "fieldtype": "Link", "options": "Property", "width": 150},
        {"label": _("Room Type"), "fieldname": "room_type", "fieldtype": "Link", "options": "Room Type", "width": 140},
        {"label": _("Floor"), "fieldname": "floor", "fieldtype": "Data", "width": 80},
        {"label": _("Status"), "fieldname": "status", "fieldtype": "Data", "width": 120},
        {"label": _("Current Guest"), "fieldname": "current_guest", "fieldtype": "Link", "options": "Guest Profile", "width": 150},
    ]
    conditions = "WHERE 1=1"
    if filters.get("property"):
        conditions += " AND property = %(property)s"
    if filters.get("status"):
        conditions += " AND status = %(status)s"

    data = frappe.db.sql(f"""
        SELECT room_number, property, room_type, floor, status, current_guest
        FROM `tabRoom`
        {conditions}
        ORDER BY floor, room_number
    """, filters, as_dict=True)
    return columns, data
