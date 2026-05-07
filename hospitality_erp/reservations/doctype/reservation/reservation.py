import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import date_diff, getdate


class Reservation(Document):
    def validate(self):
        self.validate_dates()
        self.calculate_amounts()

    def on_submit(self):
        self.db_set("status", "Confirmed")

    def on_cancel(self):
        self.db_set("status", "Cancelled")
        if self.room:
            frappe.db.set_value("Room", self.room, "status", "Vacant Dirty")

    def validate_dates(self):
        if self.check_in_date and self.check_out_date:
            if getdate(self.check_out_date) <= getdate(self.check_in_date):
                frappe.throw(_("Check-Out must be after Check-In"))
            self.nights = date_diff(self.check_out_date, self.check_in_date)

    def calculate_amounts(self):
        self.total_amount = (self.rate_per_night or 0) * (self.nights or 0)
        self.balance_due = self.total_amount - (self.advance_paid or 0)


def after_insert(doc, method=None):
    frappe.sendmail(
        recipients=[doc.email] if hasattr(doc, "email") and doc.email else [],
        subject=f"Reservation Confirmed — {doc.name}",
        message=f"Your reservation at {doc.property} is confirmed. Check-in: {doc.check_in_date}",
    )


def on_submit(doc, method=None):
    pass
