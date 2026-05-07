from frappe.model.document import Document
class RevenueBudget(Document):
    def validate(self):
        self.total_budget = sum([
            self.rooms_budget or 0, self.fnb_budget or 0,
            self.spa_budget or 0, self.events_budget or 0, self.other_budget or 0
        ])
        self.variance = self.total_budget - (self.actual_revenue or 0)
