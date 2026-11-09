print("Estructuras Condicionales")

# Condicional Simple
nota_TBI = 17
if nota_TBI >= 10.51:
    print("Aprobaste")

# Condicional Doble
edad = 17
if edad>=18:
    print("Tomar bebidas en exceso no es bueno")
else:
    print("No apto para menores")

# Condicional Anidado
nota = 20 
if nota>17 & nota<=20:
    print("Alumno brillante")
elif nota>=15 & nota< 17:
    print("Alumno excelente")
elif nota>=13 & nota< 15:
    print("Alumno Bueno")

# Condicional Multiple
"""
Python 
"""

num =4
match num:
    case 1: print("Vocal A")
    case 2: print("Vocal E")
    case 3: print("Vocal I")
    case 4: print("Vocal O")
    case 5: print("Vocal U")
    case _: print("Numero no pertenece a Vocal")