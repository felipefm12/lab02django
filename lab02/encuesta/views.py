from django.shortcuts import render

# Creacion de vistas.
def index(request):
    context = {
        'titulo':"Formulaario"
    }
    return render(request, 'encuesta/formulario.html', context)


#-----------------------------Vista formulario matematico---------------------------
def indexmatematico(request):
    context = {
        'titulo':"Formulaario"
    }
    return render(request, 'encuesta/formatematico.html', context)

#-----------------------------Vista formulario de Cilindro---------------------------
def indexcilindro(request):
    context = {
        'titulo':"Formulario de Volumen"
    }
    return render(request, 'encuesta/forcilindro.html', context)


def enviar(request):
    context = {
        'titulo': "Respuesta",
        'nombre': request.POST['nombre'], #request.POST['nombre'] etiqueta name="nombre"
        'clave': request.POST['password'], #clave biene ser las variables que van aser usadas
        'educacion': request.POST['educacion'],
        'nacionalidad': request.POST['nacionalidad'],
        'idiomas': request.POST.getlist('idiomas'),
        'correo': request.POST['email'],
        'website': request.POST['sitioweb'],     
    }
    return render(request,'encuesta/respuesta.html', context )  #manda valores de la funcion hacia respuesta.html



def enviar2(request):
    x = request.POST['number1']
    y = request.POST['number2']
    
    resultsuma = int(x) + int(y) 
    resultresta = int(x) - int(y)
    resultmulti = int(x) * int(y)
    
    context = {
        'titulo': "Respuesta",
        'numero1': request.POST['number1'], #request.POST['number1'] etiqueta name="number1"
        'numero2': request.POST['number2'], #clave biene ser las variables que van aser usadas
        'operacion': request.POST['operacion'],
        'suma': resultsuma,
        'resta': resultresta,
        'multi': resultmulti,     
    }
    return render(request,'encuesta/resmatematico.html', context )


def calcular(request):
    x = request.POST['diametro']
    radio2 = ((float(x) / 2) ** 2) * 3.1416
    
    y = request.POST['altura']
    
    resultvolumen = float(radio2) * float(y) 
    #resultresta = int(x) - int(y)
    #resultmulti = int(x) * int(y)
    
    context1 = {
        'titulo': "Formulario de Volumen:",
        #'numero1': request.POST['number1'], #request.POST['number1'] etiqueta name="number1"
        #'numero2': request.POST['number2'], #clave biene ser las variables que van aser usadas
        #'operacion': request.POST['operacion'],
        'volumen': resultvolumen,
        #'radio': radio2,
        
            
    }
    return render(request,'encuesta/forcilindro.html', context1 )