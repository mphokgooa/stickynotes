from django.test import TestCase
from django.urls import reverse
from notes.models import Note

class NoteViewsTest(TestCase):

    def setUp(self):
        self.note = Note.objects.create(
            title="Existing Note",
            content="Existing content"
        )

    def test_note_list_view(self):
        response = self.client.get(reverse('notes:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Existing Note")

    def test_note_detail_view(self):
        response = self.client.get(
            reverse('notes:detail', args=[self.note.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.note.title)

    def test_note_create_view(self):
        response = self.client.post(
            reverse('notes:add'),
            {
                'title': 'New Note',
                'content': 'New content'
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Note.objects.filter(title='New Note').exists()
        )

    def test_note_update_view(self):
        response = self.client.post(
            reverse('notes:edit', args=[self.note.id]),
            {
                'title': 'Updated Note',
                'content': 'Updated content'
            }
        )
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Note')

    def test_note_delete_view(self):
        response = self.client.post(
            reverse('notes:delete', args=[self.note.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            Note.objects.filter(id=self.note.id).exists()
        )
