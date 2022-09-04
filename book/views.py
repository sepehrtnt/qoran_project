from django.shortcuts import render
from .models import Verses
from django.db.models import Q


def index(request):
    if request.method == 'POST':
        page = request.POST['page']
        number_aye = request.POST['number_aye']
        topic = request.POST['topic']
        try:
            print('*' * 10)
            # data = Verses.objects.raw(
            #     '''SELECT
            #         *
            #     FROM
            #         book_verses
            #     WHERE
            #         page = %s
            #         and number_aye = %s
            #         and topic = %s  ''', [page, number_aye, topic])[0]
            # return render(request, 'book_search.html',
            #               {
            #                   'text': data.text
            #               })
            data = Verses.objects.all().filter(page=page, number_aye=number_aye).get()
            # data = Verses.objects.get(page=page, number_aye=number_aye, topic=topic)
            print('1' * 10)
            print(data.text)
            return render(request, 'book_search.html',
                          {
                              'text': data.text
                          })
        except:
            return render(request, 'book_search.html',
                          {
                              'text': 'چیزی پیدا نشد لطفا دوباره سرچ کنید...'
                          })

    data = Verses.objects.all().filter(page='2')
    return render(request, 'book_search.html',
                  {
                      'text': data.text
                  })
