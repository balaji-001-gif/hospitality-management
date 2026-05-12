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
			"label": _("Date"),
			"fieldname": "posting_date",
			"fieldtype": "Date",
			"width": 120
		},
		{
			"label": _("Description"),
			"fieldname": "description",
			"fieldtype": "Data",
			"width": 300
		},
		{
			"label": _("Guest"),
			"fieldname": "guest",
			"fieldtype": "Link",
			"options": "Guest",
			"width": 150
		},
		{
			"label": _("Amount"),
			"fieldname": "amount",
			"fieldtype": "Currency",
			"width": 120
		}
	]

def get_data(filters):
	return frappe.db.sql(f"""
		SELECT 
			posting_date, description, parent as guest, amount
		FROM 
			`tabGuest Folio Item`
		WHERE 
			posting_date BETWEEN '{filters.from_date}' AND '{filters.to_date}'
		ORDER BY 
			posting_date DESC
	""", as_dict=1)

def get_chart(data):
	if not data:
		return None
	
	labels = []
	values = []
	
	# Aggregate by date for the chart
	daily_revenue = {}
	for row in data:
		date = str(row.posting_date)
		daily_revenue[date] = daily_revenue.get(date, 0) + row.amount
		
	for date in sorted(daily_revenue.keys()):
		labels.append(date)
		values.append(daily_revenue[date])
		
	return {
		"data": {
			"labels": labels,
			"datasets": [{"name": "Revenue", "values": values}]
		},
		"type": "bar",
		"colors": ["#7cd6fd"]
	}
