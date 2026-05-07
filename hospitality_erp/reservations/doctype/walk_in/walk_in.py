from frappe.model.document import Document
class WalkIn(Document):
    def validate(self):
        self.total_amount = (self.rate_per_night or 0) * (self.total_nights or 0)
