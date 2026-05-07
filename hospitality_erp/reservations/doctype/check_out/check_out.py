import frappe
from frappe.model.document import Document

class CheckOut(Document):
    def on_submit(self):
        frappe.db.set_value("Room", self.room, "status", "Vacant Dirty")
        frappe.db.set_value("Room", self.room, "current_guest", None)
        frappe.db.set_value("Room", self.room, "current_reservation", None)
        if self.reservation:
            frappe.db.set_value("Reservation", self.reservation, "status", "Checked Out")
