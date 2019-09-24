# Se deben validar las dimensiones de una imagen para saber si es posible o no subir una imagen
l = int(input())
n = int(input())
while n > 0:
    w, h = map(int, input().split())
    if w < l or h < l:
        print("UPLOAD ANOTHER")
    elif w == l and h == l:
        print("ACCEPTED")
    elif w == h and w >= l:
        print("ACCEPTED")
    else:
        print("CROP IT")
    n -= 1
