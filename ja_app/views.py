from django.http import HttpResponse

def home(request):
    return HttpResponse("Athos, Hello from django, it has rendered the views.py archive. Try out <a href='/admin/'>/admin/</a>\n")