from frappe.model.document import Document

class GuestInvoice(Document):
    def validate(self):
        for row in (self.invoice_items or []):
            row.amount = (row.quantity or 1) * (row.rate or 0)
            tax_rate = 0
            if row.tax_category:
                import frappe
                tax_rate = frappe.db.get_value("Tax Category", row.tax_category, "tax_rate") or 0
            row.tax_amount = row.amount * (tax_rate / 100)
        self.subtotal = sum(r.amount or 0 for r in (self.invoice_items or []))
        self.tax_total = sum(r.tax_amount or 0 for r in (self.invoice_items or []))
        self.total_amount = self.subtotal + self.tax_total
        self.balance = self.total_amount - (self.amount_paid or 0)

    def on_submit(self):
        self.db_set("status", "Submitted")
