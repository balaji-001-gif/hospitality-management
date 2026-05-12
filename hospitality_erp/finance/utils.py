import frappe

def post_charge_to_folio(guest, amount, description, charge_type="Other"):
	# Find active folio for guest
	folio = frappe.db.get_value("Guest Folio", {"guest": guest, "status": "Open"}, "name")
	
	if not folio:
		return
		
	folio_doc = frappe.get_doc("Guest Folio", folio)
	folio_doc.append("charges", {
		"description": description,
		"charge_type": charge_type,
		"quantity": 1,
		"rate": amount,
		"amount": amount,
		"posting_date": frappe.utils.today()
	})
	folio_doc.save()
	frappe.db.commit()

def flag_overdue_invoices():
	"""Finds unpaid Sales Invoices that are past their due date and flags them."""
	overdue_invoices = frappe.get_all(
		"Sales Invoice",
		filters={
			"docstatus": 1,
			"status": ["!=", "Paid"],
			"due_date": ["<", frappe.utils.today()]
		},
		fields=["name", "customer", "due_date"]
	)
	
	for inv in overdue_invoices:
		# Logic to flag or notify
		# In a real system, you might change the status or send a reminder
		frappe.log_error(f"Invoice {inv.name} is overdue since {inv.due_date}", "Billing Alert")
