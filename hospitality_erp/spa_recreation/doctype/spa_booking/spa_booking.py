import frappe
from frappe.model.document import Document
class SpaBooking(Document):
    def validate(self):
        if self.spa_service and not self.amount:
            self.amount = frappe.db.get_value("Spa Service", self.spa_service, "price")
