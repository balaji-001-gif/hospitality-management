frappe.ui.form.on("Guest Folio Item", {
    rate(frm, cdt, cdn) {
        const row = locals[cdt][cdn];
        frappe.model.set_value(cdt, cdn, "amount", (row.quantity || 1) * (row.rate || 0));
        frm.trigger("calc_total");
    },
    quantity(frm, cdt, cdn) {
        const row = locals[cdt][cdn];
        frappe.model.set_value(cdt, cdn, "amount", (row.quantity || 1) * (row.rate || 0));
        frm.trigger("calc_total");
    }
});
frappe.ui.form.on("Guest Folio", {
    calc_total(frm) {
        const total = (frm.doc.charges || []).reduce((s, r) => s + (r.amount || 0), 0);
        frm.set_value("total_charges", total);
        frm.set_value("balance", total - (frm.doc.total_paid || 0));
    },
    total_paid(frm) { frm.trigger("calc_total"); }
});
