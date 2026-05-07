from frappe.model.document import Document
class MenuItem(Document):
    def validate(self):
        if self.rate and self.cost and self.rate > 0:
            self.margin_pct = round(((self.rate - self.cost) / self.rate) * 100, 2)
