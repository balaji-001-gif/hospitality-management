import frappe
from frappe.utils import today, add_days, getdate
import random

def run():
	"""Main entry point for bench execute."""
	setup_demo_data()

def setup_demo_data():
	frappe.logger().info("Setting up Global Hospitality & Leisure Demo Data...")
	
	try:
		# 1. Base Masters (Hospitality Management)
		property_types = ["Hotel", "Resort", "Boutique Hotel", "Hostel", "Villa"]
		for pt in property_types:
			if not frappe.db.exists("Property Type", pt):
				frappe.get_doc({"doctype": "Property Type", "type_name": pt}).insert(ignore_permissions=True)

		room_categories = ["Standard", "Deluxe", "Superior", "Suite", "Villa"]
		for rc in room_categories:
			if not frappe.db.exists("Room Category", rc):
				frappe.get_doc({"doctype": "Room Category", "category_name": rc}).insert(ignore_permissions=True)

		# 2. Properties (10 entries)
		properties = []
		for i in range(1, 11):
			name = f"Elite Hospitality Resort {i}"
			if not frappe.db.exists("Property", {"property_name": name}):
				prop = frappe.get_doc({
					"doctype": "Property",
					"naming_series": "PROP-.YYYY.-",
					"property_name": name,
					"city": random.choice(["Dubai", "Singapore", "London", "New York", "Paris", "Tokyo"]),
					"country": "International",
					"status": "Active",
					"star_rating": "5 Star"
				}).insert(ignore_permissions=True)
				properties.append(prop.name)
			else:
				properties.append(frappe.db.get_value("Property", {"property_name": name}))

		# 3. Room Types & Rooms (10 per property)
		room_types_list = ["Single", "Double", "Twin", "King", "Penthouse"]
		for prop in properties:
			created_rt = []
			for rt_name in room_types_list:
				if not frappe.db.exists("Room Type", {"type_name": rt_name, "property": prop}):
					rt = frappe.get_doc({
						"doctype": "Room Type",
						"naming_series": "RT-.YYYY.-",
						"type_name": rt_name,
						"property": prop,
						"base_rate": random.randint(200, 1500),
						"max_occupancy": random.randint(1, 4)
					}).insert(ignore_permissions=True)
					created_rt.append(rt.name)
				else:
					created_rt.append(frappe.db.get_value("Room Type", {"type_name": rt_name, "property": prop}))
			
			for i in range(1, 11):
				room_no = f"{prop[:3].upper()}-{i:03d}"
				if not frappe.db.exists("Room", {"room_number": room_no}):
					frappe.get_doc({
						"doctype": "Room",
						"room_number": room_no,
						"property": prop,
						"room_type": random.choice(created_rt),
						"status": "Vacant Clean"
					}).insert(ignore_permissions=True)

		# 4. Guests (20 entries)
		guests = []
		for i in range(1, 21):
			name = f"Elite Guest {i}"
			if not frappe.db.exists("Guest Profile", {"full_name": name}):
				guest = frappe.get_doc({
					"doctype": "Guest Profile",
					"naming_series": "GUEST-.YYYY.-",
					"full_name": name,
					"email": f"guest{i}@hospitality.com",
					"status": "Active"
				}).insert(ignore_permissions=True)
				guests.append(guest.name)
			else:
				guests.append(frappe.db.get_value("Guest Profile", {"full_name": name}))

		# 5. F&B (10 Outlets, 10 Tables each)
		for i in range(1, 11):
			name = f"Premium Outlet {i}"
			if not frappe.db.exists("Outlet", {"outlet_name": name}):
				outlet = frappe.get_doc({
					"doctype": "Outlet",
					"outlet_name": name,
					"property": random.choice(properties)
				}).insert(ignore_permissions=True)
				
				for j in range(1, 11):
					table_no = f"TAB-{i}-{j:02d}"
					if not frappe.db.exists("Restaurant Table", {"table_number": table_no}):
						frappe.get_doc({
							"doctype": "Restaurant Table",
							"table_number": table_no,
							"outlet": outlet.name,
							"capacity": random.choice([2, 4, 6, 8]),
							"status": "Available"
						}).insert(ignore_permissions=True)

		# 6. Theme Parks (10 Attractions)
		for i in range(1, 11):
			name = f"Galaxy Adventure {i}"
			if not frappe.db.exists("Theme Park Attraction", {"attraction_name": name}):
				frappe.get_doc({
					"doctype": "Theme Park Attraction",
					"attraction_name": name,
					"type": random.choice(["Ride", "Show", "Exhibit"]),
					"status": "Open",
					"capacity": random.randint(800, 3000)
				}).insert(ignore_permissions=True)

		# 7. Cinema (10 Halls)
		for i in range(1, 11):
			name = f"IMAX Hall {i}"
			if not frappe.db.exists("Cinema Hall", {"hall_name": name}):
				frappe.get_doc({
					"doctype": "Cinema Hall",
					"hall_name": name,
					"property": random.choice(properties),
					"capacity": 200,
					"screen_type": "IMAX"
				}).insert(ignore_permissions=True)

		# 8. Marina (10 Berths)
		for i in range(1, 11):
			berth_id = f"BERTH-PRO-{i:03d}"
			if not frappe.db.exists("Berth", {"berth_id": berth_id}):
				frappe.get_doc({
					"doctype": "Berth",
					"berth_id": berth_id,
					"property": random.choice(properties),
					"length_limit": random.choice([40, 60, 100]),
					"status": "Available",
					"hourly_rate": random.randint(100, 500)
				}).insert(ignore_permissions=True)

		# 9. Cruise (20 Cabins)
		for i in range(1, 21):
			cabin_no = f"SUITE-{100 + i}"
			if not frappe.db.exists("Cruise Cabin", {"cabin_number": cabin_no}):
				frappe.get_doc({
					"doctype": "Cruise Cabin",
					"cabin_number": cabin_no,
					"vessel_name": "Ocean Monarch",
					"cabin_type": "Grand Suite",
					"deck_level": random.randint(5, 12),
					"status": "Available"
				}).insert(ignore_permissions=True)

		# 10. Sustainability (20 Sensors)
		for i in range(1, 21):
			sensor_id = f"SENSOR-IOT-{i:04d}"
			if not frappe.db.exists("IoT Sensor", {"sensor_id": sensor_id}):
				frappe.get_doc({
					"doctype": "IoT Sensor",
					"sensor_id": sensor_id,
					"sensor_type": random.choice(["Temperature", "Energy Meter", "Water Meter"]),
					"status": "Active"
				}).insert(ignore_permissions=True)

		# 11. Spa (10 Therapists)
		for i in range(1, 11):
			name = f"Expert Therapist {i}"
			if not frappe.db.exists("Therapist", {"therapist_name": name}):
				frappe.get_doc({
					"doctype": "Therapist",
					"naming_series": "THER-.YYYY.-",
					"therapist_name": name,
					"specialization": random.choice(["Massage", "Aromatherapy", "Skin Care"]),
					"status": "Available"
				}).insert(ignore_permissions=True)

		# 12. Security (10 Logs)
		for i in range(1, 11):
			try:
				frappe.get_doc({
					"doctype": "Visitor Log",
					"naming_series": "VIS-.YYYY.-",
					"visitor_name": f"Visitor {i}",
					"purpose": "Business Meeting",
					"status": "Checked In"
				}).insert(ignore_permissions=True)
			except:
				pass

		frappe.db.commit()
		print("Hyper-comprehensive global demo data setup completed successfully!")

	except Exception as e:
		frappe.db.rollback()
		frappe.log_error(frappe.get_traceback(), "Global Demo Data Setup Failed")
		print(f"Error setting up demo data: {str(e)}")

if __name__ == "__main__":
	run()
