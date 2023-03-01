from .forms import IndexPage
from .models import Urls
from django.shortcuts import render
from django.http import JsonResponse


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def index(request):
    context = {'form': IndexPage()}

    if is_ajax(request):
        data = request.POST.get('text', None)

        if data:
            response = {'msg': data}

            a = IndexPage()
            a.url = data
            a.save()
            return JsonResponse(response)
        else:
            response = {'msg': ""}
            return JsonResponse(response)

    return render(request, "index.html", context)



