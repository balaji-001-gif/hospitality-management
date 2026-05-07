import frappe
from frappe.model.document import Document

class Room(Document):
    def validate(self):
        pass

def on_update(doc, method=None):
    if doc.status == "Vacant Clean":
        frappe.publish_realtime(
            "room_ready",
            {"room": doc.room_number, "property": doc.property},
            user=frappe.session.user,
        )
