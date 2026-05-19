import frappe

def run():
    """
    Fix legacy app_name references from the old 'hospitality_leisure' package
    name to the current 'hospitality_erp' name in the Module Def table.
    """
    count = frappe.db.sql(
        """UPDATE `tabModule Def`
           SET app_name = 'hospitality_erp'
           WHERE app_name = 'hospitality_leisure'"""
    )
    frappe.db.commit()

    rows = frappe.db.sql(
        "SELECT name, app_name FROM `tabModule Def` WHERE app_name = 'hospitality_erp'",
        as_dict=True
    )

    print(f"Fixed {len(rows)} module(s) now pointing to hospitality_erp:")
    for r in rows:
        print(f"  - {r['name']}")

    print("Done. Run 'bench --site <site> migrate' to continue.")
