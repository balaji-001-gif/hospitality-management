import frappe
from frappe.utils import today, add_days, getdate, now
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
		rooms = []
		room_types = []
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
		for i in range(1, 11):
			check_in = add_days(today(), random.randint(-5, 5))
			frappe.get_doc({
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

		# 8. Maintenance Requests (10 entries)
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

		# 9. FnB Orders (10 entries)
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

		# 10. Spa & Recreation
		therapists = []
		for i in range(1, 6):
			name = f"Therapist {i}"
			if not frappe.db.exists("Therapist", {"full_name": name}):
				therapist = frappe.get_doc({
					"doctype": "Therapist",
					"full_name": name,
					"specialization": random.choice(["Massage", "Facial", "Yoga", "Aroma Therapy"]),
					"status": "Available"
				}).insert(ignore_permissions=True)
				therapists.append(therapist.name)
			else:
				therapists.append(frappe.db.get_value("Therapist", {"full_name": name}))

		spa_services = []
		for i in range(1, 6):
			name = f"Spa Treatment {i}"
			if not frappe.db.exists("Spa Service", {"service_name": name}):
				service = frappe.get_doc({
					"doctype": "Spa Service",
					"service_name": name,
					"duration_minutes": random.choice([30, 60, 90]),
					"rate": random.randint(50, 300)
				}).insert(ignore_permissions=True)
				spa_services.append(service.name)
			else:
				spa_services.append(frappe.db.get_value("Spa Service", {"service_name": name}))

		for i in range(1, 11):
			frappe.get_doc({
				"doctype": "Spa Booking",
				"naming_series": "SPA-.YYYY.-",
				"guest": random.choice(guests),
				"service": random.choice(spa_services),
				"therapist": random.choice(therapists),
				"booking_date": today(),
				"status": "Confirmed"
			}).insert(ignore_permissions=True)

		# 11. Events
		venues = []
		for i in range(1, 6):
			name = f"Event Venue {i}"
			if not frappe.db.exists("Event Venue", {"venue_name": name}):
				venue = frappe.get_doc({
					"doctype": "Event Venue",
					"venue_name": name,
					"capacity": random.randint(50, 500),
					"rate_per_hour": random.randint(100, 1000)
				}).insert(ignore_permissions=True)
				venues.append(venue.name)
			else:
				venues.append(frappe.db.get_value("Event Venue", {"venue_name": name}))

		for i in range(1, 6):
			frappe.get_doc({
				"doctype": "Event Booking",
				"naming_series": "EVT-.YYYY.-",
				"customer_name": f"Event Customer {i}",
				"venue": random.choice(venues),
				"booking_date": today(),
				"event_type": random.choice(["Wedding", "Conference", "Birthday", "Seminar"]),
				"status": "Confirmed"
			}).insert(ignore_permissions=True)

		# 12. Membership & Fitness
		membership_plans = ["Basic", "Silver", "Gold", "Platinum"]
		for plan in membership_plans:
			if not frappe.db.exists("Membership Plan", plan):
				frappe.get_doc({
					"doctype": "Membership Plan",
					"plan_name": plan,
					"monthly_rate": random.randint(50, 500)
				}).insert(ignore_permissions=True)

		for i in range(1, 6):
			frappe.get_doc({
				"doctype": "Leisure Membership",
				"naming_series": "MEM-.YYYY.-",
				"member_name": f"Member {i}",
				"plan": random.choice(membership_plans),
				"status": "Active",
				"start_date": today()
			}).insert(ignore_permissions=True)

		# 13. Cinema & Entertainment
		halls = []
		for i in range(1, 4):
			name = f"Cinema Hall {i}"
			if not frappe.db.exists("Cinema Hall", {"hall_name": name}):
				hall = frappe.get_doc({
					"doctype": "Cinema Hall",
					"hall_name": name,
					"total_seats": random.randint(50, 200)
				}).insert(ignore_permissions=True)
				halls.append(hall.name)
			else:
				halls.append(frappe.db.get_value("Cinema Hall", {"hall_name": name}))

		for i in range(1, 6):
			frappe.get_doc({
				"doctype": "Movie Show",
				"movie_name": f"Blockbuster Movie {i}",
				"cinema_hall": random.choice(halls),
				"show_time": now(),
				"ticket_price": random.randint(10, 50)
			}).insert(ignore_permissions=True)

		# 14. Theme Park
		for i in range(1, 6):
			name = f"Attraction {i}"
			if not frappe.db.exists("Theme Park Attraction", {"attraction_name": name}):
				frappe.get_doc({
					"doctype": "Theme Park Attraction",
					"attraction_name": name,
					"type": random.choice(["Roller Coaster", "Water Slide", "Dark Ride", "Show"]),
					"status": "Operational"
				}).insert(ignore_permissions=True)

		for i in range(1, 6):
			frappe.get_doc({
				"doctype": "Attraction Ticket",
				"naming_series": "TKT-.YYYY.-",
				"visitor_name": f"Visitor {i}",
				"ticket_type": random.choice(["Adult", "Child", "Senior", "VIP"]),
				"price": random.randint(30, 150),
				"status": "Issued"
			}).insert(ignore_permissions=True)

		# 15. Security & Visitor Log
		for i in range(1, 11):
			frappe.get_doc({
				"doctype": "Visitor Log",
				"visitor_name": f"Visitor {i}",
				"purpose_of_visit": random.choice(["Guest", "Delivery", "Contractor", "Maintenance"]),
				"check_in_time": now(),
				"status": "Checked In"
			}).insert(ignore_permissions=True)

		# 16. Sustainability Log
		for i in range(1, 6):
			frappe.get_doc({
				"doctype": "Sustainability Log",
				"property": random.choice(properties),
				"energy_usage_kwh": random.randint(100, 1000),
				"water_usage_liters": random.randint(500, 5000),
				"waste_recycled_kg": random.randint(10, 100),
				"log_date": today()
			}).insert(ignore_permissions=True)

		# 17. HR & Staffing
		for i in range(1, 11):
			frappe.get_doc({
				"doctype": "Staff Shift",
				"staff_name": f"Employee {i}",
				"shift_type": random.choice(["Morning", "Afternoon", "Night"]),
				"start_time": "08:00:00",
				"end_time": "16:00:00",
				"date": today()
			}).insert(ignore_permissions=True)

		frappe.db.commit()
		print("Global Hospitality & Leisure demo data setup completed successfully!")

	except Exception as e:
		frappe.db.rollback()
		frappe.log_error(frappe.get_traceback(), "Global Demo Data Setup Failed")
		print(f"Error setting up demo data: {str(e)}")

if __name__ == "__main__":
	setup_demo_data()
