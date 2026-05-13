import frappe
from frappe.utils import nowdate, add_days

def run():
    print("Setting up demo data for HospitaLeisure ERP...")
    try:
        # Core Infrastructure
        create_property_types()
        create_properties()
        create_room_categories()
        create_meal_plans()
        create_room_types()
        create_rooms()
        create_banquet_halls()
        
        # Guest CRM
        create_guests()
        
        # Transactions
        create_reservations()
        create_maintenance_requests()
        create_event_bookings()
        
        frappe.db.commit()
        print("Demo data setup completed successfully!")
    except Exception as e:
        frappe.db.rollback()
        print(f"Error setting up demo data: {e}")
        raise e

def create_property_types():
    types = ["Hotel", "Resort", "Apartment", "Villa"]
    for t in types:
        if not frappe.db.exists("Property Type", t):
            frappe.get_doc({"doctype": "Property Type", "type_name": t}).insert()

def create_properties():
    properties = [
        {
            "property_name": "Grand Leisure Resort", 
            "property_type": "Resort", 
            "city": "Goa", 
            "naming_series": "PROP-.YYYY.-"
        },
        {
            "property_name": "Skyline Boutique Hotel", 
            "property_type": "Hotel", 
            "city": "Mumbai", 
            "naming_series": "PROP-.YYYY.-"
        }
    ]
    for p in properties:
        if not frappe.db.exists("Property", {"property_name": p["property_name"]}):
            doc = frappe.get_doc({"doctype": "Property", **p})
            doc.insert()

def create_room_categories():
    categories = ["Standard", "Deluxe", "Suite", "Luxury"]
    for c in categories:
        if not frappe.db.exists("Room Category", c):
            frappe.get_doc({"doctype": "Room Category", "category_name": c}).insert()

def create_meal_plans():
    plans = [
        {"plan_name": "Room Only", "code": "EP"},
        {"plan_name": "Bed & Breakfast", "code": "CP"},
        {"plan_name": "Half Board", "code": "MAP"},
        {"plan_name": "Full Board", "code": "AP"}
    ]
    for p in plans:
        if not frappe.db.exists("Meal Plan", p["plan_name"]):
            frappe.get_doc({"doctype": "Meal Plan", **p}).insert()

def create_room_types():
    # Resolve Property IDs
    prop1 = frappe.db.get_value("Property", {"property_name": "Grand Leisure Resort"})
    prop2 = frappe.db.get_value("Property", {"property_name": "Skyline Boutique Hotel"})
    
    room_types = [
        {
            "type_name": "Deluxe King", 
            "property": prop1, 
            "base_rate": 5000, 
            "max_occupancy": 2, 
            "naming_series": "RT-.YYYY.-",
            "room_category": "Deluxe"
        },
        {
            "type_name": "Luxury Suite", 
            "property": prop1, 
            "base_rate": 12000, 
            "max_occupancy": 3, 
            "naming_series": "RT-.YYYY.-",
            "room_category": "Suite"
        },
        {
            "type_name": "Business Single", 
            "property": prop2, 
            "base_rate": 3500, 
            "max_occupancy": 1, 
            "naming_series": "RT-.YYYY.-",
            "room_category": "Standard"
        }
    ]
    for rt in room_types:
        if not frappe.db.exists("Room Type", {"type_name": rt["type_name"], "property": rt["property"]}):
            doc = frappe.get_doc({"doctype": "Room Type", **rt})
            doc.insert()

def create_rooms():
    # Resolve Property and Room Type IDs
    prop1 = frappe.db.get_value("Property", {"property_name": "Grand Leisure Resort"})
    rt_deluxe = frappe.db.get_value("Room Type", {"type_name": "Deluxe King", "property": prop1})
    rt_suite = frappe.db.get_value("Room Type", {"type_name": "Luxury Suite", "property": prop1})
    
    rooms = [
        {"room_number": "101", "property": prop1, "room_type": rt_deluxe, "floor": "1st Floor"},
        {"room_number": "102", "property": prop1, "room_type": rt_deluxe, "floor": "1st Floor"},
        {"room_number": "201", "property": prop1, "room_type": rt_suite, "floor": "2nd Floor"}
    ]
    for r in rooms:
        if not frappe.db.exists("Room", {"room_number": r["room_number"], "property": r["property"]}):
            doc = frappe.get_doc({"doctype": "Room", **r})
            doc.insert()

def create_banquet_halls():
    prop1 = frappe.db.get_value("Property", {"property_name": "Grand Leisure Resort"})
    halls = [
        {"hall_name": "Grand Ballroom", "property": prop1, "capacity": 500, "base_rate_per_day": 50000},
        {"hall_name": "Emerald Room", "property": prop1, "capacity": 100, "base_rate_per_day": 15000}
    ]
    for h in halls:
        if not frappe.db.exists("Banquet Hall", h["hall_name"]):
            doc = frappe.get_doc({"doctype": "Banquet Hall", **h})
            doc.insert()

def create_guests():
    guests = [
        {
            "full_name": "John Doe", 
            "email": "john.doe@example.com", 
            "phone": "+1234567890", 
            "naming_series": "GUEST-.YYYY.-"
        },
        {
            "full_name": "Jane Smith", 
            "email": "jane.smith@example.com", 
            "phone": "+9876543210", 
            "naming_series": "GUEST-.YYYY.-"
        }
    ]
    for g in guests:
        if not frappe.db.exists("Guest Profile", {"email": g["email"]}):
            doc = frappe.get_doc({"doctype": "Guest Profile", **g})
            doc.insert()

def create_reservations():
    guest = frappe.db.get_value("Guest Profile", {"full_name": "John Doe"})
    prop = frappe.db.get_value("Property", {"property_name": "Grand Leisure Resort"})
    rt = frappe.db.get_value("Room Type", {"type_name": "Deluxe King", "property": prop})
    room = frappe.db.get_value("Room", {"room_number": "101", "property": prop})
    
    if not frappe.db.exists("Reservation", {"guest": guest, "status": "Confirmed"}):
        doc = frappe.get_doc({
            "doctype": "Reservation",
            "naming_series": "RES-.YYYY.-",
            "guest": guest,
            "property": prop,
            "room_type": rt,
            "room": room,
            "check_in_date": nowdate(),
            "check_out_date": add_days(nowdate(), 2),
            "status": "Confirmed",
            "adults": 2,
            "rate_per_night": 5000
        })
        doc.insert()

def create_maintenance_requests():
    prop = frappe.db.get_value("Property", {"property_name": "Grand Leisure Resort"})
    room = frappe.db.get_value("Room", {"room_number": "102", "property": prop})
    
    if not frappe.db.exists("Maintenance Request", {"title": "AC Not Working", "room": room}):
        doc = frappe.get_doc({
            "doctype": "Maintenance Request",
            "naming_series": "MR-.YYYY.-",
            "title": "AC Not Working",
            "description": "The AC in room 102 is making loud noise and not cooling.",
            "property": prop,
            "room": room,
            "priority": "High",
            "status": "Open",
            "category": "AC/HVAC"
        })
        doc.insert()

def create_event_bookings():
    prop = frappe.db.get_value("Property", {"property_name": "Grand Leisure Resort"})
    hall = frappe.db.get_value("Banquet Hall", {"hall_name": "Grand Ballroom", "property": prop})
    
    if not frappe.db.exists("Event Booking", {"event_name": "Annual Corporate Gala"}):
        doc = frappe.get_doc({
            "doctype": "Event Booking",
            "naming_series": "EVT-.YYYY.-",
            "event_name": "Annual Corporate Gala",
            "client_name": "TechCorp Inc.",
            "property": prop,
            "banquet_hall": hall,
            "event_date": add_days(nowdate(), 15),
            "pax_count": 300,
            "event_type": "Corporate",
            "hall_charges": 50000,
            "catering_charges": 150000
        })
        doc.insert()
