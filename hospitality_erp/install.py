import json
import os
import frappe


def after_install():
    create_workspace()
    load_default_masters()
    frappe.db.commit()


def create_workspace():
    if frappe.db.exists("Workspace", "Hospitality Management"):
        return
    ws_path = os.path.join(
        os.path.dirname(__file__),
        "workspace", "hospitality_erp", "hospitality_erp.json"
    )
    if not os.path.exists(ws_path):
        frappe.log_error(f"Workspace JSON not found at {ws_path}", "Install")
        return
    with open(ws_path) as f:
        ws_data = json.load(f)
    for field in ("creation", "modified", "modified_by", "owner"):
        ws_data.pop(field, None)
    doc = frappe.get_doc(ws_data)
    doc.insert(ignore_permissions=True, ignore_links=True)


def load_default_masters():
    _insert_if_missing("Property Type", "type_name", [
        "Hotel", "Resort", "Boutique Hotel", "Hostel", "Villa", "Service Apartment"
    ])
    _insert_if_missing("Room Category", "category_name", [
        "Standard", "Deluxe", "Superior", "Suite",
        "Junior Suite", "Presidential Suite", "Villa", "Penthouse"
    ])
    _insert_if_missing("Rate Category", "category_name", [
        "Rack Rate", "Corporate Rate", "OTA Rate",
        "Package Rate", "Day Use", "Complimentary"
    ])
    _insert_if_missing("Channel", "channel_name", [
        "Direct", "Walk-in", "MakeMyTrip", "Agoda",
        "Booking.com", "Expedia", "OYO", "Corporate", "Travel Agent"
    ])
    _insert_if_missing("Meal Plan", "plan_name", [
        "EP - No Meals", "CP - Breakfast Only",
        "MAP - Breakfast & Dinner", "AP - All Meals"
    ])
    _insert_if_missing("Tax Category", "category_name", [
        "GST 12%", "GST 18%", "Luxury Tax", "Service Charge", "GST Exempt"
    ])
    _insert_if_missing("Amenity Type", "type_name", [
        "In-Room", "Property", "F&B", "Recreation", "Business"
    ])
    frappe.db.commit()


def _insert_if_missing(doctype, name_field, values):
    for v in values:
        if not frappe.db.exists(doctype, v):
            try:
                frappe.get_doc({"doctype": doctype, name_field: v, "name": v}).insert(
                    ignore_permissions=True
                )
            except Exception as e:
                frappe.log_error(str(e), f"Install {doctype}")
