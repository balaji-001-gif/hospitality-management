import frappe
from frappe.model.document import Document
from frappe.utils import today, getdate, flt

class NightAudit(Document):
    def validate(self):
        self.calculate_stats()

    def calculate_stats(self):
        # 1. Rooms Stats
        total_rooms = frappe.db.count("Room", {"property": self.property})
        occupied_rooms = frappe.db.count("Reservation", {
            "property": self.property,
            "status": "Checked In",
            "check_in_date": ["<=", self.audit_date],
            "check_out_date": [">", self.audit_date]
        })
        
        self.total_rooms_available = total_rooms
        self.total_rooms_occupied = occupied_rooms
        if total_rooms > 0:
            self.occupancy_rate = (occupied_rooms / total_rooms) * 100
            
        # 2. Revenue Stats (Simplified for demo)
        self.room_revenue = frappe.db.get_value("Reservation", {
            "property": self.property,
            "status": "Checked In"
        }, "sum(rate_per_night)") or 0
        
        self.fb_revenue = frappe.db.get_value("FnB Order", {
            "status": "Closed",
            "creation": ["like", f"{self.audit_date}%"]
        }, "sum(total_amount)") or 0
        
        self.total_revenue = flt(self.room_revenue) + flt(self.fb_revenue) + flt(self.other_revenue)

    def on_submit(self):
        self.post_nightly_charges()

    def post_nightly_charges(self):
        """Post nightly room rates to guest folios."""
        from hospitality_erp.finance.utils import post_charge_to_folio
        
        active_reservations = frappe.get_all("Reservation", filters={
            "property": self.property,
            "status": "Checked In"
        }, fields=["name", "guest", "rate_per_night"])
        
        for res in active_reservations:
            post_charge_to_folio(
                guest=res.guest,
                amount=res.rate_per_night,
                description=f"Room Charge - {self.audit_date}",
                charge_type="Room"
            )

def run_night_audit():
    """Daily task to run audit for all properties."""
    import frappe
    from frappe.utils import today
    
    properties = frappe.get_all("Property", filters={"status": "Active"})
    for prop in properties:
        if not frappe.db.exists("Night Audit", {"property": prop.name, "audit_date": today()}):
            audit = frappe.new_doc("Night Audit")
            audit.property = prop.name
            audit.audit_date = today()
            audit.insert(ignore_permissions=True)
            audit.submit()
