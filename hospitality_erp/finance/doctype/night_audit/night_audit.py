from frappe.model.document import Document
class NightAudit(Document):
    def validate(self):
        self.total_revenue = sum([
            self.rooms_revenue or 0, self.fnb_revenue or 0,
            self.spa_revenue or 0, self.events_revenue or 0, self.other_revenue or 0
        ])
        self.outstanding = (self.total_invoiced or 0) - (self.total_collected or 0)
