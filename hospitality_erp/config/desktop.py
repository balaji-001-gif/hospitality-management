from frappe import _

def get_data():
    return [
        {
            "module_name": "Reservations",
            "app": "hospitality_erp",
            "label": _("Reservations"),
            "color": "#1a73e8",
            "icon": "uil uil-calendar-alt",
            "type": "module",
        },
        {
            "module_name": "Property Management",
            "app": "hospitality_erp",
            "label": _("Property Management"),
            "color": "#27ae60",
            "icon": "uil uil-building",
            "type": "module",
        },
        {
            "module_name": "Guest CRM",
            "app": "hospitality_erp",
            "label": _("Guest CRM"),
            "color": "#8e44ad",
            "icon": "uil uil-users-alt",
            "type": "module",
        },
        {
            "module_name": "Finance",
            "app": "hospitality_erp",
            "label": _("Finance"),
            "color": "#e67e22",
            "icon": "uil uil-invoice",
            "type": "module",
        },
        {
            "module_name": "Housekeeping",
            "app": "hospitality_erp",
            "label": _("Housekeeping"),
            "color": "#16a085",
            "icon": "uil uil-broom",
            "type": "module",
        },
        {
            "module_name": "Maintenance",
            "app": "hospitality_erp",
            "label": _("Maintenance"),
            "color": "#c0392b",
            "icon": "uil uil-wrench",
            "type": "module",
        },
        {
            "module_name": "FnB",
            "app": "hospitality_erp",
            "label": _("Food and Beverage"),
            "color": "#e74c3c",
            "icon": "uil uil-utensils",
            "type": "module",
        },
    ]
