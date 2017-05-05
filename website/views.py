from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Media


def index(request):
    media_list = list(Media.objects.order_by('language'))
    if not media_list:
        raise Http404("No Media Found")

    #Get all of the languages
    language_list = []
    for media_item in media_list:
        if media_item.language not in language_list:
            language_list.append(media_item.language)

    context = {'language_list': language_list}
    return render(request, 'website/language_list.html', context)

def language(request,language_name):
    media_list = get_list_or_404(Media, language=language_name)
    context = {'language_name':language_name,'media_list':media_list}
    return render(request, 'website/language_view.html', context)

def media(request,media_id):
    media_item = get_object_or_404(Media, id=media_id)
    supplied_code = request.POST.get('code','')
    context = {'media_item':media_item, 'supplied_code':supplied_code}

    #Return Media Page
    if media_item.is_valid_code(supplied_code):
        return render(request, 'website/media_view.html', context)
    else: #Return Code Page
        show_error_message = False
        if len(supplied_code.strip()) != 0:
            show_error_message = True
        context = {'media_item':media_item, 'show_error_message':show_error_message}
        return render(request, 'website/code_entry.html', context)

def codes_list(request):
    media_list = list(Media.objects.order_by('language'))
    if not media_list:
        raise Http404("No Media Found")

    for i in range(0,len(media_list)):
        media = media_list[i]
        media.first_in_language = i == 0 or media_list[i].language != media_list[i - 1].language
        media.code = media.course_name.replace(' ','').lower()

    context = {'media_list': media_list}
    return render(request, 'website/codes_list.html', context)
