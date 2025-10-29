from django import forms
from .models import StickyNote

class StickyNoteForm(forms.ModelForm):
    class Meta:
        model = StickyNote
        fields = ['title', 'content', 'color']
        widgets = {
            'content': forms.Textarea(attrs={'rows':4, 'cols':40}),
        }
