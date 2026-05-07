import frappe
from frappe import _


def execute(filters=None):
    filters = filters or {}
    columns = [
        {"label": _("Channel"), "fieldname": "channel", "fieldtype": "Link", "options": "Channel", "width": 150},
        {"label": _("Bookings"), "fieldname": "bookings", "fieldtype": "Int", "width": 90},
        {"label": _("Revenue"), "fieldname": "revenue", "fieldtype": "Currency", "width": 130},
        {"label": _("Avg Stay (nights)"), "fieldname": "avg_nights", "fieldtype": "Float", "width": 130},
        {"label": _("Avg Rate"), "fieldname": "avg_rate", "fieldtype": "Currency", "width": 110},
    ]
    conditions = "WHERE docstatus = 1"
    if filters.get("from_date"):
        conditions += " AND check_in_date >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " AND check_in_date <= %(to_date)s"

    data = frappe.db.sql(f"""
        SELECT channel, COUNT(name) as bookings,
               SUM(total_amount) as revenue,
               AVG(nights) as avg_nights,
               AVG(rate_per_night) as avg_rate
        FROM `tabReservation`
        {conditions}
        GROUP BY channel
        ORDER BY revenue DESC
    """, filters, as_dict=True)
    return columns, data
