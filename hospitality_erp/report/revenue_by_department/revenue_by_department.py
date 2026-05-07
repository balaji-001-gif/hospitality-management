import frappe
from frappe import _


def execute(filters=None):
    filters = filters or {}
    columns = [
        {"label": _("Property"), "fieldname": "property", "fieldtype": "Link", "options": "Property", "width": 160},
        {"label": _("Department"), "fieldname": "charge_type", "fieldtype": "Data", "width": 130},
        {"label": _("Revenue"), "fieldname": "revenue", "fieldtype": "Currency", "width": 130},
        {"label": _("Invoices"), "fieldname": "invoice_count", "fieldtype": "Int", "width": 90},
    ]
    conditions = "WHERE gi.docstatus = 1"
    if filters.get("property"):
        conditions += " AND gi.property = %(property)s"
    if filters.get("from_date"):
        conditions += " AND gi.invoice_date >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " AND gi.invoice_date <= %(to_date)s"

    data = frappe.db.sql(f"""
        SELECT gi.property, gii.charge_type,
               SUM(gii.amount) as revenue, COUNT(DISTINCT gi.name) as invoice_count
        FROM `tabGuest Invoice` gi
        JOIN `tabGuest Invoice Item` gii ON gii.parent = gi.name
        {conditions}
        GROUP BY gi.property, gii.charge_type
        ORDER BY revenue DESC
    """, filters, as_dict=True)
    return columns, data
