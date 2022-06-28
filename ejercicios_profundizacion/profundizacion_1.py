# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:

A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!')
#Empezar aquí la resolución del ejercicio

Numero_1 = int(input())
Numero_2 = int(input())

suma= Numero_1 + Numero_2
print('La suma entre',Numero_1,'y',Numero_2, 'es',suma)
resta= Numero_1 - Numero_2
print('El resultado de restarle',Numero_2,'a',Numero_1, 'es',resta)
multiplicacion = Numero_1 * Numero_2
print('El resultado de multiplicar',Numero_1,'con',Numero_2, 'es',multiplicacion)
división = Numero_1 * Numero_2
print('El resultado de dividir',Numero_1,'entre',Numero_2, 'es',división)
potencia = Numero_1 ** Numero_2
print('La potencia de',Numero_1,'con exponente',Numero_2, 'es',potencia)