import frappe
from frappe.model.document import Document

class MaintenanceRequest(Document):
    def validate(self):
        if self.status == "Assigned" and not self.assigned_to:
            frappe.throw("Please assign to a technician")

def on_update(doc, method=None):
    if doc.status == "Assigned":
        frappe.publish_realtime(
            "maintenance_assigned",
            {"request": doc.name, "assigned_to": doc.assigned_to},
            user=frappe.session.user,
        )
