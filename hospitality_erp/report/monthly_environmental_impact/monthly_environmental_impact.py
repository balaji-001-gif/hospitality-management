import frappe
from frappe import _

def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	chart = get_chart(data)
	return columns, data, None, chart

def get_columns():
	return [
		{
			"label": _("Property"),
			"fieldname": "property",
			"fieldtype": "Link",
			"options": "Property",
			"width": 150
		},
		{
			"label": _("Total Energy (kWh)"),
			"fieldname": "total_energy",
			"fieldtype": "Float",
			"width": 150
		},
		{
			"label": _("Total Water (L)"),
			"fieldname": "total_water",
			"fieldtype": "Float",
			"width": 150
		},
		{
			"label": _("Recycled Waste (kg)"),
			"fieldname": "total_recycled",
			"fieldtype": "Float",
			"width": 150
		},
		{
			"label": _("General Waste (kg)"),
			"fieldname": "total_general",
			"fieldtype": "Float",
			"width": 150
		}
	]

def get_data(filters):
	query_filters = {}
	if filters.get("from_date"):
		query_filters["log_date"] = [">=", filters.get("from_date")]
	if filters.get("to_date"):
		if "log_date" in query_filters:
			query_filters["log_date"] = ["between", [filters.get("from_date"), filters.get("to_date")]]
		else:
			query_filters["log_date"] = ["<=", filters.get("to_date")]
			
	data = frappe.db.get_list(
		"Sustainability Log",
		fields=[
			"property",
			"sum(energy_usage_kwh) as total_energy",
			"sum(water_usage_liters) as total_water",
			"sum(waste_recycled_kg) as total_recycled",
			"sum(waste_general_kg) as total_general"
		],
		filters=query_filters,
		group_by="property"
	)
	return data

def get_chart(data):
	labels = [d.property for d in data]
	energy_values = [d.total_energy for d in data]
	water_values = [d.total_water for d in data]
	
	return {
		"data": {
			"labels": labels,
			"datasets": [
				{"name": _("Energy (kWh)"), "values": energy_values},
				{"name": _("Water (L)"), "values": water_values}
			]
		},
		"type": "bar"
	}
