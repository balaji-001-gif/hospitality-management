frappe.query_reports["Housekeeping Status"] = {
    filters: [
        {fieldname: "property", label: __("Property"), fieldtype: "Link", options: "Property"},
        {fieldname: "status", label: __("Status"), fieldtype: "Select", options: "\nVacant Clean\nVacant Dirty\nOccupied\nOut of Order\nUnder Maintenance"},
    ],
};
