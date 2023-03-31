from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Esto sirve para convertir strings a jsons y jsons a strings
from json import loads, dumps
import sqlite3
import requests

# Create your views here.
# Ruta para index
def index(request):
    return render(request, 'index.html')


## USUARIOS
# Create
# {"password": "something"}
@csrf_exempt
def crear_usuario(request):
    body = request.body.decode('UTF-8')
    eljson = loads(body)
    # id = eljson['id']
    password = eljson['password']
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    res = cur.execute("INSERT INTO usuarios (password) VALUES (?)", (password))
    con.commit()
    return HttpResponse('Se agregó el usuario exitosamente')

# Read
@csrf_exempt
def leer_usuario(request):
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM usuarios")
    resultado = res.fetchall()
    return render(request, 'usuarios.html', {'lista_usuarios':resultado})

# Update
# {"id": "1", "password": "updated"}
@csrf_exempt
def actualizar_usuario(request):
    body = request.body.decode('UTF-8')
    eljson = loads(body)
    id = eljson['id']
    password = eljson['password']
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    res = cur.execute("UPDATE usuarios SET password = ? WHERE id = ?",(password, str(id)))
    con.commit()
    return HttpResponse('Usuario '+ str(id) + ' actualizado')

# Delete
# {"id": "2"}
@csrf_exempt
def borrar_usuario(request):
    body = request.body.decode('UTF-8')
    eljson = loads(body)
    id = eljson['id']
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    res1 = cur.execute("DELETE from usuarios WHERE id = ?", str(id))
    res2 = cur.execute("DELETE from partidas WHERE id_usuario = ?", str(id))
    con.commit()
    return HttpResponse('Se borró el Usuario con '+ str(id) + ' y las partidas con su ID')


## PARTIDAS
# Create
# {"fecha": "marzo 30", "id_usuario": "1", "minutos_jugados": "20", "puntaje": "234"}
@csrf_exempt
def crear_partidas(request):
    body = request.body.decode('UTF-8')
    eljson = loads(body)
    fecha = eljson['fecha']
    id_usuario = eljson['id_usuario']
    minutos_jugados = eljson['minutos_jugados']
    puntaje = eljson['puntaje']
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    res = cur.execute("INSERT INTO partidas (fecha, id_usuario, minutos_jugados, puntaje) VALUES(?, ?, ?, ?)", (fecha, id_usuario, minutos_jugados, puntaje))
    con.commit()
    return HttpResponse('Se agregó la partida exitosamente')

# Read
@csrf_exempt
def leer_partidas(request):
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM partidas")
    resultado = res.fetchall()
    return render(request, 'partidas.html', {'lista_partidas':resultado})

# Update
# {"id": "1", "fecha": "marzo 30", "minutos_jugados": "30", "puntaje": "246"}
@csrf_exempt
def actualizar_partidas(request):
    body = request.body.decode('UTF-8')
    eljson = loads(body)
    id = eljson['id']
    fecha = eljson['fecha']
    minutos_jugados = eljson['minutos_jugados']
    puntaje = eljson['puntaje']
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    res = cur.execute("UPDATE partidas SET fecha = ?, minutos_jugados = ?, puntaje = ? WHERE id = ?",(fecha, minutos_jugados, puntaje, str(id)))
    con.commit()
    return HttpResponse('Partida '+ str(id) + ' actualizada')

# Delete
# {"id": "2"}
@csrf_exempt
def borrar_partidas(request):
    body = request.body.decode('UTF-8')
    eljson = loads(body)
    id = eljson['id']
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    res = cur.execute("DELETE from partidas WHERE id = ?", str(id))
    con.commit()
    return HttpResponse('Partida '+ str(id) + ' borrada')


# Rutas para los procesos
## USUARIOS
@csrf_exempt
def usuarios(request):
    if request.method == 'GET':
        # Read
        return(leer_usuario(request))
    elif request.method == 'POST':
        # Create
        return(crear_usuario(request))
    elif request.method == 'PUT':
        # Update
        return(actualizar_usuario(request))
    elif request.method == 'DELETE':
        # Delete
        return(borrar_usuario(request))
    
## PARTIDAS
@csrf_exempt
def partidas(request):
    if request.method == 'GET':
        # Read
        return(leer_partidas(request))
    elif request.method == 'POST':
        # Create
        return(crear_partidas(request))
    elif request.method == 'PUT':
        # Update
        return(actualizar_partidas(request))
    elif request.method == 'DELETE':
        # Delete
        return(borrar_partidas(request))