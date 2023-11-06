# Copyright {{license_years}} Laetitia Da Costa ({{company}})
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "{{name}}",
    "version": "{{version}}",
    "author": "Elabore",
    "website": "https://elabore.coop",
    "maintainer": "Laetitia Da Costa",
    "license": "AGPL-3",
    "category": "{{category}}",
    "summary": "{{summary}}",
    # any module necessary for this one to work correctly
    "depends": [
        "base",
    ],
    "qweb": [],
    "external_dependencies": {
        "python": [],
    },
    # always loaded
    "data": [
        # "security/security.xml",
        # "security/ir.model.access.csv",
        # "views/menu.xml",
        # "data/data.xml",
    ],
    # only loaded in demonstration mode
    "demo": [],
    "js": [],
    "css": [],
    "installable": True,
    # Install this module automatically if all dependency have been previously
    # and independently installed.  Used for synergetic or glue modules.
    "auto_install": False,
    "application": False,
}