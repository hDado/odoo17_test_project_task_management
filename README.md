# Odoo17 Portfolio — Project 1: Task Management

This repository contains Odoo development portfolio work. Current focus: Project 1 — Task Management.

Progress
- Module scaffolded: `addons/task_management`
- Models: `task.task`, `task.category`
- Views: Form, Tree, Kanban (`views/task_views.xml`)
- Security: `security/ir.model.access.csv`
- Demo data: `data/demo_data.xml` (sample categories & tasks)
- Unit tests: `tests/test_task.py`
- Docs: `docs/project1_impl.md`, `docs/tutorial_actions.md`, `docs/odoo_mindmap.svg`, `docs/projects_index.md`
- Todo: finalize other portfolio projects in separate branches/repos

How to run locally
```bash
# from repository root
docker compose down -v
docker compose up -d
# Open Odoo at http://localhost:8070 -> Update Apps List -> Install "Task Management"
```

Repository: https://github.com/hDado/odoo17_test_project_task_management

If you want me to create Project 2 scaffold or add CI (GitHub Actions), tell me the project idea and branch name and I'll create it.