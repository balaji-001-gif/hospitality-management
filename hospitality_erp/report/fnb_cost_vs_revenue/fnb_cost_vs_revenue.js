frappe.query_reports["F&B Cost vs Revenue"] = {
    filters: [
        {fieldname: "outlet", label: __("Outlet"), fieldtype: "Link", options: "Outlet"},
        {fieldname: "from_date", label: __("From Date"), fieldtype: "Date", default: frappe.datetime.add_months(frappe.datetime.get_today(), -1)},
        {fieldname: "to_date", label: __("To Date"), fieldtype: "Date", default: frappe.datetime.get_today()},
    ],
};
