from frappe.model.document import Document
class OccupancyForecast(Document):
    def validate(self):
        if self.total_rooms:
            self.available = self.total_rooms - (self.occupied or 0)
            self.occupancy_pct = round(((self.occupied or 0) / self.total_rooms) * 100, 2)
        self.revpar = (self.occupancy_pct or 0) / 100 * (self.adr or 0)
