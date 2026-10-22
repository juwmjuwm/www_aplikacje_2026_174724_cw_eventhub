from django.http import HttpResponse

def welcome_view(request):
    return HttpResponse("Witaj w platformie EventHub – systemie obsługi wydarzeń i biletów!")


def about_view(request):
    return HttpResponse(
        "EventHub umożliwia tworzenie wydarzeń i rezerwacje biletów."
    )
