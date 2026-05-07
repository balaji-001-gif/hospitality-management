frappe.query_reports["Guest Feedback Summary"] = {
    filters: [
        {fieldname: "property", label: __("Property"), fieldtype: "Link", options: "Property"},
        {fieldname: "from_date", label: __("From Date"), fieldtype: "Date", default: frappe.datetime.add_months(frappe.datetime.get_today(), -1)},
        {fieldname: "to_date", label: __("To Date"), fieldtype: "Date", default: frappe.datetime.get_today()},
    ],
};
