from frappe.model.document import Document
class NoShow(Document):
    def on_submit(self):
        if self.reservation:
            import frappe
            frappe.db.set_value("Reservation", self.reservation, "status", "No Show")
