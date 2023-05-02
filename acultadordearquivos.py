import ctypes

atributos_acultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('ocultar.txt', atributos_acultar)

if retorno:
    print("Arquivo foi acultado")
else:
    print("Arquivo não foi acultado")