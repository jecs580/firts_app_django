from django.http import HttpResponse
from datetime import datetime
import json
def hello_world (request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, Hola!. La hora actual de servidor es: {now}'.format(now=now))

def sorted_numbers(request):
    import pdb
    numbers=[ int(i) for i in request.GET['numbers'].split(',')]
    sorted_number=sorted(numbers)
    # pdb.set_trace()
    data={
        'estado':'ok',
        'numbers':sorted_number,
        'mensaje':'numbers ordenados satisfactoriamente'
    }
    return HttpResponse(json.dumps(data),content_type='application/json')

def hi(request,name,edad):
    if edad <12:
        mensaje='Lo siento {},pero no puedes estar aqui'.format(name)
    else:
        mensaje='Hola, {}! Bienvenido a Platzigram'.format(name.upper())
    return HttpResponse(mensaje)