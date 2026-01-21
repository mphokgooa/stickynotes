from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.NoteListView.as_view(), name='list'),
    path('note/<int:pk>/', views.NoteDetailView.as_view(), name='detail'),
    path('note/add/', views.NoteCreateView.as_view(), name='add'),
    path('note/<int:pk>/edit/', views.NoteUpdateView.as_view(), name='edit'),
    path('note/<int:pk>/delete/', views.NoteDeleteView.as_view(), name='delete'),
]
