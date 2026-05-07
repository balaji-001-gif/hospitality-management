import frappe
from frappe import _


def execute(filters=None):
    filters = filters or {}
    columns = [
        {"label": _("Property"), "fieldname": "property", "fieldtype": "Link", "options": "Property", "width": 150},
        {"label": _("Total Feedback"), "fieldname": "total", "fieldtype": "Int", "width": 110},
        {"label": _("Avg Overall"), "fieldname": "avg_overall", "fieldtype": "Float", "width": 110},
        {"label": _("Avg Room"), "fieldname": "avg_room", "fieldtype": "Float", "width": 100},
        {"label": _("Avg Service"), "fieldname": "avg_service", "fieldtype": "Float", "width": 110},
        {"label": _("Avg F&B"), "fieldname": "avg_fnb", "fieldtype": "Float", "width": 90},
        {"label": _("Would Recommend %"), "fieldname": "recommend_pct", "fieldtype": "Percent", "width": 140},
    ]
    conditions = "WHERE 1=1"
    if filters.get("property"):
        conditions += " AND property = %(property)s"
    if filters.get("from_date"):
        conditions += " AND feedback_date >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " AND feedback_date <= %(to_date)s"

    data = frappe.db.sql(f"""
        SELECT property,
               COUNT(name) as total,
               AVG(CAST(overall_rating AS UNSIGNED)) as avg_overall,
               AVG(CAST(room_rating AS UNSIGNED)) as avg_room,
               AVG(CAST(service_rating AS UNSIGNED)) as avg_service,
               AVG(CAST(fnb_rating AS UNSIGNED)) as avg_fnb,
               (SUM(would_recommend) / COUNT(name)) * 100 as recommend_pct
        FROM `tabGuest Feedback`
        {conditions}
        GROUP BY property
        ORDER BY avg_overall DESC
    """, filters, as_dict=True)
    return columns, data
