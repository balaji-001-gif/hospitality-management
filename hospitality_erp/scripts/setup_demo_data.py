import frappe
from frappe import _
from datetime import datetime, timedelta

def run():
    print("Setting up demo data for HospitaLeisure ERP...")
    try:
        # Core Infrastructure
        create_properties()
        create_room_types()
        create_rooms()
        
        # CRM & Guests
        create_guests()
        
        # F&B
        create_fb_outlets()
        create_tables()
        create_menu_items()
        create_pos_orders()
        
        # Services
        create_laundry_services()
        
        # Spa & Recreation
        create_spa_therapists()
        create_spa_services()
        create_spa_bookings()
        
        # Events & Banquet
        create_banquet_halls()
        create_event_bookings()
        
        # Membership
        create_membership_plans()
        create_leisure_memberships()
        
        # Cinema
        create_cinema_halls()
        create_movie_shows()
        
        # Tourism & Attractions
        create_attractions()
        create_visitor_passes()
        
        # HR & Security
        create_visitor_logs()
        create_staff_shifts()
        
        # Maintenance
        create_maintenance_requests()
        
        frappe.db.commit()
        print("Demo data setup completed successfully!")
        
    except Exception as e:
        frappe.db.rollback()
        print(f"Error setting up demo data: {e}")
        raise e

def create_properties():
    properties = [
        {"property_name": "Grand Leisure Resort", "property_type": "Resort", "location": "Goa"},
        {"property_name": "Skyline Boutique Hotel", "property_type": "Boutique", "location": "Mumbai"}
    ]
    for p in properties:
        if not frappe.db.exists("Property", p["property_name"]):
            doc = frappe.get_doc({"doctype": "Property", **p})
            doc.insert()

def create_room_types():
    room_types = [
        {"room_type_name": "Deluxe Room", "base_rate": 5000},
        {"room_type_name": "Executive Suite", "base_rate": 12000},
        {"room_type_name": "Presidential Suite", "base_rate": 25000}
    ]
    for rt in room_types:
        if not frappe.db.exists("Room Type", rt["room_type_name"]):
            doc = frappe.get_doc({"doctype": "Room Type", **rt})
            doc.insert()

def create_rooms():
    rooms = [
        {"room_number": "101", "room_type": "Deluxe Room", "property": "Grand Leisure Resort"},
        {"room_number": "102", "room_type": "Deluxe Room", "property": "Grand Leisure Resort"},
        {"room_number": "501", "room_type": "Executive Suite", "property": "Skyline Boutique Hotel"}
    ]
    for r in rooms:
        if not frappe.db.exists("Room", r["room_number"]):
            doc = frappe.get_doc({"doctype": "Room", **r})
            doc.insert()

def create_guests():
    guests = [
        {"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com", "phone": "9876543210"},
        {"first_name": "Jane", "last_name": "Smith", "email": "jane.smith@example.com", "phone": "9876543211"}
    ]
    for g in guests:
        if not frappe.db.exists("Guest Profile", {"email": g["email"]}):
            doc = frappe.get_doc({"doctype": "Guest Profile", **g})
            doc.insert()

def create_fb_outlets():
    outlets = [
        {"outlet_name": "Spice Garden", "outlet_type": "Restaurant", "property": "Grand Leisure Resort"},
        {"outlet_name": "Ocean Breeze Bar", "outlet_type": "Bar", "property": "Grand Leisure Resort"}
    ]
    for o in outlets:
        if not frappe.db.exists("F&B Outlet", o["outlet_name"]):
            doc = frappe.get_doc({"doctype": "F&B Outlet", **o})
            doc.insert()

def create_tables():
    if not frappe.db.exists("F&B Outlet", "Spice Garden"): return
    tables = [
        {"table_number": "T1", "capacity": 4, "outlet": "Spice Garden"},
        {"table_number": "T2", "capacity": 2, "outlet": "Spice Garden"}
    ]
    for t in tables:
        if not frappe.db.exists("Table", {"table_number": t["table_number"], "outlet": t["outlet"]}):
            doc = frappe.get_doc({"doctype": "Table", **t})
            doc.insert()

def create_menu_items():
    items = [
        {"item_name": "Grilled Salmon", "category": "Main Course", "price": 850, "outlet": "Spice Garden"},
        {"item_name": "Caesar Salad", "category": "Starters", "price": 450, "outlet": "Spice Garden"}
    ]
    for i in items:
        if not frappe.db.exists("Menu Item", i["item_name"]):
            doc = frappe.get_doc({"doctype": "Menu Item", **i})
            doc.insert()

def create_pos_orders():
    if not frappe.db.exists("Menu Item", "Grilled Salmon"): return
    if not frappe.db.exists("Guest Profile", "John Doe"): return
    
    order = {
        "doctype": "POS Order",
        "outlet": "Spice Garden",
        "guest": "John Doe",
        "order_date": frappe.utils.today(),
        "items": [{"item": "Grilled Salmon", "qty": 1, "rate": 850}]
    }
    doc = frappe.get_doc(order)
    doc.insert()

def create_laundry_services():
    services = [
        {"service_name": "Dry Cleaning", "rate": 200},
        {"service_name": "Ironing", "rate": 50}
    ]
    for s in services:
        if not frappe.db.exists("Laundry Service", s["service_name"]):
            doc = frappe.get_doc({"doctype": "Laundry Service", **s})
            doc.insert()

def create_spa_therapists():
    therapists = [
        {"therapist_name": "Elena Gilbert", "specialization": "Swedish Massage"},
        {"therapist_name": "Damon Salvatore", "specialization": "Deep Tissue"}
    ]
    for t in therapists:
        if not frappe.db.exists("Therapist", t["therapist_name"]):
            doc = frappe.get_doc({"doctype": "Therapist", **t})
            doc.insert()

def create_spa_services():
    services = [
        {"service_name": "Aromatherapy", "duration": 60, "price": 3000},
        {"service_name": "Thai Massage", "duration": 90, "price": 4500}
    ]
    for s in services:
        if not frappe.db.exists("Spa Service", s["service_name"]):
            doc = frappe.get_doc({"doctype": "Spa Service", **s})
            doc.insert()

def create_spa_bookings():
    if not frappe.db.exists("Spa Service", "Aromatherapy"): return
    booking = {
        "doctype": "Spa Booking",
        "guest": "John Doe",
        "spa_service": "Aromatherapy",
        "booking_date": frappe.utils.today(),
        "status": "Booked"
    }
    doc = frappe.get_doc(booking)
    doc.insert()

def create_banquet_halls():
    halls = [
        {"hall_name": "Grand Ballroom", "capacity": 500, "property": "Grand Leisure Resort"},
        {"hall_name": "Royal Pavilion", "capacity": 200, "property": "Grand Leisure Resort"}
    ]
    for h in halls:
        if not frappe.db.exists("Banquet Hall", h["hall_name"]):
            doc = frappe.get_doc({"doctype": "Banquet Hall", **h})
            doc.insert()

def create_event_bookings():
    if not frappe.db.exists("Banquet Hall", "Grand Ballroom"): return
    booking = {
        "doctype": "Event Booking",
        "event_name": "Annual Corporate Gala",
        "client_name": "Acme Corp",
        "banquet_hall": "Grand Ballroom",
        "event_date": frappe.utils.add_days(frappe.utils.today(), 10),
        "status": "Tentative"
    }
    doc = frappe.get_doc(booking)
    doc.insert()

def create_membership_plans():
    plans = [
        {"plan_name": "Gold Membership", "duration_months": 12, "price": 50000},
        {"plan_name": "Platinum Membership", "duration_months": 12, "price": 85000}
    ]
    for p in plans:
        if not frappe.db.exists("Membership Plan", p["plan_name"]):
            doc = frappe.get_doc({"doctype": "Membership Plan", **p})
            doc.insert()

def create_leisure_memberships():
    if not frappe.db.exists("Membership Plan", "Gold Membership"): return
    membership = {
        "doctype": "Leisure Membership",
        "guest": "Jane Smith",
        "membership_plan": "Gold Membership",
        "start_date": frappe.utils.today(),
        "end_date": frappe.utils.add_months(frappe.utils.today(), 12),
        "status": "Active"
    }
    doc = frappe.get_doc(membership)
    doc.insert()

def create_cinema_halls():
    halls = [
        {"hall_name": "Screen 1", "property": "Grand Leisure Resort", "capacity": 150},
        {"hall_name": "IMAX Screen", "property": "Grand Leisure Resort", "capacity": 100}
    ]
    for h in halls:
        if not frappe.db.exists("Cinema Hall", h["hall_name"]):
            doc = frappe.get_doc({"doctype": "Cinema Hall", **h})
            doc.insert()

def create_movie_shows():
    if not frappe.db.exists("Cinema Hall", "Screen 1"): return
    shows = [
        {"movie_name": "Interstellar", "cinema_hall": "Screen 1", "show_date": frappe.utils.today(), "show_time": "18:00:00"},
        {"movie_name": "Inception", "cinema_hall": "IMAX Screen", "show_date": frappe.utils.today(), "show_time": "21:00:00"}
    ]
    for s in shows:
        doc = frappe.get_doc({"doctype": "Movie Show", **s})
        doc.insert()

def create_attractions():
    attractions = [
        {"attraction_name": "Water Park", "location": "Resort North Wing", "property": "Grand Leisure Resort"},
        {"attraction_name": "Infinity Pool", "location": "Rooftop", "property": "Skyline Boutique Hotel"}
    ]
    for a in attractions:
        if not frappe.db.exists("Attraction", a["attraction_name"]):
            doc = frappe.get_doc({"doctype": "Attraction", **a})
            doc.insert()

def create_visitor_passes():
    if not frappe.db.exists("Attraction", "Water Park"): return
    pass_doc = {
        "doctype": "Visitor Pass",
        "visitor_name": "Alice Wonderland",
        "attraction": "Water Park",
        "valid_date": frappe.utils.today()
    }
    doc = frappe.get_doc(pass_doc)
    doc.insert()

def create_visitor_logs():
    log = {
        "doctype": "Visitor Log",
        "visitor_name": "Bob Builder",
        "purpose": "Maintenance Check",
        "entry_time": frappe.utils.now_datetime()
    }
    doc = frappe.get_doc(log)
    doc.insert()

def create_staff_shifts():
    shift = {
        "doctype": "Staff Shift",
        "shift_name": "Morning Shift - Front Desk",
        "shift_date": frappe.utils.today(),
        "start_time": "08:00:00",
        "end_time": "16:00:00",
        "status": "Scheduled"
    }
    doc = frappe.get_doc(shift)
    doc.insert()

def create_maintenance_requests():
    request = {
        "doctype": "Maintenance Request",
        "title": "AC Not Working",
        "description": "The AC in room 101 is making loud noise and not cooling.",
        "property": "Grand Leisure Resort",
        "room": "101",
        "priority": "High",
        "status": "Open"
    }
    doc = frappe.get_doc(request)
    doc.insert()
