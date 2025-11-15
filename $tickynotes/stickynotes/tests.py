from django.test import TestCase
from django.urls import reverse
from .models import Note

class NoteCRUDTests(TestCase):
    """Test suite for all CRUD operations in StickyNotes."""

    def setUp(self):
        # Create a sample note for use in the tests
        self.note = Note.objects.create(
            title="Test Note",
            content="Initial content for testing."
        )

    def test_create_note(self):
        """Test that a new note can be created."""
        response = self.client.post(reverse('note_create'), {
            'title': 'New Note',
            'content': 'This is a new note.'
        })
        self.assertEqual(response.status_code, 302)  # redirect expected
        self.assertTrue(Note.objects.filter(title='New Note').exists())

    def test_read_notes(self):
        """Test that the note list page loads and displays the note."""
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.note.title)

    def test_update_note(self):
        """Test that an existing note can be updated."""
        response = self.client.post(reverse('note_update', args=[self.note.id]), {
            'title': 'Updated Note',
            'content': 'This note has been updated.'
        })
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Note')
        self.assertEqual(self.note.content, 'This note has been updated.')

    def test_delete_note(self):
        """Test that an existing note can be deleted."""
        response = self.client.post(reverse('note_delete', args=[self.note.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Note.objects.filter(id=self.note.id).exists())
