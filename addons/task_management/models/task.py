from odoo import models, fields, api


class TaskCategory(models.Model):
    _name = 'task.category'
    _description = 'Task Category'

    name = fields.Char(string='Category Name', required=True)
    description = fields.Text(string='Description')
    color = fields.Integer(string='Color Index')


class Task(models.Model):
    _name = 'task.task'
    _description = 'Task'
    _order = 'priority desc, id desc'

    name = fields.Char(string='Task Name', required=True)
    description = fields.Text(string='Description')

    user_id = fields.Many2one('res.users', string='Assigned To',
                              default=lambda self: self.env.user)

    date_start = fields.Date(string='Start Date', default=fields.Date.context_today)
    date_end = fields.Date(string='Due Date')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft', tracking=True)

    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Medium'),
        ('2', 'High')
    ], string='Priority', default='1')

    category_id = fields.Many2one('task.category', string='Category')

    color = fields.Integer(string='Color Index')

    active = fields.Boolean(default=True)

    def action_start(self):
        for rec in self:
            rec.state = 'in_progress'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            # If the record is new (not yet saved), don't attempt to write —
            # writing would trigger validation (required fields) and block cancel.
            if not rec.id:
                # nothing to persist; client will simply close the form
                continue
            rec.state = 'cancelled'
        return True
