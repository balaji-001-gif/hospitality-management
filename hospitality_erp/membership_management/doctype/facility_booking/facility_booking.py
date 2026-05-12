import frappe
from frappe.model.document import Document
from hospitality_erp.finance.utils import post_charge_to_folio

class FacilityBooking(Document):
	def on_update(self):
		if self.status == "Completed" and self.amount > 0:
			# Check if already billed
			if not frappe.db.exists("Guest Folio Item", {"reference_type": "Facility Booking", "reference_name": self.name}):
				post_charge_to_folio(
					guest=self.guest,
					amount=self.amount,
					description=f"Facility Usage: {self.facility}",
					charge_type="Other"
				)
