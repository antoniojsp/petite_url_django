from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from .models import Urls
from .forms import IndexPage
from .helpers import generate_hash, get_title, is_expired


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def index(request):
    context = {'form': IndexPage()}

    if is_ajax(request):
        url = request.POST.get('text', None)
        exp_time = request.POST.get('exp_time', None)
        custom = request.POST.get('custom', None)
        if is_ajax(request):
            # TODO: check "custom" to have onlue [a-z0-9] characters.
            hash_value = custom if custom else generate_hash(length=8)
            expiration_time = exp_time if exp_time else None

            is_hash_taken = Urls.objects.filter(hash_value=hash_value)

            # for now, we will enforce a 8 char length hash value. Client checks for that but we add extra protection.
            if len(is_hash_taken) > 0 or len(hash_value) != 8:  # TODO change return to a 403 message
                return JsonResponse({"result": "ERROR", "title": "Something went really wrong!"})

            # TODO check that url is valid, alive and healthy (We do this on the server side)
            # get_title() may throw an error if the website is invalid.
            title = get_title(url)

            new_url_entry = Urls(hash_value=hash_value,
                                 url=url,
                                 count=0,
                                 exp_date=expiration_time
                                 )

            response = {'result': request.build_absolute_uri() + hash_value, "title": title}

            new_url_entry.save()
            return JsonResponse(response)

    return render(request, "index.html", context)


def redirect_view(request, hashing: str):

    try:
        mymember = Urls.objects.get(hash_value=hashing)
    except Exception as e:
        print('Exception: {}'.format(e))
        return render(request, "404.html")



    if is_expired(mymember.exp_date):
        return render(request, "404.html")

    mymember.count += 1
    mymember.save()
    return HttpResponseRedirect(mymember.url)


def is_hash_used(request):
    custom_hash = request.POST.get('custom', None)
    is_hash_present = Urls.objects.filter(hash_value=custom_hash)

    exists = len(is_hash_present)
    hash_len = len(custom_hash)

    if exists == 0:
        response = {"valid": True}
    elif hash_len != 8:
        response = {"valid": False}  # check if the length of the custom hash is not 8
    else:  # catch's any other error in custom hash (most of those error are handled by the client)
        response = {"valid": False}
        print("Unexpected error receiving the custom hash.")

    return JsonResponse(response)
