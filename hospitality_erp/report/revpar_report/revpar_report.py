import frappe
from frappe import _


def execute(filters=None):
    filters = filters or {}
    columns = [
        {"label": _("Property"), "fieldname": "property", "fieldtype": "Link", "options": "Property", "width": 160},
        {"label": _("Date"), "fieldname": "check_in_date", "fieldtype": "Date", "width": 110},
        {"label": _("Revenue"), "fieldname": "total_revenue", "fieldtype": "Currency", "width": 130},
        {"label": _("Available Rooms"), "fieldname": "available_rooms", "fieldtype": "Int", "width": 120},
        {"label": _("ADR"), "fieldname": "adr", "fieldtype": "Currency", "width": 110},
        {"label": _("RevPAR"), "fieldname": "revpar", "fieldtype": "Currency", "width": 110},
    ]
    conditions = "WHERE r.docstatus = 1"
    if filters.get("property"):
        conditions += " AND r.property = %(property)s"
    if filters.get("from_date"):
        conditions += " AND r.check_in_date >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " AND r.check_in_date <= %(to_date)s"

    data = frappe.db.sql(f"""
        SELECT r.property, r.check_in_date,
               SUM(r.total_amount) as total_revenue, COUNT(r.name) as bookings,
               (SELECT COUNT(rm.name) FROM `tabRoom` rm WHERE rm.property = r.property) as available_rooms
        FROM `tabReservation` r
        {conditions}
        GROUP BY r.property, r.check_in_date
        ORDER BY r.check_in_date DESC
    """, filters, as_dict=True)

    for row in data:
        row.adr = (row.total_revenue / row.bookings) if row.bookings else 0
        row.revpar = (row.total_revenue / row.available_rooms) if row.available_rooms else 0
    return columns, data
