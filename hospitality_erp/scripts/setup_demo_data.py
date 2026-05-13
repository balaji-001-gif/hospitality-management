import frappe
from frappe.utils import today, add_days, getdate
import random

def run():
	"""Main entry point for bench execute."""
	setup_demo_data()

def setup_demo_data():
	# 0. Self-healing for Lost and Found (Force module alignment)
	if not frappe.db.exists("Module Def", "Housekeeping"):
		frappe.get_doc({
			"doctype": "Module Def",
			"module_name": "Housekeeping",
			"app_name": "hospitality_erp"
		}).insert(ignore_permissions=True)
		frappe.db.commit()

	if frappe.db.exists("DocType", "Lost and Found"):
		frappe.db.sql("""
			UPDATE `tabDocType` 
			SET module = 'Housekeeping', custom = 0 
			WHERE name = 'Lost and Found'
		""")
		frappe.db.commit()
		# Clear all related caches
		frappe.clear_cache(doctype="Lost and Found")
		frappe.cache().delete_value("doctype_module:Lost and Found")
		frappe.logger().info("Forced module for Lost and Found to Housekeeping via direct SQL")

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
		rooms = []
		room_types = []
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
			room_types.extend(created_rt)
			
			for i in range(1, 11):
				room_no = f"{prop[:3].upper()}-{i:03d}"
				if not frappe.db.exists("Room", {"room_number": room_no}):
					room = frappe.get_doc({
						"doctype": "Room",
						"room_number": room_no,
						"property": prop,
						"room_type": random.choice(created_rt),
						"status": "Vacant Clean"
					}).insert(ignore_permissions=True)
					rooms.append(room.name)
				else:
					rooms.append(frappe.db.get_value("Room", {"room_number": room_no}))

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

		# 5. F&B (10 Outlets, 10 Tables, 10 Menu Items)
		outlets = []
		for i in range(1, 11):
			name = f"Premium Outlet {i}"
			if not frappe.db.exists("Outlet", {"outlet_name": name}):
				outlet = frappe.get_doc({
					"doctype": "Outlet",
					"outlet_name": name,
					"property": random.choice(properties)
				}).insert(ignore_permissions=True)
				outlets.append(outlet.name)
				
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
			else:
				outlets.append(frappe.db.get_value("Outlet", {"outlet_name": name}))

		menu_items = []
		for i in range(1, 21):
			name = f"Signature Dish {i}"
			if not frappe.db.exists("Menu Item", {"item_name": name}):
				item = frappe.get_doc({
					"doctype": "Menu Item",
					"naming_series": "MENU-.YYYY.-",
					"item_name": name,
					"rate": random.randint(15, 100),
					"category": random.choice(["Appetizer", "Main Course", "Dessert", "Beverage"])
				}).insert(ignore_permissions=True)
				menu_items.append(item.name)
			else:
				menu_items.append(frappe.db.get_value("Menu Item", {"item_name": name}))

		# 6. Reservations (10 entries)
		reservations = []
		for i in range(1, 11):
			check_in = add_days(today(), random.randint(-5, 5))
			res = frappe.get_doc({
				"doctype": "Reservation",
				"naming_series": "RES-.YYYY.-",
				"guest": random.choice(guests),
				"property": random.choice(properties),
				"room_type": random.choice(room_types),
				"check_in_date": check_in,
				"check_out_date": add_days(check_in, random.randint(1, 7)),
				"status": "Confirmed",
				"rate_per_night": random.randint(200, 1000)
			}).insert(ignore_permissions=True)
			reservations.append(res.name)

		# 7. Laundry Orders (10 entries)
		for i in range(1, 11):
			frappe.get_doc({
				"doctype": "Laundry Order",
				"naming_series": "LAU-.YYYY.-",
				"guest": random.choice(guests),
				"property": random.choice(properties),
				"room": random.choice(rooms),
				"status": "Pickup Requested",
				"item_count": random.randint(1, 10),
				"amount": random.randint(20, 150)
			}).insert(ignore_permissions=True)

		# 8. Lost and Found (5 entries)
		frappe.logger().info("Setting up Lost and Found...")
		for i in range(1, 6):
			try:
				frappe.get_doc({
					"doctype": "Lost and Found",
					"naming_series": "LNF-.YYYY.-",
					"item_description": random.choice(["iPhone 13", "Leather Wallet", "Keycard", "Sunglasses", "Watch"]),
					"property": random.choice(properties),
					"status": "In Custody",
					"found_date": today()
				}).insert(ignore_permissions=True)
			except Exception as e:
				frappe.logger().error(f"Failed to insert Lost and Found: {str(e)}")
				raise e

		# 9. Maintenance Requests (10 entries)
		for i in range(1, 11):
			frappe.get_doc({
				"doctype": "Maintenance Request",
				"naming_series": "MNT-.YYYY.-",
				"property": random.choice(properties),
				"room": random.choice(rooms),
				"issue_description": random.choice(["AC not cooling", "Leaking faucet", "TV remote broken", "Light flicker"]),
				"priority": random.choice(["Low", "Medium", "High"]),
				"status": "Open"
			}).insert(ignore_permissions=True)

		# 10. FnB Orders (10 entries)
		for i in range(1, 11):
			order = frappe.get_doc({
				"doctype": "FnB Order",
				"naming_series": "FNBO-.YYYY.-",
				"outlet": random.choice(outlets),
				"status": "Open"
			})
			for _ in range(random.randint(1, 3)):
				order.append("order_items", {
					"item": random.choice(menu_items),
					"quantity": random.randint(1, 3),
					"rate": 50 # Simplified
				})
			order.insert(ignore_permissions=True)

		frappe.db.commit()
		print("Hyper-comprehensive global demo data setup completed successfully!")

	except Exception as e:
		frappe.db.rollback()
		frappe.log_error(frappe.get_traceback(), "Global Demo Data Setup Failed")
		print(f"Error setting up demo data: {str(e)}")

if __name__ == "__main__":
	run()
