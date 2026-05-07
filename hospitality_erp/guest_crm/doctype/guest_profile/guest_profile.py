import frappe
from frappe import _
from frappe.model.document import Document

class GuestProfile(Document):
    def validate(self):
        if self.email and not frappe.utils.validate_email_address(self.email):
            frappe.throw(_("Invalid Email: {0}").format(self.email))
