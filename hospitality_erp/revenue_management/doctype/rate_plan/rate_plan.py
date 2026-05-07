from frappe.model.document import Document
class RatePlan(Document):
    def validate(self):
        self.net_rate = (self.base_rate or 0) * (1 - (self.discount_pct or 0) / 100)
