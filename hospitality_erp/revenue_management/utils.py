import frappe

def get_rate_for_date(property_name, room_type, check_in_date):
    seasonal = frappe.db.get_value(
        "Seasonal Pricing",
        {"property": property_name, "room_type": room_type,
         "from_date": ["<=", check_in_date], "to_date": [">=", check_in_date], "is_active": 1},
        "rate"
    )
    return seasonal
