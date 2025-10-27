# Project 1: Task Management System

## Project Overview
A task management system that allows users to create, assign, and track tasks with different states and priorities.

## Learning Objectives
1. Basic Odoo module structure
2. Model creation and field types
3. Basic views (form, tree, search)
4. Security and access rights
5. Basic workflows with states

## Features
- Task creation and management
- Task assignment to users
- Priority levels
- Task states (draft, in-progress, done, cancelled)
- Task categories
- Due date tracking
- Basic reporting

## Technical Implementation

### 1. Models

#### Task Model
```python
from odoo import models, fields, api

class Task(models.Model):
    _name = 'task.task'
    _description = 'Task'
    _order = 'priority desc, id desc'

    name = fields.Char(string='Task Name', required=True)
    description = fields.Text(string='Description')
    
    user_id = fields.Many2one('res.users', string='Assigned To', 
                             default=lambda self: self.env.user)
    
    date_start = fields.Date(string='Start Date', default=fields.Date.today)
    date_end = fields.Date(string='Due Date')
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft')
    
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Medium'),
        ('2', 'High')
    ], string='Priority', default='1')
    
    category_id = fields.Many2one('task.category', string='Category')
    
    color = fields.Integer(string='Color Index')
    
    active = fields.Boolean(default=True)
```

#### Category Model
```python
class TaskCategory(models.Model):
    _name = 'task.category'
    _description = 'Task Category'

    name = fields.Char(string='Category Name', required=True)
    description = fields.Text(string='Description')
    color = fields.Integer(string='Color Index')
```

### 2. Views

#### Task Tree View
```xml
<record id="view_task_tree" model="ir.ui.view">
    <field name="name">task.task.tree</field>
    <field name="model">task.task</field>
    <field name="arch" type="xml">
        <tree decoration-info="state == 'draft'" 
              decoration-warning="state == 'in_progress'"
              decoration-success="state == 'done'"
              decoration-danger="state == 'cancelled'">
            <field name="name"/>
            <field name="user_id"/>
            <field name="category_id"/>
            <field name="priority"/>
            <field name="date_end"/>
            <field name="state"/>
        </tree>
    </field>
</record>
```

#### Task Form View
```xml
<record id="view_task_form" model="ir.ui.view">
    <field name="name">task.task.form</field>
    <field name="model">task.task</field>
    <field name="arch" type="xml">
        <form>
            <header>
                <button name="action_start" string="Start" type="object"
                        states="draft" class="oe_highlight"/>
                <button name="action_done" string="Mark as Done" type="object"
                        states="in_progress" class="oe_highlight"/>
                <button name="action_cancel" string="Cancel" type="object"
                        states="draft,in_progress"/>
                <field name="state" widget="statusbar"
                       statusbar_visible="draft,in_progress,done"/>
            </header>
            <sheet>
                <div class="oe_title">
                    <h1>
                        <field name="name" placeholder="Task Name"/>
                    </h1>
                </div>
                <group>
                    <group>
                        <field name="user_id"/>
                        <field name="category_id"/>
                        <field name="priority" widget="priority"/>
                    </group>
                    <group>
                        <field name="date_start"/>
                        <field name="date_end"/>
                        <field name="active" invisible="1"/>
                    </group>
                </group>
                <notebook>
                    <page string="Description">
                        <field name="description"/>
                    </page>
                </notebook>
            </sheet>
        </form>
    </field>
</record>
```

### 3. Security
```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_task_user,task.task.user,model_task_task,base.group_user,1,1,1,1
access_task_category_user,task.category.user,model_task_category,base.group_user,1,1,1,1
```

### 4. State Management Methods
```python
@api.model
def action_start(self):
    self.write({'state': 'in_progress'})

def action_done(self):
    self.write({'state': 'done'})

def action_cancel(self):
    self.write({'state': 'cancelled'})
```

## Development Steps

1. Create module structure:
```bash
odoo_portfolio/
└── addons/
    └── task_management/
        ├── __init__.py
        ├── __manifest__.py
        ├── models/
        │   ├── __init__.py
        │   └── task.py
        ├── security/
        │   └── ir.model.access.csv
        └── views/
            └── task_views.xml
```

2. Implement models
3. Create views
4. Set up security
5. Add business logic
6. Test functionality

## Testing Checklist

1. Module Installation
- [ ] Module appears in apps list
- [ ] Installation completes without errors
- [ ] Menu items are created

2. Basic Operations
- [ ] Create new task
- [ ] Assign to users
- [ ] Change states
- [ ] Set priorities
- [ ] Add categories

3. Views
- [ ] Tree view shows all fields
- [ ] Form view works correctly
- [ ] State changes reflect in UI
- [ ] Priority widget works

4. Security
- [ ] Users can access tasks
- [ ] Proper access rights

## Common Issues and Solutions

1. Module Not Visible
- Check manifest file
- Update apps list
- Check addons path

2. Security Errors
- Verify CSV format
- Check model names
- Update access rights

3. State Transitions
- Verify button states
- Check method names
- Test transitions

## Next Steps

After completing this project, you should be able to:
1. Create basic Odoo modules
2. Work with models and fields
3. Create and customize views
4. Implement basic workflows
5. Handle security