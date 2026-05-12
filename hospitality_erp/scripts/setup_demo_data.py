import frappe

def setup_demo_data():
	frappe.logger().info("Setting up Hospitality & Leisure Demo Data...")
	
	try:
		# Create Membership Plan
		if not frappe.db.exists("Membership Plan", {"plan_name": "Gold Annual"}):
			frappe.get_doc({
				"doctype": "Membership Plan",
				"plan_name": "Gold Annual",
				"membership_type": "Annual",
				"amount": 1200.0,
				"is_active": 1
			}).insert(ignore_permissions=True)

		# Create Facility
		if not frappe.db.exists("Facility", {"facility_name": "Main Tennis Court"}):
			# Assume a default property exists or we'll create a dummy one
			prop = frappe.db.get_value("Property", {"name": ["!=", ""]})
			if not prop:
				prop = frappe.get_doc({
					"doctype": "Property",
					"property_name": "Demo Resort",
					"city": "Demo City"
				}).insert(ignore_permissions=True).name

			frappe.get_doc({
				"doctype": "Facility",
				"facility_name": "Main Tennis Court",
				"facility_type": "Tennis Court",
				"property": prop,
				"capacity": 4,
				"is_active": 1
			}).insert(ignore_permissions=True)

		frappe.db.commit()
		print("Demo data setup completed successfully!")

	except Exception as e:
		frappe.db.rollback()
		print(f"Error setting up demo data: {str(e)}")

if __name__ == "__main__":
	setup_demo_data()
