from django.shortcuts import render
from .models import Verses


def index(request):
    data = Verses.objects.get(page=2)
    return render(request, 'book_search.html',
                  {
                      'text': data.text
                  })
