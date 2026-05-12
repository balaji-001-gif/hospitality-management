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
