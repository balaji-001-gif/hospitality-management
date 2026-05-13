import frappe
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
        from hospitality_erp.finance.utils import make_gl_entries
        
        # Determine accounts (Usually configurable, using defaults for demo)
        company = frappe.db.get_value("Property", self.property, "company")
        receivable_account = frappe.db.get_value("Company", company, "default_receivable_account") or f"Debtors - {company}"
        income_account = frappe.db.get_value("Company", company, "default_income_account") or f"Sales - {company}"
        
        make_gl_entries(self, receivable_account, income_account, self.total_amount)
        self.db_set("status", "Paid" if self.balance <= 0 else "Submitted")
