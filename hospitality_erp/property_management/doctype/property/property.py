import frappe
from frappe.model.document import Document

class Property(Document):
    def validate(self):
        if self.total_rooms and self.total_rooms < 0:
            frappe.throw("Total Rooms cannot be negative")
