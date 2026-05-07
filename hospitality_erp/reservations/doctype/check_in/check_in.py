import frappe
from frappe.model.document import Document

class CheckIn(Document):
    def on_submit(self):
        frappe.db.set_value("Room", self.room, "status", "Occupied")
        frappe.db.set_value("Room", self.room, "current_guest", self.guest)
        if self.reservation:
            frappe.db.set_value("Reservation", self.reservation, "status", "Checked In")
