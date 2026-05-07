import frappe
from frappe import _


def execute(filters=None):
    filters = filters or {}
    columns = [
        {"label": _("Property"), "fieldname": "property", "fieldtype": "Link", "options": "Property", "width": 160},
        {"label": _("Room Type"), "fieldname": "room_type", "fieldtype": "Link", "options": "Room Type", "width": 140},
        {"label": _("Date"), "fieldname": "check_in_date", "fieldtype": "Date", "width": 110},
        {"label": _("Total Rooms"), "fieldname": "total_rooms", "fieldtype": "Int", "width": 100},
        {"label": _("Occupied"), "fieldname": "occupied", "fieldtype": "Int", "width": 90},
        {"label": _("Occupancy %"), "fieldname": "occupancy_pct", "fieldtype": "Percent", "width": 110},
    ]
    conditions = "WHERE r.docstatus = 1"
    if filters.get("property"):
        conditions += " AND r.property = %(property)s"
    if filters.get("from_date"):
        conditions += " AND r.check_in_date >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " AND r.check_in_date <= %(to_date)s"

    data = frappe.db.sql(f"""
        SELECT r.property, r.room_type, r.check_in_date,
               COUNT(r.name) as occupied,
               (SELECT COUNT(rm.name) FROM `tabRoom` rm WHERE rm.property = r.property AND rm.room_type = r.room_type) as total_rooms
        FROM `tabReservation` r
        {conditions}
        GROUP BY r.property, r.room_type, r.check_in_date
        ORDER BY r.check_in_date DESC
    """, filters, as_dict=True)

    for row in data:
        if row.total_rooms:
            row.occupancy_pct = round((row.occupied / row.total_rooms) * 100, 2)
    return columns, data
