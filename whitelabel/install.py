import frappe


def set_app_name():
    frappe.db.set_single_value("Website Settings", "app_name", "Kanaan")
    frappe.db.commit()
