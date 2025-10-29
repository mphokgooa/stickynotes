from django.shortcuts import render, get_object_or_404, redirect
from .models import StickyNote
from .forms import StickyNoteForm
from django.contrib.auth.decorators import login_required

def index(request):
    notes = StickyNote.objects.all().order_by('-updated_at')
    return render(request, 'stickynotes_app/index.html', {'notes': notes})

@login_required
def create_note(request):
    if request.method == 'POST':
        form = StickyNoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect('index')
    else:
        form = StickyNoteForm()
    return render(request, 'stickynotes_app/form.html', {'form': form, 'action': 'Create'})

@login_required
def edit_note(request, pk):
    note = get_object_or_404(StickyNote, pk=pk, author=request.user)
    if request.method == 'POST':
        form = StickyNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StickyNoteForm(instance=note)
    return render(request, 'stickynotes_app/form.html', {'form': form, 'action': 'Edit'})

@login_required
def delete_note(request, pk):
    note = get_object_or_404(StickyNote, pk=pk, author=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('index')
    return render(request, 'stickynotes_app/confirm_delete.html', {'note': note})
