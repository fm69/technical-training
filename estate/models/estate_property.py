from odoo import fields, models

class EstateProperty(models.Model):
    _name: "estate_property"
    _description: "Estate Poperty"

    name = fields.Char(required=True)
    description =  fields.Text()
    date_available = fields.Date()
    expected_price = fields.Float()
    bedrooms = fields.Integer()
    gardens = fields.Boolean()
    garden_orientation =  fields.Selection([("north", "North"), ("south", "South"), ("east", "East"), ("west", "West")])


