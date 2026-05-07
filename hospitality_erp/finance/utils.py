import frappe
from frappe.utils import today


def flag_overdue_invoices():
    overdue = frappe.db.get_all(
        "Guest Invoice",
        filters={"status": "Submitted", "due_date": ["<", today()]},
        fields=["name", "guest", "total_amount", "balance"],
    )
    for inv in overdue:
        frappe.db.set_value("Guest Invoice", inv.name, "status", "Overdue")
    frappe.db.commit()
