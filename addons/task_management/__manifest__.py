{
    'name': 'Task Management',
    'version': '17.0.1.0',
    'summary': 'Simple task management system for learning and portfolio',
    'category': 'Project',
    'author': 'Dado',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/demo_data.xml',
        'views/task_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}