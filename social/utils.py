import random
import string


def random_string(string_length):
    """ Generate a random string of fixed length. """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))


def increment_by_one(link):
    """ Increment by one the use count. """
    link.use_count = link.use_count + 1
    link.save()
    return link
