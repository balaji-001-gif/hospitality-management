import frappe
from frappe.model.document import Document
from hospitality_erp.finance.utils import post_charge_to_folio

class AttractionTicket(Document):
	def on_submit(self):
		if self.amount > 0:
			post_charge_to_folio(
				guest=self.guest,
				amount=self.amount,
				description=f"Theme Park Ticket: {self.ticket_type} for {self.date}"
			)
			frappe.msgprint(f"Charge of {self.amount} posted to Guest Folio.")
