// Hospitality ERP — Global JS Utilities
frappe.provide("hospitality_erp");
hospitality_erp = {
    get_room_status_color(status) {
        const map = {
            "Vacant Clean": "green", "Vacant Dirty": "orange",
            "Occupied": "blue", "Out of Order": "red",
            "Under Maintenance": "gray",
        };
        return map[status] || "gray";
    },
};
