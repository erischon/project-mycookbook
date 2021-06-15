import random
import string

from django.shortcuts import redirect
from django.http import HttpResponse
from django.urls import reverse

from .models import OneTimeLinkModel


STRING_LENGTH = 20
MAX_IMPRESSION = 3


def randomString(string_length):
    """ Generate a random string of fixed length. """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))


def generate_link(request, id):
    """ Generate the link itself. """
    the_string = randomString(STRING_LENGTH)
    OneTimeLinkModel.objects.create(one_time_code=the_string)
    return HttpResponse('<a href="/social/otl/{}/{}">{}{}</a>'.format(id, the_string, request.build_absolute_uri(), the_string))


def one_time_link(request, id, access_code):
    """ Handles the link request. """
    if OneTimeLinkModel.objects.filter(one_time_code=access_code).exists():
        model = OneTimeLinkModel.objects.get(one_time_code=access_code)
        model.use_count = model.use_count + 1
        model.save()

        if model.use_count <= MAX_IMPRESSION:
            url = reverse('social-detail', args=[id])
            return redirect(url)
        else:
            OneTimeLinkModel.objects.filter(one_time_code=access_code).delete()
            return HttpResponse("Expired link.")

    elif not OneTimeLinkModel.objects.filter(one_time_code=access_code).exists():
        return HttpResponse("Bad or expired link.")
    else:
        return HttpResponse("Bad or expired link.")