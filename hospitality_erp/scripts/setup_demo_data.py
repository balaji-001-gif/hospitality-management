import frappe
from frappe.utils import today, add_days, getdate
import random

def run():
	"""Main entry point for bench execute."""
	setup_demo_data()

def setup_demo_data():
	frappe.logger().info("Setting up Global Hospitality & Leisure Demo Data...")
	
	try:
		# 1. Properties
		properties = []
		for i in range(1, 6):
			name = f"Grand Plaza Resort {i}"
			if not frappe.db.exists("Property", {"property_name": name}):
				prop = frappe.get_doc({
					"doctype": "Property",
					"naming_series": "PROP-.YYYY.-",
					"property_name": name,
					"city": random.choice(["Dubai", "Singapore", "London", "New York"]),
					"country": "International",
					"status": "Active"
				}).insert(ignore_permissions=True)
				properties.append(prop.name)
			else:
				properties.append(frappe.db.get_value("Property", {"property_name": name}))

		# 2. Room Types & Rooms
		room_types = ["Single", "Double", "Twin", "King", "Suite"]
		for prop in properties:
			for rt_name in room_types:
				if not frappe.db.exists("Room Type", {"type_name": rt_name, "property": prop}):
					rt = frappe.get_doc({
						"doctype": "Room Type",
						"naming_series": "RT-.YYYY.-",
						"type_name": rt_name,
						"property": prop,
						"base_rate": random.randint(150, 800),
						"max_occupancy": 2 if "Single" not in rt_name else 1
					}).insert(ignore_permissions=True)
					
					# Create 5 rooms for each type per property
					for j in range(1, 6):
						room_no = f"{prop[:3].upper()}-{rt_name[:1]}-{j:02d}"
						if not frappe.db.exists("Room", {"room_number": room_no}):
							frappe.get_doc({
								"doctype": "Room",
								"room_number": room_no,
								"property": prop,
								"room_type": rt.name,
								"status": "Vacant Clean"
							}).insert(ignore_permissions=True)

		# 3. Guests (10 entries)
		guests = []
		for i in range(1, 11):
			name = f"Guest {i}"
			if not frappe.db.exists("Guest Profile", {"full_name": name}):
				guest = frappe.get_doc({
					"doctype": "Guest Profile",
					"naming_series": "GUEST-.YYYY.-",
					"full_name": name,
					"email": f"guest{i}@example.com",
					"status": "Active"
				}).insert(ignore_permissions=True)
				guests.append(guest.name)
			else:
				guests.append(frappe.db.get_value("Guest Profile", {"full_name": name}))

		# 4. F&B (Outlets & Tables)
		for i in range(1, 6):
			name = f"Restaurant {i}"
			if not frappe.db.exists("Outlet", {"outlet_name": name}):
				outlet = frappe.get_doc({
					"doctype": "Outlet",
					"outlet_name": name,
					"property": random.choice(properties)
				}).insert(ignore_permissions=True)
				
				for j in range(1, 6):
					table_no = f"T-{i}-{j}"
					if not frappe.db.exists("Restaurant Table", {"table_number": table_no}):
						frappe.get_doc({
							"doctype": "Restaurant Table",
							"table_number": table_no,
							"outlet": outlet.name,
							"capacity": 4,
							"status": "Available"
						}).insert(ignore_permissions=True)

		# 5. Theme Park & Attractions
		for i in range(1, 6):
			name = f"Thrill Ride {i}"
			if not frappe.db.exists("Theme Park Attraction", {"attraction_name": name}):
				frappe.get_doc({
					"doctype": "Theme Park Attraction",
					"attraction_name": name,
					"type": "Ride",
					"status": "Open",
					"capacity": 1000
				}).insert(ignore_permissions=True)

		# 6. Marina & Berths
		for i in range(1, 6):
			berth_id = f"M-BERTH-{i:03d}"
			if not frappe.db.exists("Berth", {"berth_id": berth_id}):
				frappe.get_doc({
					"doctype": "Berth",
					"berth_id": berth_id,
					"property": random.choice(properties),
					"length_limit": 60,
					"status": "Available",
					"hourly_rate": 100
				}).insert(ignore_permissions=True)

		# 7. Cruise Cabins
		for i in range(1, 6):
			cabin_no = f"CR-CABIN-{i:03d}"
			if not frappe.db.exists("Cruise Cabin", {"cabin_number": cabin_no}):
				frappe.get_doc({
					"doctype": "Cruise Cabin",
					"cabin_number": cabin_no,
					"vessel_name": "Sky Cruise",
					"cabin_type": "Balcony",
					"deck_level": random.randint(1, 5),
					"status": "Available"
				}).insert(ignore_permissions=True)

		# 8. Sustainability Sensors
		for i in range(1, 6):
			sensor_id = f"IOT-{i:04d}"
			if not frappe.db.exists("IoT Sensor", {"sensor_id": sensor_id}):
				frappe.get_doc({
					"doctype": "IoT Sensor",
					"sensor_id": sensor_id,
					"sensor_type": "Temperature",
					"status": "Active"
				}).insert(ignore_permissions=True)

		# 9. Concierge & Logistics
		for i in range(1, 6):
			req_id = f"TRANS-{i:04d}"
			if not frappe.db.exists("Transport Request", {"name": req_id}):
				# Just create it with naming series if it exists
				try:
					frappe.get_doc({
						"doctype": "Transport Request",
						"guest": random.choice(guests),
						"destination": "Airport",
						"status": "Pending"
					}).insert(ignore_permissions=True)
				except:
					pass

		# 10. Maintenance Assets
		for i in range(1, 6):
			name = f"Asset {i}"
			if not frappe.db.exists("Asset Register", {"asset_name": name}):
				try:
					frappe.get_doc({
						"doctype": "Asset Register",
						"asset_name": name,
						"property": random.choice(properties),
						"status": "Active"
					}).insert(ignore_permissions=True)
				except:
					pass

		frappe.db.commit()
		print("Global demo data setup completed successfully!")

	except Exception as e:
		frappe.db.rollback()
		frappe.log_error(frappe.get_traceback(), "Global Demo Data Setup Failed")
		print(f"Error setting up demo data: {str(e)}")

if __name__ == "__main__":
	run()
