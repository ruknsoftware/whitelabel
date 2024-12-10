# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version
from . import __logo__ as app_logo


app_name = "whitelabel"
app_title = "Whitelabel"
app_publisher = "Bhavesh Maheshwari"
app_description = "ERPNext Whitelabel"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "maheshwaribhavesh95863@gmail.com"
app_license = "MIT"
app_logo_url = '/assets/whitelabel/images/Kanaan_Logo.png'

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/whitelabel/css/whitelabel_app.css"
app_include_js = "/assets/whitelabel/js/whitelabel.js"

# include js, css files in header of web template
web_include_css = "/assets/whitelabel/css/whitelabel_web.css"
# web_include_js = "/assets/whitelabel/js/whitelabel.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "whitelabel.utils.get_home_page"

website_context = {
	"favicon": app_logo or "/assets/whitelabel/images/Kanaan_Logo.png",
	"splash_image": app_logo or "/assets/whitelabel/images/Kanaan_Logo.png"
}
after_migrate = ['whitelabel.api.whitelabel_patch']

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "whitelabel.install.before_install"
after_install = "whitelabel.install.set_app_name"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "whitelabel.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"whitelabel.tasks.all"
# 	],
# 	"daily": [
# 		"whitelabel.tasks.daily"
# 	],
# 	"hourly": [
# 		"whitelabel.tasks.hourly"
# 	],
# 	"weekly": [
# 		"whitelabel.tasks.weekly"
# 	]
# 	"monthly": [
# 		"whitelabel.tasks.monthly"
# 	]
# }

boot_session = "whitelabel.api.boot_session"
# Testing
# -------

# before_tests = "whitelabel.install.before_tests"

fixtures = [
    {"dt": "Custom Field", "filters": [["Translation","source_text","like","%ERPNext%"]]}
]

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "whitelabel.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "whitelabel.task.get_dashboard_data"
# }

# override_whitelisted_methods = {
# 	"frappe.utils.change_log.show_update_popup": "whitelabel.api.ignore_update_popup"
# }

