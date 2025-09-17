from calendar import month
from dataclasses import Field
from email.policy import default

from odoo import fields, models

class EstateProperty(models.Model):
    _name = "estate_property"
    _description = "Estate Property"

    name = fields.Char(required=True)
    description =  fields.Text()
    date_available = fields.Date(copy=False, default=lambda self: fields.Date.add(fields.Date.today(),month=9))
    expected_price = fields.Float()
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer()
    facades = fields.Integer()
    gardens = fields.Boolean()
    garage = fields.Boolean()
    postcode = fields.Char()
    living_area = fields.Float()
    garden_orientation =  fields.Selection([("north", "North"), ("south", "South"), ("east", "East"), ("west", "West")])
    garden_area = fields.Integer()
    active = fields.Boolean(default=True)
    state = fields.Selection(
        selection=[
            ("new", "New"),("offer_received", "Offer received"),("offer_accepted", "Offer accepted"),("sold", "Sold"),("cancelled", "Cancelled")],
        default="new",
        copy=False,
        required=True,
    )
    property_type_id = fields.Many2one("estate.property.type")
    salesperson_id = fields.Many2one("res.users", default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", copy=False)
    tag_id = fields.Many2one("estate.property.tag")
    offer_ids = fields.One2many("estate.property.offer","property_id")






