import frappe
from frappe.utils import today, add_days


def send_checkin_reminders():
    tomorrow = add_days(today(), 1)
    reservations = frappe.db.get_all(
        "Reservation",
        filters={"check_in_date": tomorrow, "status": "Confirmed"},
        fields=["name", "guest", "property", "check_in_date"],
    )
    for r in reservations:
        guest_email = frappe.db.get_value("Guest Profile", r.guest, "email")
        if guest_email:
            frappe.sendmail(
                recipients=[guest_email],
                subject=f"Check-In Reminder — {r.name}",
                message=f"Reminder: Your check-in at {r.property} is tomorrow ({r.check_in_date}).",
            )


def send_checkout_reminders():
    checkouts_today = frappe.db.get_all(
        "Reservation",
        filters={"check_out_date": today(), "status": "Checked In"},
        fields=["name", "guest", "property"],
    )
    for r in checkouts_today:
        guest_email = frappe.db.get_value("Guest Profile", r.guest, "email")
        if guest_email:
            frappe.sendmail(
                recipients=[guest_email],
                subject="Check-Out Reminder",
                message=f"Your check-out from {r.property} is due today. Please visit the front desk.",
            )
