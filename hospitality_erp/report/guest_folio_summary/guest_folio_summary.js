frappe.query_reports["Guest Folio Summary"] = {
    filters: [
        {fieldname: "property", label: __("Property"), fieldtype: "Link", options: "Property"},
        {fieldname: "status", label: __("Status"), fieldtype: "Select", options: "\nOpen\nSettled\nCancelled"},
    ],
};
