"""Przykładowe zapytania ORM z laboratorium 2.

Uruchom: python -m events.orm_queries <ID_opublikowanego_wydarzenia>
"""

from decimal import Decimal


def run_queries(event_id):
    from events.models import Event

    # 1. Opublikowane wydarzenia w kolejności chronologicznej.
    published_events = Event.objects.filter(is_published=True).order_by('date')
    for event in published_events:
        print(event)

    # 2. Wydarzenia z limitem co najmniej 50 miejsc.
    large_events = Event.objects.filter(capacity__gte=50)
    for event in large_events:
        print(event)

    # 3. Łączna liczba darmowych wydarzeń.
    free_events_count = Event.objects.filter(price=Decimal('0.00')).count()
    print(f"Liczba darmowych wydarzeń: {free_events_count}")

    # 4. Zmiana statusu wskazanego, opublikowanego wydarzenia.
    event = Event.objects.get(pk=event_id, is_published=True)
    event.is_published = False
    event.save()
    print(f"Wycofano publikację: {event}")


if __name__ == '__main__':
    import argparse
    import os

    import django

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('event_id', type=int, help='ID opublikowanego wydarzenia')
    args = parser.parse_args()

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eventhub.settings')
    django.setup()
    run_queries(args.event_id)
