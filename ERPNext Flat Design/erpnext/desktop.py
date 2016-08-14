from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Accounts",
			"color": "#183A60",
			"icon": "octicon octicon-repo",
			"label": _("Accounts"),
			"type": "module"
		},
		{
			"module_name": "CRM",
			"color": "#183A60",
			"icon": "octicon octicon-broadcast",
			"type": "module"
		},
		{
			"module_name": "Selling",
			"color": "#183A60",
			"icon": "icon-tag",
			"icon": "octicon octicon-tag",
			"type": "module"
		},
		{
			"module_name": "Buying",
			"color": "#183A60",
			"icon": "icon-shopping-cart",
			"icon": "octicon octicon-briefcase",
			"type": "module"
		},
		{
			"module_name": "HR",
			"color": "#183A60",
			"icon": "icon-group",
			"icon": "octicon octicon-organization",
			"label": _("Human Resources"),
			"type": "module"
		},
		{
			"module_name": "Manufacturing",
			"color": "#183A60",
			"icon": "icon-cogs",
			"icon": "octicon octicon-tools",
			"type": "module"
		},
		{
			"module_name": "POS",
			"color": "#183A60",
			"icon": "icon-th",
			"icon": "octicon octicon-credit-card",
			"type": "page",
			"link": "pos",
			"label": _("POS")
		},
		{
			"module_name": "Projects",
			"color": "#183A60",
			"icon": "icon-puzzle-piece",
			"icon": "octicon octicon-rocket",
			"type": "module"
		},
		{
			"module_name": "Stock",
			"color": "#183A60",
			"icon": "icon-truck",
			"icon": "octicon octicon-package",
			"type": "module"
		},
		{
			"module_name": "Support",
			"color": "#183A60",
			"icon": "icon-phone",
			"icon": "octicon octicon-issue-opened",
			"type": "module"
		},
		{
			"module_name": "Learn",
			"color": "#183A60",
			"icon": "octicon octicon-device-camera-video",
			"type": "module",
			"is_help": True,
			"label": _("Learn")
		}
	]
