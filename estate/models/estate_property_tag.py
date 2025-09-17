from odoo import fields, models

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Estate Property Tag"

    name = fields.Char(required=True)

    _sql_constraints = [
        ("unique_name", "UNIQUE(name)", "The name should be unique.")
    ]