import random
import string
import datetime
from datetime import date
from datetime import timedelta

from django.shortcuts import redirect
from django.http import HttpResponse
from django.urls import reverse

from .models import OneTimeLinkModel


def randomString(stringLength):
    """ Generate a random string of fixed length. """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def generate_link(request, id):
    """ Generate the link itself. """
    the_string = randomString(20)
    OneTimeLinkModel.objects.create(one_time_code=the_string)
    return HttpResponse('<a href="/social/otl/{}/{}">{}{}</a>'.format(id, the_string, request.build_absolute_uri(), the_string))


def one_time_link(request, id, access_code):
    """ Handles the link request. """
    if OneTimeLinkModel.objects.filter(one_time_code=access_code).exists():
        model = OneTimeLinkModel.objects.get(one_time_code=access_code)
        expire_time = model.expiry_time - datetime.timedelta(days=1)
        today = datetime.datetime.now()

        if expire_time > today:
            OneTimeLinkModel.objects.filter(one_time_code=access_code).delete()
            return HttpResponse("Expired link.")

        url = reverse('social-detail', args=[id])
        return redirect(url)

    elif not OneTimeLinkModel.objects.filter(one_time_code=access_code).exists():
        return HttpResponse("Bad or expired link.")
    else:
        return HttpResponse("Bad or expired link.")
