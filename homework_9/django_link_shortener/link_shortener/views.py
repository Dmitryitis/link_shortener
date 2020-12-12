import random
import string

from django.shortcuts import render
from link_shortener.forms import ReceiverLink
from link_shortener.models import Link


def shortener(request):
    link = ""
    error_message = ""
    short_link = ""

    if request.POST is not None:
        receiver_link = ReceiverLink(request.POST or None)
        if receiver_link.is_valid():
            link = receiver_link.cleaned_data.get('link')

            short_part = short_gen()
            short_link = create_short_link(link, short_part)

            Link.objects.update_or_create(link=link)
        elif not receiver_link.is_valid() and hasattr(receiver_link, 'cleaned_data'):
            error_message = "Введите правильную ссылку"

    context = {
        'link': link,
        'short_link': short_link,
        'error_message': error_message,
    }

    return render(request, 'link_shorter.html', context)


def base_str():
    return string.ascii_letters + string.digits


def short_gen():
    res = ""
    for i in range(4):
        result_short = random.choices(base_str())
        res += result_short[0]
    return res


def create_short_link(link, short_part):
    link_parts = str(link).split('/')
    res_link = f"{link_parts[0]}//{link_parts[2]}/{short_part}"
    return res_link
