import frappe
from frappe import _


def execute(filters=None):
    filters = filters or {}
    columns = [
        {"label": _("Outlet"), "fieldname": "outlet", "fieldtype": "Link", "options": "Outlet", "width": 150},
        {"label": _("Menu Item"), "fieldname": "menu_item", "fieldtype": "Data", "width": 180},
        {"label": _("Qty Sold"), "fieldname": "qty_sold", "fieldtype": "Float", "width": 90},
        {"label": _("Revenue"), "fieldname": "revenue", "fieldtype": "Currency", "width": 120},
        {"label": _("Recipe Cost"), "fieldname": "recipe_cost", "fieldtype": "Currency", "width": 120},
        {"label": _("Gross Profit"), "fieldname": "gross_profit", "fieldtype": "Currency", "width": 120},
        {"label": _("Margin %"), "fieldname": "margin_pct", "fieldtype": "Percent", "width": 90},
    ]
    conditions = "WHERE fo.docstatus = 1"
    if filters.get("outlet"):
        conditions += " AND fo.outlet = %(outlet)s"
    if filters.get("from_date"):
        conditions += " AND fo.creation >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " AND fo.creation <= %(to_date)s"

    data = frappe.db.sql(f"""
        SELECT fo.outlet, foi.menu_item,
               SUM(foi.quantity) as qty_sold,
               SUM(foi.amount) as revenue,
               SUM(foi.quantity * IFNULL(mi.cost, 0)) as recipe_cost
        FROM `tabFnB Order` fo
        JOIN `tabFnB Order Item` foi ON foi.parent = fo.name
        LEFT JOIN `tabMenu Item` mi ON mi.item_name = foi.menu_item
        {conditions}
        GROUP BY fo.outlet, foi.menu_item
        ORDER BY revenue DESC
    """, filters, as_dict=True)

    for row in data:
        row.gross_profit = row.revenue - (row.recipe_cost or 0)
        row.margin_pct = round((row.gross_profit / row.revenue * 100), 2) if row.revenue else 0
    return columns, data
