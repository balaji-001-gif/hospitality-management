app_name = "hospitality_erp"
app_title = "Hospitality ERP"
app_publisher = "Your Company"
app_description = "Hospitality ERP for hotels, resorts and multi-property groups"
app_email = "dev@yourcompany.com"
app_license = "MIT"
app_version = "0.0.1"

required_apps = ["frappe", "erpnext"]

app_include_css = "/assets/hospitality_erp/css/hospitality_erp.css"
app_include_js = "/assets/hospitality_erp/js/hospitality_erp.js"

doc_events = {
    "Reservation": {
        "after_insert": "hospitality_erp.reservations.doctype.reservation.reservation.after_insert",
        "on_submit": "hospitality_erp.reservations.doctype.reservation.reservation.on_submit",
    },
    "Room": {
        "on_update": "hospitality_erp.property_management.doctype.room.room.on_update",
    },
    "Maintenance Request": {
        "on_update": "hospitality_erp.hotel_maintenance.doctype.maintenance_request.maintenance_request.on_update",
    },
}

scheduler_events = {
    "daily": [
        "hospitality_erp.hotel_masters.doctype.night_audit.night_audit.run_night_audit",
        "hospitality_erp.reservations.utils.send_checkin_reminders",
        "hospitality_erp.reservations.utils.send_checkout_reminders",
        "hospitality_erp.finance.utils.flag_overdue_invoices",
    ],
    "weekly": [],
}

# NOTE: Workspace is NOT listed here — v15 auto-syncs workspace/ folder
fixtures = [
    {"dt": "Custom Field", "filters": [["module", "=", "Hospitality Management"]]},
    {"dt": "Property Setter", "filters": [["module", "=", "Hospitality Management"]]},
    "Property Type",
    "Room Category",
    "Rate Category",
    "Channel",
    "Meal Plan",
    "Tax Category",
    "Amenity Type",
]

after_install = "hospitality_erp.install.after_install"
