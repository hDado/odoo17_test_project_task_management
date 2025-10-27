from odoo import models, fields, api

class SkillLevel(models.Model):
    _name = 'skill.level'
    _description = 'Skill Level'

    name = fields.Char(string='Level Name', required=True)
    value = fields.Integer(string='Level Value', required=True)
    description = fields.Text(string='Description')

    _sql_constraints = [
        ('unique_value', 'unique(value)', 'Level value must be unique!')
    ]