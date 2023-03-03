from .forms import IndexPage
from .models import Urls
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from .helpers import generate_hash, convert_to_utc


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def index(request):
    context = {'form': IndexPage()}
    if is_ajax(request):
        url = request.POST.get('text', None)
        exp_time = request.POST.get('exp_time', None)
        custom = request.POST.get('custom', None)
        if url:
            if custom:
                hash_value = custom
            else:
                hash_value = generate_hash(length=8)

            is_hash_used = Urls.objects.filter(hash_value=hash_value)
            print(len(is_hash_used))

            if len(is_hash_used) > 0:
                return JsonResponse({"result": "duplicate hash"})

            if exp_time:
                expiration_time = convert_to_utc(exp_time)
            else:
                expiration_time = None

            a = Urls(hash_value=hash_value,
                     url=url,
                     count=0,
                     exp_date=expiration_time)

            response = {'result': request.build_absolute_uri() + hash_value}

            a.save()
            return JsonResponse(response)
        else:
            response = {'result': ""}
            return JsonResponse(response)

    return render(request, "index.html", context)


def redirect_view(request, hashing: str):
    mymember = Urls.objects.get(hash_value=hashing)
    mymember.count += 1
    mymember.save()
    return HttpResponseRedirect(mymember.url)
