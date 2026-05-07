from frappe.model.document import Document

class GuestFolio(Document):
    def validate(self):
        self.total_charges = sum((row.amount or 0) for row in (self.charges or []))
        self.balance = self.total_charges - (self.total_paid or 0)
