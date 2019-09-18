from django.http import HttpResponse
from datetime import datetime
'''Modulo de Json viene preinstalada en python'''
import json
def hello_world (request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, Hola!. La hora actual de servidor es: {0}'.format(now))

def sorted_numbers(request):
    import pdb
    # Comprehensions volviendo una lista de ordenada de enteros a nuestra peticion get con parametros numbers
    # Tambien podia haberlo hecho asi: numbers= sorted(list(map(int,request.GET['numbers'].split(','))))
    numbers=sorted([ int(i) for i in request.GET['numbers'].split(',')])
    # pdb.set_trace()
    data={
        'estado':'ok',
        'numbers':numbers,
        'mensaje':'numbers ordenados satisfactoriamente'
    }
    pdb.set_trace()
    '''"json.dumps(data)" convierte el diccionario en json  y en content_type: especificamos el tipo de valor que entendera el html'''
    return HttpResponse(json.dumps(data),content_type='application/json')

def hi(request,name,edad):
    if edad <12:
        mensaje='Lo siento {},pero no puedes estar aqui'.format(name)
    else:
        mensaje='Hola, {}! Bienvenido a Platzigram'.format(name.upper())
    return HttpResponse(mensaje)