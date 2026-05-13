import frappe
from frappe import _
from frappe.utils import flt

def make_gl_entries(doc, debit_account, credit_account, amount, posting_date=None):
	"""Creates General Ledger entries for a transaction."""
	if not amount:
		return

	company = get_company(doc)
	if not company:
		frappe.msgprint(_("Please set Company in Property {0} to enable accounting entries").format(doc.property))
		return

	posting_date = posting_date or doc.get("posting_date") or doc.get("creation")

	# Debit Entry
	frappe.get_doc({
		"doctype": "GL Entry",
		"posting_date": posting_date,
		"account": debit_account,
		"debit": flt(amount),
		"credit": 0,
		"company": company,
		"voucher_type": doc.doctype,
		"voucher_no": doc.name,
		"remarks": _("Hospitality Transaction: {0}").format(doc.name)
	}).insert(ignore_permissions=True)

	# Credit Entry
	frappe.get_doc({
		"doctype": "GL Entry",
		"posting_date": posting_date,
		"account": credit_account,
		"debit": 0,
		"credit": flt(amount),
		"company": company,
		"voucher_type": doc.doctype,
		"voucher_no": doc.name,
		"remarks": _("Hospitality Transaction: {0}").format(doc.name)
	}).insert(ignore_permissions=True)

def get_company(doc):
	if hasattr(doc, "company") and doc.company:
		return doc.company
	if hasattr(doc, "property") and doc.property:
		return frappe.db.get_value("Property", doc.property, "company")
	return None

def flag_overdue_invoices():
	"""Daily job to flag invoices that are past their due date."""
	import frappe
	from frappe.utils import today
	
	overdue_invoices = frappe.get_all("Guest Invoice", filters={
		"status": ["in", ["Submitted", "Partially Paid"]],
		"due_date": ["<", today()]
	})
	
	for inv in overdue_invoices:
		frappe.db.set_value("Guest Invoice", inv.name, "status", "Overdue")

def post_charge_to_folio(guest, amount, description, charge_type="Other"):
	"""Helper to post a charge to an active guest folio."""
	import frappe
	from frappe.utils import today
	
	# Find active folio for guest
	folio = frappe.db.get_value("Guest Folio", {"guest": guest, "status": "Open"}, "name")
	
	if not folio:
		# Optionally create one or log
		frappe.msgprint(f"No active folio found for guest {guest}. Charge {amount} for {description} was not posted.")
		return
	
	folio_doc = frappe.get_doc("Guest Folio", folio)
	folio_doc.append("charges", {
		"posting_date": today(),
		"description": description,
		"charge_type": charge_type,
		"quantity": 1,
		"rate": amount,
		"amount": amount
	})
	folio_doc.save(ignore_permissions=True)
