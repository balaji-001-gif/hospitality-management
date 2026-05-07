from frappe.model.document import Document
class TipDistribution(Document):
    def validate(self):
        if self.staff_count and self.total_tips:
            self.per_staff_amount = self.total_tips / self.staff_count
