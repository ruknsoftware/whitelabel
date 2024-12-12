import frappe
import base64
import os

def after_install():
    set_app_name()
    update_login_page_with_attachment()

def set_app_name():
    frappe.db.set_single_value("Website Settings", "app_name", "Kanaan")
    frappe.db.commit()

def create_attachment_and_assign(file_path, file_name, doctype, docname, fieldname):
    try:
        with open(file_path, "rb") as file:
            file_content = base64.b64encode(file.read()).decode("utf-8")

        file_doc = frappe.get_doc({
            "doctype": "File",
            "file_name": file_name,
            "attached_to_doctype": doctype,
            "attached_to_name": docname,
            "attached_to_field": fieldname,
            "content": file_content,
            "decode": 1
        })
        file_doc.insert(ignore_permissions=True)

        # Attach the file URL to the document using doc.save()
        doc = frappe.get_doc(doctype, docname)
        setattr(doc, fieldname, file_doc.file_url)
        doc.save()

        print(f"File {file_name} attached and assigned to {doctype}.{fieldname} successfully.")
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Error Creating and Assigning Attachment")
        print(f"Error: {e}")

def update_login_page_with_attachment():
    try:
        file_path = os.path.join(
            frappe.get_app_path("whitelabel"),
            "public/images/Kanaan_Logo.png"
        )
        file_name = "Kanaan_Logo.png"

        create_attachment_and_assign(
            file_path=file_path,
            file_name=file_name,
            doctype="Website Settings",
            docname="Website Settings",
            fieldname="app_logo"
        )

        frappe.clear_cache()
        print("Updated login page and attached logo successfully.")
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Error Updating Login Page with Attachment")
        print(f"Error: {e}")