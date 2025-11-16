from django.test import TestCase
from django.urls import reverse
from notes.models import Note

class NotesViewTests(TestCase):
    def test_list_and_detail(self):
        n = Note.objects.create(title='T1', content='C1')
        res = self.client.get(reverse('notes:list'))
        assert res.status_code == 200
        res2 = self.client.get(reverse('notes:detail', args=[n.pk]))
        assert res2.status_code == 200
