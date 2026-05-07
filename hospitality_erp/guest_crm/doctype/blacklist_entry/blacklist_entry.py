from frappe.model.document import Document
class BlacklistEntry(Document):
    def on_submit(self):
        import frappe
        frappe.db.set_value("Guest Profile", self.guest, "status", "Blacklisted")
