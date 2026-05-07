frappe.ui.form.on("Room", {
    refresh(frm) {
        const colors = {
            "Vacant Clean": "green", "Vacant Dirty": "orange",
            "Occupied": "blue", "Out of Order": "red", "Under Maintenance": "gray"
        };
        if (frm.doc.status) {
            frm.page.set_indicator(frm.doc.status, colors[frm.doc.status] || "gray");
        }
    }
});
