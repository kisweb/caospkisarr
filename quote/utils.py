
from django.core.paginator import (Paginator, EmptyPage, PageNotAnInteger)

from college.models import Quote

from .models import *

def pagination(request, quotes):
    # default_page 
        default_page = 1 

        page = request.GET.get('page', default_page)

        # paginate items

        items_per_page = 5

        paginator = Paginator(quotes, items_per_page)

        try:

            items_page = paginator.page(page)

        except PageNotAnInteger:

            items_page = paginator.page(default_page)

        except EmptyPage:

            items_page = paginator.page(paginator.num_pages) 

        return items_page    



def get_quote(pk):
    """ get quote fonction """

    obj = Quote.objects.get(pk=pk)

    articles = obj.article_set.all()

    context = {
        'obj': obj,
        'articles': articles
    }

    return context