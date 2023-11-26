from django.http import HttpResponse
from rest_framework.parsers import MultiPartParser
from rest_framework.request import Request
from . import calldeplot


def understand_graph(request: Request):
    if request.method == "POST":
        image_data = request.data["image"]
        resp = calldeplot.call_deplot(image_data)
        return HttpResponse(resp)
    else:
        return HttpResponse("Could not parse image")
