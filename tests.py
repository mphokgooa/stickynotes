from django.test import TestCase
from .models import StickyNote
from django.contrib.auth.models import User

class StickyNoteModelTest(TestCase):
    def test_create_note(self):
        user = User.objects.create_user(username='testuser', password='pass')
        note = StickyNote.objects.create(author=user, title='Test', content='hello', color='yellow')
        self.assertEqual(str(note), 'Test (testuser)')
