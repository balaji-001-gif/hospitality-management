import frappe
from frappe import _

def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	return columns, data

def get_columns():
	return [
		{
			"label": _("Incident ID"),
			"fieldname": "name",
			"fieldtype": "Link",
			"options": "Security Incident",
			"width": 150
		},
		{
			"label": _("Incident Type"),
			"fieldname": "incident_type",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Severity"),
			"fieldname": "severity",
			"fieldtype": "Data",
			"width": 100
		},
		{
			"label": _("Property"),
			"fieldname": "property",
			"fieldtype": "Link",
			"options": "Property",
			"width": 120
		},
		{
			"label": _("Status"),
			"fieldname": "status",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Reported By"),
			"fieldname": "reported_by",
			"fieldtype": "Data",
			"width": 150
		},
		{
			"label": _("Resolution"),
			"fieldname": "resolution",
			"fieldtype": "Small Text",
			"width": 200
		}
	]

def get_data(filters):
	query_filters = {}
	if filters.get("property"):
		query_filters["property"] = filters.get("property")
	if filters.get("status"):
		query_filters["status"] = filters.get("status")
	if filters.get("severity"):
		query_filters["severity"] = filters.get("severity")
		
	data = frappe.get_all(
		"Security Incident",
		fields=["name", "incident_type", "severity", "property", "status", "reported_by", "resolution"],
		filters=query_filters,
		order_by="creation desc"
	)
	return data
