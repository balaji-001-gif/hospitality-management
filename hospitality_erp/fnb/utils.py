import frappe

def get_outlet_revenue(outlet, from_date, to_date):
    return frappe.db.sql("""
        SELECT SUM(total_amount) as revenue
        FROM `tabFnB Order`
        WHERE outlet=%s AND docstatus=1
        AND creation BETWEEN %s AND %s
    """, (outlet, from_date, to_date), as_dict=True)
