from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html  import escape
# Create your views here.

def handle_request(request):
    print(request.body);
    return HttpResponse(pretty_request(request));

def pretty_request(request):
    headers = ''
    for header, value in request.META.items():
        if not header.startswith('HTTP'):
            continue
        header = '-'.join([h.capitalize() for h in header[5:].lower().split('_')])
        headers += '{}: {}\n'.format(header, value)

    return (
        '{method} HTTP/1.1<br>'
        'Content-Length: {content_length}<br>'
        'Content-Type: {content_type}<br>'
        '{headers}<br><br>'
        '{body}'
    ).format(
        method=request.method,
        content_length=request.META['CONTENT_LENGTH'],
        content_type=request.META['CONTENT_TYPE'],
        headers=headers,
        body=request.body,
    )