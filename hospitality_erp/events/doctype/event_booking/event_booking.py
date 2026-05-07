from frappe.model.document import Document
class EventBooking(Document):
    def validate(self):
        self.total_amount = (self.hall_charges or 0) + (self.catering_charges or 0)
        self.balance = self.total_amount - (self.advance_paid or 0)
