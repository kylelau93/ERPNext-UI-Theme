from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Desk",
			"label": _("Tools"),
			"color": "#183A60",
			# "reverse": 1,
			"icon": "octicon octicon-calendar",
			"type": "module"
		},
		{
			"module_name": "File Manager",
			"color": "#183A60",
			"doctype": "File",
			"icon": "octicon octicon-file-directory",
			"label": _("File Manager"),
			"link": "List/File",
			"type": "list"
		},
		{
			"module_name": "Website",
			"color": "#183A60",
			"icon": "octicon octicon-globe",
			"type": "module"
		},
		{
			"module_name": "Setup",
			"color": "#183A60",
			# "reverse": 1,
			"icon": "octicon octicon-settings",
			"type": "module"
		},
		{
			"module_name": "Core",
			"label": _("Developer"),
			"color": "#183A60",
			"icon": "icon-cog",
			"icon": "octicon octicon-circuit-board",
			"type": "module",
			"system_manager": 1
		}
	]
