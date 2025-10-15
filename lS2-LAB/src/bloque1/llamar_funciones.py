

from src.bloque1.funciones import parte_fraccionaria , redondea, eliminar_espacios_sobrantes, detectar_isograma, transformar_en_camelcase

print(parte_fraccionaria(3.1415))
print(parte_fraccionaria(-3.1415))
print(redondea(3.1415, 1))
print(redondea(3.1815, 1))
print(eliminar_espacios_sobrantes("  Hola   Mundo  "))
print(detectar_isograma("lobo"))
print(detectar_isograma("murcielago"))
print(transformar_en_camelcase("  hola   mundo  "))
print(transformar_en_camelcase("  este es un ejemplo de camelcase  "))