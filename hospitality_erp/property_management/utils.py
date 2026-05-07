import frappe


def get_available_rooms(property_name, check_in, check_out, room_type=None):
    filters = {"property": property_name, "status": "Vacant Clean"}
    if room_type:
        filters["room_type"] = room_type
    return frappe.db.get_all("Room", filters=filters, fields=["name", "room_number", "room_type", "status"])
