from odoo.tests.common import TransactionCase


class TestTask(TransactionCase):
    def setUp(self):
        super().setUp()
        self.Task = self.env['task.task']
        self.Category = self.env['task.category']
        self.cat = self.Category.create({'name': 'Test Category'})
        self.task = self.Task.create({
            'name': 'Test Task',
            'category_id': self.cat.id,
        })

    def test_default_state(self):
        # Newly created tasks should start in draft
        self.assertEqual(self.task.state, 'draft')

    def test_transitions_start_done(self):
        # Start -> In Progress
        self.task.action_start()
        self.assertEqual(self.task.state, 'in_progress')
        # Done -> Done
        self.task.action_done()
        self.assertEqual(self.task.state, 'done')

    def test_cancel_sets_cancelled(self):
        # Cancel from a saved record sets state to cancelled
        t2 = self.Task.create({'name': 'To be cancelled', 'category_id': self.cat.id})
        t2.action_cancel()
        self.assertEqual(t2.state, 'cancelled')
