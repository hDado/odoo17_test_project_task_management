{
    'name': 'Employee Skills',
    'version': '17.0.1.0',
    'category': 'Human Resources',
    'summary': 'Manage employee skills and competencies',
    'description': """
        This module allows you to:
        * Track employee skills
        * Add skill levels
        * View skills in tree and form views
    """,
    'author': 'Your Name',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_skill_views.xml',
        'views/skill_level_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}