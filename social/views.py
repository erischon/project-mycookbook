import random
import string

from django.http import HttpResponse
from .models import OneTimeLinkModel


def randomString(stringLength=20):
    """ Generate a random string of fixed length. """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def generate_link(request, pk):
    """ Generate the link itself. """
    the_string = randomString(stringLength=20)
    the_url = "69/detail"
    OneTimeLinkModel.objects.create(one_time_code=the_string)
    return HttpResponse('<a href="/cookbook/{}/{}">{}{}</a>'.format(the_url, the_string, request.build_absolute_uri(), the_string))


def one_time_link(request,access_code=0):
    """ Handles the link request. """

    if (access_code == 0):
        return HttpResponse("Test link")

    elif OneTimeLinkModel.objects.filter(one_time_code=access_code).exists():
        OneTimeLinkModel.objects.filter(one_time_code=access_code).delete()
        return HttpResponse("Hey, your linked worked. Make sure to download as it won't work again.")

    elif not OneTimeLinkModel.objects.filter(one_time_code=access_code).exists():
        return HttpResponse("Bad or expired link.")
    else:
        return HttpResponse("Bad or expired link.")
