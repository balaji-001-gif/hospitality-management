frappe.ui.form.on("Guest Invoice Item", {
    rate(frm, cdt, cdn) {
        const row = locals[cdt][cdn];
        frappe.model.set_value(cdt, cdn, "amount", (row.quantity || 1) * (row.rate || 0));
    },
    quantity(frm, cdt, cdn) {
        const row = locals[cdt][cdn];
        frappe.model.set_value(cdt, cdn, "amount", (row.quantity || 1) * (row.rate || 0));
    }
});
