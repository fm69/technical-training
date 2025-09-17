from calendar import month
from dataclasses import Field
from email.policy import default

from odoo import _, api, fields, models
from odoo.exceptions import UserError

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
    total_area = fields.Integer(compute="_compute_total_area")
    best_price = fields.Float(compute="_compute_best_price")

    @api.depends("garden_area", "living_area")
    def _compute_total_area(self):
        for property in self:
            property.total_area = property.living_area + property.garden_area

    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for property in self:
            if property.offer_ids:
                property.best_price = max(property.offer_ids.mapped("price"))
            else:
                property.best_price = 0
    @api.onchange("gardens")
    def _onchange_gardens(self):
        if self.gardens:
            self.total_area = 10
            self.garden_orientation = "north"
        else:
            self.garden_area = self.garden_orientation = False

    def action_sell_property(self):
        for property in self:
            if property.state == "cancelled":
                raise UserError(_("Canceled property could not sold!"))
            property.state = "sold"

    def action_cancel_property(self):
        self.state = "cancelled"

    _sql_constraints = [
        ("check_selling_price", "CHECK(selling_price>=0)","The selling price must be positive.")
    ]







