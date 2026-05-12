import frappe
from frappe.utils import today, add_days, getdate
import random

def run():
	"""Main entry point for bench execute."""
	setup_demo_data()

def setup_demo_data():
	frappe.logger().info("Setting up Comprehensive Hospitality & Leisure Demo Data...")
	
	try:
		# 1. Properties (5 entries)
		properties = []
		property_names = ["Royal Palm Resort", "Ocean Breeze Hotel", "Mountain View Lodge", "City Center Suites", "Emerald Garden Resort"]
		cities = ["Dubai", "Miami", "Aspen", "New York", "Singapore"]
		
		for i, name in enumerate(property_names):
			if not frappe.db.exists("Property", {"property_name": name}):
				prop = frappe.get_doc({
					"doctype": "Property",
					"naming_series": "PROP-.YYYY.-",
					"property_name": name,
					"city": cities[i],
					"country": "International",
					"status": "Active",
					"star_rating": "5 Star" if i == 0 else "4 Star"
				}).insert(ignore_permissions=True)
				properties.append(prop.name)
			else:
				properties.append(frappe.db.get_value("Property", {"property_name": name}))

		# 2. Room Categories & Rooms (10 per property)
		categories = ["Standard", "Deluxe", "Superior", "Suite"]
		for cat in categories:
			if not frappe.db.exists("Room Category", cat):
				frappe.get_doc({"doctype": "Room Category", "category_name": cat}).insert(ignore_permissions=True)

		for prop in properties:
			for i in range(1, 11):
				room_no = f"{prop[:3].upper()}-{100 + i}"
				if not frappe.db.exists("Room", {"room_number": room_no}):
					frappe.get_doc({
						"doctype": "Room",
						"room_number": room_no,
						"property": prop,
						"room_category": random.choice(categories),
						"status": "Available"
					}).insert(ignore_permissions=True)

		# 3. Guests (10 entries)
		guests = []
		guest_names = ["John Doe", "Jane Smith", "Robert Brown", "Emily White", "Michael Green", "Sarah Blue", "David Black", "Linda Grey", "James Red", "Nancy Gold"]
		for name in guest_names:
			if not frappe.db.exists("Guest Profile", {"first_name": name.split()[0], "last_name": name.split()[1]}):
				guest = frappe.get_doc({
					"doctype": "Guest Profile",
					"naming_series": "GUEST-.YYYY.-",
					"first_name": name.split()[0],
					"last_name": name.split()[1],
					"email": f"{name.lower().replace(' ', '.')}@example.com",
					"status": "Active"
				}).insert(ignore_permissions=True)
				guests.append(guest.name)
			else:
				guests.append(frappe.db.get_value("Guest Profile", {"first_name": name.split()[0], "last_name": name.split()[1]}))

		# 4. F&B Outlets & Tables (5 outlets, 5 tables each)
		outlets = []
		outlet_names = ["Main Dining", "Sky Bar", "Poolside Grill", "Italian Bistro", "Sushi Corner"]
		for name in outlet_names:
			if not frappe.db.exists("Outlet", {"outlet_name": name}):
				outlet = frappe.get_doc({
					"doctype": "Outlet",
					"outlet_name": name,
					"property": random.choice(properties)
				}).insert(ignore_permissions=True)
				outlets.append(outlet.name)
			else:
				outlets.append(frappe.db.get_value("Outlet", {"outlet_name": name}))

		for outlet in outlets:
			for i in range(1, 6):
				table_no = f"{outlet[:3].upper()}-T{i}"
				if not frappe.db.exists("Restaurant Table", {"table_number": table_no}):
					frappe.get_doc({
						"doctype": "Restaurant Table",
						"table_number": table_no,
						"outlet": outlet,
						"capacity": random.choice([2, 4, 6]),
						"status": "Available"
					}).insert(ignore_permissions=True)

		# 5. Theme Park Attractions (5 entries)
		attractions = ["Dragon Coaster", "Splash Mountain", "Space Voyage", "Haunted Mansion", "Carousel of Dreams"]
		for name in attractions:
			if not frappe.db.exists("Theme Park Attraction", {"attraction_name": name}):
				frappe.get_doc({
					"doctype": "Theme Park Attraction",
					"attraction_name": name,
					"type": random.choice(["Ride", "Show", "Exhibit"]),
					"status": "Open",
					"capacity": random.randint(500, 2000),
					"minimum_height": 120.0
				}).insert(ignore_permissions=True)

		# 6. Cinema Halls & Shows (5 entries)
		for i in range(1, 6):
			hall_name = f"Cinema Hall {i}"
			if not frappe.db.exists("Cinema Hall", {"hall_name": hall_name}):
				frappe.get_doc({
					"doctype": "Cinema Hall",
					"hall_name": hall_name,
					"property": random.choice(properties),
					"capacity": 150,
					"screen_type": random.choice(["2D", "3D", "IMAX"])
				}).insert(ignore_permissions=True)

		# 7. Marina Berths (10 entries)
		for i in range(1, 11):
			berth_id = f"BERTH-{i:03d}"
			if not frappe.db.exists("Berth", {"berth_id": berth_id}):
				frappe.get_doc({
					"doctype": "Berth",
					"berth_id": berth_id,
					"property": random.choice(properties),
					"length_limit": random.choice([30, 50, 80]),
					"status": "Available",
					"hourly_rate": random.randint(50, 200)
				}).insert(ignore_permissions=True)

		# 8. Cruise Cabins (10 entries)
		for i in range(1, 11):
			cabin_no = f"CABIN-{1000 + i}"
			if not frappe.db.exists("Cruise Cabin", {"cabin_number": cabin_no}):
				frappe.get_doc({
					"doctype": "Cruise Cabin",
					"cabin_number": cabin_no,
					"vessel_name": "Sea Majesty",
					"cabin_type": random.choice(["Interior", "Ocean View", "Balcony", "Suite"]),
					"deck_level": random.randint(1, 10),
					"status": "Available"
				}).insert(ignore_permissions=True)

		# 9. IoT Sensors (10 entries)
		sensor_types = ["Temperature", "Humidity", "Occupancy", "Energy Meter"]
		for i in range(1, 11):
			sensor_id = f"SENSOR-{i:04d}"
			if not frappe.db.exists("IoT Sensor", {"sensor_id": sensor_id}):
				frappe.get_doc({
					"doctype": "IoT Sensor",
					"sensor_id": sensor_id,
					"sensor_type": random.choice(sensor_types),
					"status": "Active"
				}).insert(ignore_permissions=True)

		# 10. Spa & Recreation (5 Therapists)
		therapist_names = ["Alice", "Bob", "Charlie", "Diana", "Edward"]
		for name in therapist_names:
			if not frappe.db.exists("Therapist", {"therapist_name": name}):
				frappe.get_doc({
					"doctype": "Therapist",
					"naming_series": "THER-.YYYY.-",
					"therapist_name": name,
					"specialization": random.choice(["Massage", "Facial", "Yoga"]),
					"status": "Available"
				}).insert(ignore_permissions=True)

		frappe.db.commit()
		print("Comprehensive demo data setup completed successfully!")

	except Exception as e:
		frappe.db.rollback()
		frappe.log_error(frappe.get_traceback(), "Demo Data Setup Failed")
		print(f"Error setting up demo data: {str(e)}")

if __name__ == "__main__":
	run()
