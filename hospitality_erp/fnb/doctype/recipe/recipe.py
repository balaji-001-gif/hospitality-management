from frappe.model.document import Document
class Recipe(Document):
    def validate(self):
        for r in (self.ingredients or []):
            r.total_cost = (r.quantity or 0) * (r.cost_per_unit or 0)
        self.total_cost = sum(r.total_cost or 0 for r in (self.ingredients or []))
