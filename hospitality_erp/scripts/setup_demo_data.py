import frappe

def run():
	"""Main entry point for bench execute."""
	setup_demo_data()

def setup_demo_data():
	frappe.logger().info("Setting up Hospitality & Leisure Demo Data...")
	
	try:
		# 1. Properties
		if not frappe.db.exists("Property", {"property_name": "Royal Palm Resort"}):
			prop = frappe.get_doc({
				"doctype": "Property",
				"naming_series": "PROP-.YYYY.-",
				"property_name": "Royal Palm Resort",
				"city": "Dubai",
				"country": "United Arab Emirates"
			}).insert(ignore_permissions=True)
			prop_name = prop.name
		else:
			prop_name = "Royal Palm Resort"

		# 2. Theme Park Attraction
		if not frappe.db.exists("Theme Park Attraction", "Dragon Coaster"):
			frappe.get_doc({
				"doctype": "Theme Park Attraction",
				"attraction_name": "Dragon Coaster",
				"type": "Ride",
				"status": "Open",
				"capacity": 1200,
				"minimum_height": 120.0
			}).insert(ignore_permissions=True)

		# 3. Cinema Hall
		if not frappe.db.exists("Cinema Hall", "Screen 1 - IMAX"):
			frappe.get_doc({
				"doctype": "Cinema Hall",
				"hall_name": "Screen 1 - IMAX",
				"property": prop_name,
				"capacity": 250,
				"screen_type": "IMAX"
			}).insert(ignore_permissions=True)

		# 4. Marina Berth
		if not frappe.db.exists("Berth", "B-001"):
			frappe.get_doc({
				"doctype": "Berth",
				"berth_id": "B-001",
				"property": prop_name,
				"length_limit": 50.0,
				"status": "Available",
				"hourly_rate": 150.0
			}).insert(ignore_permissions=True)

		# 5. Cruise Cabin
		if not frappe.db.exists("Cruise Cabin", "C-701"):
			frappe.get_doc({
				"doctype": "Cruise Cabin",
				"cabin_number": "C-701",
				"vessel_name": "Sea Majesty",
				"cabin_type": "Suite",
				"deck_level": 7,
				"status": "Available"
			}).insert(ignore_permissions=True)

		# 6. Restaurant Table
		if not frappe.db.exists("Restaurant Table", "T-10"):
			# Ensure an outlet exists
			if not frappe.db.exists("Outlet", "Main Dining"):
				frappe.get_doc({
					"doctype": "Outlet",
					"outlet_name": "Main Dining"
				}).insert(ignore_permissions=True)
				
			frappe.get_doc({
				"doctype": "Restaurant Table",
				"table_number": "T-10",
				"outlet": "Main Dining",
				"capacity": 4,
				"status": "Available"
			}).insert(ignore_permissions=True)

		frappe.db.commit()
		print("Comprehensive demo data setup completed successfully!")

	except Exception as e:
		frappe.db.rollback()
		print(f"Error setting up demo data: {str(e)}")

if __name__ == "__main__":
	run()
