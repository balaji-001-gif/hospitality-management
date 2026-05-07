import frappe
from frappe.utils import now
from frappe.model.document import Document
class HousekeepingTask(Document):
    def validate(self):
        if self.status == "Completed" and not self.completed_at:
            self.completed_at = now()
        if self.status == "Completed":
            frappe.db.set_value("Room", self.room, "status", "Vacant Clean")
