from django.http import HttpResponseBadRequest, JsonResponse

from django.template import loader
from .forms import IndexPage
from django.shortcuts import render

from django.shortcuts import render
from django.http import JsonResponse


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def index(request):
    context = {'form': IndexPage()}
    print("html")
    # template = loader.get_template('index.html')

    if is_ajax(request):
        print("ajax")
        data = request.POST.get('text', None)
        print(data)

        if data:
            response = {'msg': data}
            return JsonResponse(response)
        else:
            response = {'msg': ""}
            return JsonResponse(response)

    return render(request, "index.html", context)


# def submit(request):
#



