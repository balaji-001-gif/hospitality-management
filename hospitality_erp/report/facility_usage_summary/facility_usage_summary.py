import frappe
from frappe import _

def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	return columns, data

def get_columns():
	return [
		{
			"label": _("Facility"),
			"fieldname": "facility",
			"fieldtype": "Link",
			"options": "Facility",
			"width": 150
		},
		{
			"label": _("Total Bookings"),
			"fieldname": "total_bookings",
			"fieldtype": "Int",
			"width": 120
		},
		{
			"label": _("Confirmed Bookings"),
			"fieldname": "confirmed_bookings",
			"fieldtype": "Int",
			"width": 120
		},
		{
			"label": _("Cancelled Bookings"),
			"fieldname": "cancelled_bookings",
			"fieldtype": "Int",
			"width": 120
		}
	]

def get_data(filters):
	query_filters = {}
	if filters.get("from_date"):
		query_filters["booking_date"] = [">=", filters.get("from_date")]
	if filters.get("to_date"):
		if "booking_date" in query_filters:
			query_filters["booking_date"] = ["between", [filters.get("from_date"), filters.get("to_date")]]
		else:
			query_filters["booking_date"] = ["<=", filters.get("to_date")]
			
	data = frappe.db.get_list(
		"Facility Booking",
		fields=[
			"facility",
			"count(name) as total_bookings",
			"sum(case when status='Booked' then 1 else 0 end) as confirmed_bookings",
			"sum(case when status='Cancelled' then 1 else 0 end) as cancelled_bookings"
		],
		filters=query_filters,
		group_by="facility"
	)
	return data
