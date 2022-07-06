from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def pg_records(request, list, num):
    paginator = Paginator(list, num)

    page = request.GET.get('page')

    try:
        page_object = paginator.page(page)
    except PageNotAnInteger:
        # if page parameter in the query string is not available, return the first page
        page_object = paginator.page(1)
    except EmptyPage:
        # if the value of the page parameter exceeds num_pages then return the last page
        page_object = paginator.page(paginator.num_pages)

    return page_object
