from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from estnltk.converters import export_TCF, import_TCF

from django.shortcuts import render

tcf_template = """
<D-Spin version="0.4" xmlns="http://www.dspin.de/data">
  <MetaData xmlns="http://www.dspin.de/data/metadata"/>
  <TextCorpus lang="et" xmlns="http://www.dspin.de/data/textcorpus">
    <text>{text}</text>
  </TextCorpus>
</D-Spin>
"""


@csrf_exempt
def words(request):
    content_type = request.META.get('CONTENT_TYPE')
    if content_type == "text/tcf+xml":
        return words_tcf(request)
    elif content_type == "text/plain":
        return words_txt(request)
    else:
        raise ValueError("Invalid content type: %s" % content_type)


def words_txt(request):
    input = request.read().decode()
    input = tcf_template.format(text=input)
    text = import_TCF(string=input)
    text.tag_layer(['words'])
    response = export_TCF(text)
    return HttpResponse(response)


def words_tcf(request):
    text = import_TCF(file=request)
    text.tag_layer(['words'])
    response = export_TCF(text)
    return HttpResponse(response)


@csrf_exempt
def sentences(request):
    content_type = request.META.get('CONTENT_TYPE')
    if content_type == "text/tcf+xml":
        return sentences_tcf(request)
    elif content_type == "text/plain":
        return sentences_txt(request)
    else:
        raise ValueError("Invalid content type: %s" % content_type)


def sentences_txt(request):
    input = request.read().decode()
    input = tcf_template.format(text=input)
    text = import_TCF(string=input)
    text.tag_layer(['sentences'])
    response = export_TCF(text)
    return HttpResponse(response)


def sentences_tcf(request):
    text = import_TCF(file=request)
    text.tag_layer(['sentences'])
    response = export_TCF(text)
    return HttpResponse(response)


@csrf_exempt
def morph(request):
    content_type = request.META.get('CONTENT_TYPE')
    if content_type == "text/tcf+xml":
        return morph_tcf(request)
    elif content_type == "text/plain":
        return morph_txt(request)
    else:
        raise ValueError("Invalid content type: %s" % content_type)


def morph_tcf(request):
    text = import_TCF(file=request)
    text.tag_layer(['morph_analysis'])
    response = export_TCF(text)
    return HttpResponse(response)


def morph_txt(request):
    input = request.read().decode()
    input = tcf_template.format(text=input)
    text = import_TCF(string=input)
    text.tag_layer(['morph_analysis'])
    response = export_TCF(text)
    return HttpResponse(response)
