import frappe
from frappe import _


def execute(filters=None):
    filters = filters or {}
    columns = [
        {"label": _("Property"), "fieldname": "property", "fieldtype": "Link", "options": "Property", "width": 150},
        {"label": _("Type"), "fieldname": "event_type", "fieldtype": "Data", "width": 110},
        {"label": _("Date"), "fieldname": "event_date", "fieldtype": "Date", "width": 110},
        {"label": _("Guest"), "fieldname": "guest", "fieldtype": "Link", "options": "Guest Profile", "width": 150},
        {"label": _("Channel"), "fieldname": "channel", "fieldtype": "Link", "options": "Channel", "width": 120},
        {"label": _("Revenue Lost"), "fieldname": "total_amount", "fieldtype": "Currency", "width": 120},
        {"label": _("Penalty"), "fieldname": "penalty_amount", "fieldtype": "Currency", "width": 110},
    ]
    conditions = "WHERE r.status IN ('No Show', 'Cancelled')"
    if filters.get("property"):
        conditions += " AND r.property = %(property)s"
    if filters.get("from_date"):
        conditions += " AND r.check_in_date >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " AND r.check_in_date <= %(to_date)s"

    data = frappe.db.sql(f"""
        SELECT r.property, r.status as event_type, r.check_in_date as event_date,
               r.guest, r.channel, r.total_amount, 0 as penalty_amount
        FROM `tabReservation` r
        {conditions}
        ORDER BY r.check_in_date DESC
    """, filters, as_dict=True)
    return columns, data
