from django.http import HttpResponse

def bienvenida(request):
    return HttpResponse("Bienvenido zoo")


