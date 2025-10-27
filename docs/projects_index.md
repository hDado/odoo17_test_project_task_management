# Projects Index

This repository contains one or more Odoo portfolio projects. Use this index to find each project's location, status, and how to run it locally.

## Project 1 — Task Management
- Path: `addons/task_management`
- Status: Completed (module scaffold, demo data, Kanban, unit tests, docs, mind map)
- Key files:
  - `addons/task_management/models/task.py`
  - `addons/task_management/views/task_views.xml`
  - `addons/task_management/data/demo_data.xml`
  - `addons/task_management/tests/test_task.py`
  - `docs/project1_impl.md`
  - `docs/tutorial_actions.md`
  - `docs/odoo_mindmap.svg`
- How to run locally:

```bash
# from repository root
# 1. Start the stack
docker compose down -v
docker compose up -d

# 2. Update apps and install module in Odoo:
# Open http://localhost:8070 -> Activate Developer Mode -> Apps -> Update Apps List -> install "Task Management"
```

- Notes:
  - Demo data creates sample categories and tasks on install.
  - Tests can be run from inside the web container (see `docs/tutorial_actions.md`).


---

## Next project
When you're ready, create a new branch or repository for Project 2 and I can scaffold it for you. Recommended branch name pattern: `project2-<brief-name>` or `project2-final` when finished.
