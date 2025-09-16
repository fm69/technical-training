from calendar import month
from dataclasses import Field

from odoo import fields, models

class EstateProperty(models.Model):
    _name = "estate_property"
    _description = "Estate Poperty"

    name = fields.Char(required=True)
    description =  fields.Text()
    date_available = fields.Date(copy=False, default=lambda self: fields.Date.add(fields.Date.today(),month=3))
    expected_price = fields.Float()
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer()
    gardens = fields.Boolean()
    postcode = fields.Char()
    living_area = fields.Float()
    garden_orientation =  fields.Selection([("north", "North"), ("south", "South"), ("east", "East"), ("west", "West")])
    active = fields.Boolean(default=True)
    state = fields.Selection(
        selection=[
            ("new", "New"),("offer_received", "Offer received"),("offer_accepted", "Offer accepted"),("sold", "Sold"),("cancelled", "Cancelled")],
        default="new",
        copy=False,
        required=True,
    )


