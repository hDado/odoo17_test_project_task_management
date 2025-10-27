# Project 1 — Tutorial: how actions and files interact (overview)

This short tutorial explains how the pieces of the `task_management` module communicate when a user interacts with the UI (for example clicking a button), and which files you should edit to change each behavior.

1) High-level flow when clicking a form button (e.g. "Start" / "Cancel")

- Browser (web client) renders the form view (from XML view file).
  - File: `addons/task_management/views/task_views.xml` — defines the form, header buttons, fields.

- When you click a button with `type="object"`, the web client sends an RPC call to the server that invokes the corresponding Python method on the model.
  - Example button attribute: `<button name="action_start" type="object" .../>`
  - The web client issues a JSON-RPC call to `model: task.task, method: action_start`.

- Server side: Odoo routes the RPC to the model method implementation.
  - File: `addons/task_management/models/task.py` — contains `action_start`, `action_done`, `action_cancel`.
  - The method executes (writes state, performs checks, etc.).

- ORM translates Python operations (create/write/search/unlink) into SQL statements executed on PostgreSQL.
  - Database is managed by the `db` container in Docker setups; data lives in Postgres (`PGDATA`/volume).

- Response returns to web client; the form/tree/kanban updates accordingly.

2) Where to modify behavior

- Change UI layout or buttons
  - Edit `views/task_views.xml`. Add attributes like `save="0"` on a button to avoid client-side auto-save, or `invisible="..."` to show/hide.

- Change business logic
  - Edit `models/task.py`. Button logic and business rules live here. Use `@api.model`, `@api.depends`, `@api.onchange` where appropriate.

- Add sample/demo data
  - `data/demo_data.xml` — records created at install time via `__manifest__` `data` key.

- Manage access rights
  - `security/ir.model.access.csv` — create basic CRUD permissions for models.
  - For complex record-level rules, create `security/ir.rule` entries (XML).

- Tests
  - `addons/task_management/tests/test_task.py` — TransactionCase tests run by Odoo test runner.
  - Tests validate model behavior without UI.

3) Practical tips / mapping of common tasks to files

- Add a new field -> `models/task.py` + update `views/task_views.xml` to show it.
- Change how a button behaves -> update `views/task_views.xml` (attributes) and `models/task.py` (method implementation).
- Preload records for demos -> `data/demo_data.xml` and add to manifest.
- Protect actions -> update `security/ir.model.access.csv` and/or add record rules.
- Add reports -> `reports/your_report.xml` + templates (QWeb)

4) Debugging steps when things fail

- Check Odoo logs inside container: `docker compose logs web --tail=200` or `docker compose exec web tail -n 200 /var/log/odoo/odoo.log` (paths vary by image).
- Use `docker compose exec web bash` to open a shell inside the container and inspect files, run `python` shell or `odoo-bin` with `-c` for advanced debugging.
- Use the web developer tools (activate developer mode) to inspect view XML and RPC calls.

5) How the `Cancel` change works (why you saw the required-name issue)

- Before: the Cancel button caused the client to try to save the record before calling the method, so the server required the `name` field and returned validation errors. This is a client-side save triggered by the form widget.
- Fixes applied:
  - In `views/task_views.xml`, the Cancel button has `save="0"` so the client won't attempt to auto-save before calling the RPC.
  - In `models/task.py`, `action_cancel` was made resilient: it checks `if not rec.id:` and avoids writing to unsaved records (writing would trigger validation). This avoids server-side validation blocking cancel on new forms.

6) Running tests locally

- To run the test file locally with your Docker setup, you can run the Odoo test runner pointing to the module. A simple way is to exec a shell into the web container and run the Odoo command that runs tests for the module. Example (from project root):

```bash
# open a shell in the running web container
docker compose exec web bash

# inside the container - run tests for the module
# (adjust the odoo binary path if different in your image)
odoo -c /etc/odoo/odoo.conf --test-enable --stop-after-init -i task_management
```

This will install `task_management` in a transient DB and run tests (the output shows successes/failures).

---

If you want, I can also:
- Add a small note in the module README linking to this tutorial (I can update `README.md`).
- Add a GitHub Actions CI file that spins up a Postgres service and runs only the module's tests inside a containerized Odoo image (I can provide a best-effort workflow). 

Which of those would you like next?