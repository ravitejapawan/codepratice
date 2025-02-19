from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.urls import reverse
from .models import TextEntry, DeletedTextEntry
from .forms import TextEntryForm

def home(request):
    """Handles form submissions and displays saved text."""
    if request.method == 'POST':
        form = TextEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = TextEntryForm()
    texts = TextEntry.objects.order_by('-created_at')
    return render(request, 'textapp/home.html', {'form': form, 'texts': texts})

@login_required
@require_POST  # Only allow POST requests
def delete_text(request, id):
    """Handles deletion of a text entry by moving it to DeletedTextEntry."""
    text_entry = get_object_or_404(TextEntry, id=id)

    # Move to deleted entries before deleting
    DeletedTextEntry.objects.create(
        original_id=text_entry.id,  # Preserve original ID
        text=text_entry.text,
        deleted_by=request.user
    )
    text_entry.delete()
    
    return JsonResponse({'status': 'success'})

@login_required
def deleted_texts(request):
    """Allows superusers to view deleted texts."""
    if not request.user.is_superuser:
        return redirect('home')

    deleted_texts = DeletedTextEntry.objects.order_by('-deleted_at')
    return render(request, 'textapp/deleted_texts.html', {'deleted_texts': deleted_texts})
