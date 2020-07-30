from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos<h1>'.format(nome, idade))
def soma(request, valor_a, valor_b):
    return HttpResponse('<h1> Calculadora: \n</h1><h2>Soma {} + {} = {}</h2>'.format(valor_b, valor_b, (valor_a+valor_b)))

def subtracao(request, valor_a, valor_b):
    return HttpResponse('<h1> Calculadora: \n</h1><h2>Subtração {} - {} = {}</h2>'.format(valor_b, valor_b, (valor_a-valor_b)))

def divisao(request, valor_a, valor_b):
    return HttpResponse('<h1> Calculadora: \n</h1><h2>Divisão {} / {} = {}</h2>'.format(valor_b, valor_b, (valor_a/valor_b)))

def multiplicacao(request, valor_a, valor_b):
    return HttpResponse('<h1> Calculadora: \n</h1><h2>Multiplicação {} * {} = {}</h2>'.format(valor_b, valor_b, (valor_a*valor_b)))
