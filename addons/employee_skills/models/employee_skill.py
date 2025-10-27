from odoo import models, fields, api

class EmployeeSkill(models.Model):
    _name = 'employee.skill'
    _description = 'Employee Skill'

    name = fields.Char(string='Skill Name', required=True)
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    level_id = fields.Many2one('skill.level', string='Skill Level', required=True)
    description = fields.Text(string='Notes')
    acquisition_date = fields.Date(string='Acquisition Date', default=fields.Date.today)

    @api.depends('name', 'level_id')
    def name_get(self):
        result = []
        for skill in self:
            name = f"{skill.name} - {skill.level_id.name}"
            result.append((skill.id, name))
        return result