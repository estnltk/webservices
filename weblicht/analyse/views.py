from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from estnltk.converters import export_TCF, import_TCF

from django.shortcuts import render

def index (request):
    return render(request, 'weblicht service.html')

@csrf_exempt
def words(request):
    text = import_TCF(file=request)
    text.tag_layer(['words'])
    response = export_TCF(text)
    return HttpResponse(response)

@csrf_exempt
def sentences(request):
    text = import_TCF(file=request)
    text.tag_layer(['sentences'])
    response = export_TCF(text)
    return HttpResponse(response)

@csrf_exempt
def morph(request):
    text = import_TCF(file=request)
    text.tag_layer(['morph_analysis'])
    response = export_TCF(text)
    return HttpResponse(response)
