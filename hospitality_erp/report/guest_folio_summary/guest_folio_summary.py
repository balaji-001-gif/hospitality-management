import frappe
from frappe import _


def execute(filters=None):
    filters = filters or {}
    columns = [
        {"label": _("Folio"), "fieldname": "name", "fieldtype": "Link", "options": "Guest Folio", "width": 150},
        {"label": _("Guest"), "fieldname": "guest", "fieldtype": "Link", "options": "Guest Profile", "width": 160},
        {"label": _("Property"), "fieldname": "property", "fieldtype": "Link", "options": "Property", "width": 140},
        {"label": _("Status"), "fieldname": "status", "fieldtype": "Data", "width": 90},
        {"label": _("Total Charges"), "fieldname": "total_charges", "fieldtype": "Currency", "width": 130},
        {"label": _("Total Paid"), "fieldname": "total_paid", "fieldtype": "Currency", "width": 110},
        {"label": _("Balance"), "fieldname": "balance", "fieldtype": "Currency", "width": 110},
    ]
    conditions = "WHERE 1=1"
    if filters.get("status"):
        conditions += " AND status = %(status)s"
    if filters.get("property"):
        conditions += " AND property = %(property)s"

    data = frappe.db.sql(f"""
        SELECT name, guest, property, status, total_charges, total_paid, balance
        FROM `tabGuest Folio`
        {conditions}
        ORDER BY modified DESC
    """, filters, as_dict=True)
    return columns, data
