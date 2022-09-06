from django.shortcuts import render
from .models import Verses


def index(request):
    if request.method == 'POST':
        page = request.POST['page']
        number_aye = request.POST['number_aye']
        topic = request.POST['topic']
        try:
            data = Verses.objects.filter(page=page,
                                         number_aye=number_aye,
                                         topic__icontains=topic).get()
            return render(request, 'blog/post/book_search.html',
                          {
                              'text': data.text
                          })
        except:
            return render(request, 'blog/post/book_search.html',
                          {
                              'text': 'لطفا همه فیلد ها را پر کنید...'
                          })

    data = Verses.objects.get(page='1')
    return render(request, 'blog/post/book_search.html',
                  {
                      'text': data.text
                  })
