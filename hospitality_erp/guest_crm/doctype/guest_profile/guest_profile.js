frappe.ui.form.on("Guest Profile", {
    refresh(frm) {
        if (!frm.is_new()) {
            frm.add_custom_button(__("View Reservations"), () => {
                frappe.set_route("List", "Reservation", { guest: frm.doc.name });
            });
        }
    }
});
