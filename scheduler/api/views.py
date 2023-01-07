from django.shortcuts import render, HttpResponse

# Create your views here.
def fetch_form(request):

    print("REQUESTS\n\n", request)

    return HttpResponse("<h1>Hello</h1>")