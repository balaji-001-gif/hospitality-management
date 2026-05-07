import frappe

def is_guest_blacklisted(guest):
    return frappe.db.exists("Blacklist Entry", {"guest": guest, "is_active": 1})
