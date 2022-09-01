from django.shortcuts import render
from .models import Verses


def index(request):
    if request.method == 'POST':
        page = request.POST['page']
        number_aye = request.POST['number_aye']
        topic = request.POST['topic']
        try:
            data = Verses.objects.raw(
                '''SELECT
                    * 
                FROM
                    book_verses 
                WHERE
                    page = %s 
                    and number_aye = %s 
                    and topic = %s  ''', [page, number_aye, topic])[0]
            return render(request, 'book_search.html',
                          {
                              'text': data.text
                          })
        except:
            return render(request, 'book_search.html',
                          {
                              'text': 'چیزی پیدا نشد لطفا دوباره سرچ کنید...'
                          })

    data = Verses.objects.raw('select * from book_verses where page = 1')[0]
    return render(request, 'book_search.html',
                  {
                      'text': data.text
                  })
