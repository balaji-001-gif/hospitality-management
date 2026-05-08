import frappe
from frappe.model.document import Document
from frappe.utils import add_months, add_days, getdate

class LeisureMembership(Document):
	def validate(self):
		if self.membership_plan:
			plan = frappe.get_doc("Membership Plan", self.membership_plan)
			self.total_amount = plan.amount
			
			if not self.end_date:
				self.calculate_end_date(plan.membership_type)

	def calculate_end_date(self, plan_type):
		start = getdate(self.start_date)
		if plan_type == "Annual":
			self.end_date = add_months(start, 12)
		elif plan_type == "Monthly":
			self.end_date = add_months(start, 1)
		elif plan_type == "Weekly":
			self.end_date = add_days(start, 7)
		elif plan_type == "Daily":
			self.end_date = add_days(start, 1)
