from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Category, Event


def event_list(request):
    """Display published events, optionally filtered by title."""
    events = Event.objects.filter(is_published=True).select_related('category', 'organizer')
    q = request.GET.get('q')
    if q:
        events = events.filter(title__icontains=q)

    return render(request, 'events/event_list.html', {
        'events': events,
        'categories': Category.objects.all(),
        'q': q,
    })


def event_detail(request, slug):
    """Display a published event and up to three events in its category."""
    event = get_object_or_404(
        Event.objects.select_related('category', 'organizer'),
        slug=slug,
        is_published=True,
    )
    related_events = (
        Event.objects.filter(category=event.category, is_published=True)
        .exclude(id=event.id)
        .select_related('category', 'organizer')[:3]
    )
    return render(request, 'events/event_detail.html', {
        'event': event,
        'related_events': related_events,
    })


def events_by_category(request, category_slug):
    """Display published events belonging to one category."""
    category = get_object_or_404(Category, slug=category_slug)
    events = category.events.filter(is_published=True).select_related('category', 'organizer')
    return render(request, 'events/event_list.html', {
        'events': events,
        'categories': Category.objects.all(),
        'current_category': category,
    })


def about_view(request):
    return HttpResponse(
        "EventHub umożliwia tworzenie wydarzeń i rezerwacje biletów."
    )
