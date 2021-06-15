from django.shortcuts import redirect
from django.http import HttpResponse
from django.urls import reverse

from .models import OneTimeLinkModel
from social.utils import random_string, increment_by_one


STRING_LENGTH = 20
MAX_IMPRESSION = 3


def generate_link(request, id):
    """ Generate the link itself. """
    the_string = random_string(STRING_LENGTH)
    OneTimeLinkModel.objects.create(one_time_code=the_string)
    return HttpResponse('<a href="/social/otl/{}/{}">{}{}</a>'.format(id, the_string, request.build_absolute_uri(), the_string))


def one_time_link(request, id, access_code):
    """ Handles the link request. """
    if OneTimeLinkModel.objects.filter(one_time_code=access_code).exists():
        link = increment_by_one(OneTimeLinkModel.objects.get(one_time_code=access_code))

        if link.use_count <= MAX_IMPRESSION:
            url = reverse('social-detail', args=[id])
            return redirect(url)
        else:
            OneTimeLinkModel.objects.filter(one_time_code=access_code).delete()
            return HttpResponse("Expired link.")

    elif not OneTimeLinkModel.objects.filter(one_time_code=access_code).exists():
        return HttpResponse("Bad or expired link.")
    else:
        return HttpResponse("Bad or expired link.")
