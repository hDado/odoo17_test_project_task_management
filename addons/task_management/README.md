# Task Management (learning project)

This simple Odoo module is the first portfolio project. It provides basic task management functionality to help you remember Odoo development concepts.

Installation
1. Place the `task_management` folder into your Odoo addons directory (in this workspace it's already in `addons/`).
2. Restart Odoo (or the Docker container):

```bash
# from project root
docker compose down -v
docker compose up -d
```

3. In Odoo: Settings -> Activate Developer Mode -> Apps -> Update Apps List -> Search "Task Management" -> Install.

Quick test
- Create a few categories (Task Management -> Categories)
- Create tasks (Task Management -> Tasks)
- Test workflow buttons in the task form: Start, Mark as Done, Cancel

Cancel behavior note
- The Cancel button is configured to avoid forcing a save of the record before running. That means you can open a new task form, leave required fields blank (like the name) and press Cancel to discard it without being forced to fill the name first.

Extending the module
- Add Kanban (already included), automated reminders (cron), or comments (mail.thread) as next steps.

Troubleshooting
- If you don't see the module: make sure the `addons` path is mounted in your Odoo container and restart Odoo.
- Check Odoo logs for errors: `docker compose logs web --tail=200`.
