# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Stock Delivery Request Report",
    "version": "12.0.1.1.1",
    "author": "Quartile Limited",
    "website": "https://www.quartile.co",
    "category": "Stock",
    "license": "AGPL-3",
    "depends": [
        "stock_picking_batch",
        "delivery",
        "report_py3o",
        "stock_picking_delivery_due_date",
    ],
    "data": [
        "report/stock_picking_report.xml",
        "views/delivery_views.xml",
        "views/stock_picking_views.xml",
        "views/stock_picking_batch_views.xml",
        "wizard/stock_picking_report_wizard_views.xml",
    ],
    "installable": True,
}
