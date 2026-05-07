from frappe.model.document import Document
class FBOrder(Document):
    def validate(self):
        for row in (self.order_items or []):
            row.amount = (row.quantity or 1) * (row.rate or 0)
        self.subtotal = sum(r.amount or 0 for r in (self.order_items or []))
        self.total_amount = self.subtotal + (self.tax_amount or 0)
