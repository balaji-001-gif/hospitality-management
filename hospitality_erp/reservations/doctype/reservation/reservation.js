frappe.ui.form.on("Reservation", {
    refresh(frm) {
        if (!frm.is_new() && frm.doc.docstatus === 1) {
            frm.add_custom_button(__("Check In"), () => {
                frappe.new_doc("Check In", { reservation: frm.doc.name, guest: frm.doc.guest, room: frm.doc.room });
            }, __("Create"));
            frm.add_custom_button(__("Guest Folio"), () => {
                frappe.new_doc("Guest Folio", { reservation: frm.doc.name, guest: frm.doc.guest });
            }, __("Create"));
        }
    },
    check_in_date(frm) { frm.trigger("calc_nights"); },
    check_out_date(frm) { frm.trigger("calc_nights"); },
    calc_nights(frm) {
        if (frm.doc.check_in_date && frm.doc.check_out_date) {
            const d1 = frappe.datetime.str_to_obj(frm.doc.check_in_date);
            const d2 = frappe.datetime.str_to_obj(frm.doc.check_out_date);
            const nights = Math.round((d2 - d1) / (1000 * 60 * 60 * 24));
            frm.set_value("nights", nights > 0 ? nights : 0);
            frm.set_value("total_amount", nights * (frm.doc.rate_per_night || 0));
        }
    },
    rate_per_night(frm) { frm.trigger("calc_total"); },
    nights(frm) { frm.trigger("calc_total"); },
    calc_total(frm) {
        const total = (frm.doc.rate_per_night || 0) * (frm.doc.nights || 0);
        frm.set_value("total_amount", total);
        frm.set_value("balance_due", total - (frm.doc.advance_paid || 0));
    },
    advance_paid(frm) {
        frm.set_value("balance_due", (frm.doc.total_amount || 0) - (frm.doc.advance_paid || 0));
    }
});
