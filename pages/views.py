from django.shortcuts import render
from . models import Page


# return HttpResponse("<h1>The Meandco Homepage</h1>")


def index(request, pagename):
        pagename='/'+ pagename
        pg=Page.objects.get(permalink=pagename)
        context = {
                'title': pg.title,
                'content': pg.bodytext,
                'last_updated': pg.updatedate,
                'page_list':Page.objects.all(),
        }
        #assert False
        return render(request, 'pages/page.html', context)

# Create your views here.
