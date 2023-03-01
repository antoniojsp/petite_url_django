from .forms import IndexPage
from .models import Urls
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from .helpers import generate_hash


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def index(request):
    context = {'form': IndexPage()}

    if is_ajax(request):
        data = request.POST.get('text', None)

        if data:
            response = {'msg': data}
            hash_value = generate_hash(length=8)
            a = Urls(hash_value =hash_value, url=data, count=0)
            a.save()
            return JsonResponse(response)
        else:
            response = {'msg': ""}
            return JsonResponse(response)

    return render(request, "index.html", context)


def redirect_view(request, hash):
    mymember = Urls.objects.get(hash_value=hash)
    context = {'form': IndexPage()}

    return HttpResponseRedirect(mymember.url)
