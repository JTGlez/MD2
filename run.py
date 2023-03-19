import binascii
import fileinput as fp

S = [ 
 41, 46, 67, 201, 162, 216, 124, 1, 61, 54, 84, 161, 236, 240, 6,
 19, 98, 167, 5, 243, 192, 199, 115, 140, 152, 147, 43, 217, 188,
 76, 130, 202, 30, 155, 87, 60, 253, 212, 224, 22, 103, 66, 111, 24,
 138, 23, 229, 18, 190, 78, 196, 214, 218, 158, 222, 73, 160, 251,
 245, 142, 187, 47, 238, 122, 169, 104, 121, 145, 21, 178, 7, 63,
 148, 194, 16, 137, 11, 34, 95, 33, 128, 127, 93, 154, 90, 144, 50,
 39, 53, 62, 204, 231, 191, 247, 151, 3, 255, 25, 48, 179, 72, 165,
 181, 209, 215, 94, 146, 42, 172, 86, 170, 198, 79, 184, 56, 210,
 150, 164, 125, 182, 118, 252, 107, 226, 156, 116, 4, 241, 69, 157,
 112, 89, 100, 113, 135, 32, 134, 91, 207, 101, 230, 45, 168, 2, 27,
 96, 37, 173, 174, 176, 185, 246, 28, 70, 97, 105, 52, 64, 126, 15,
 85, 71, 163, 35, 221, 81, 175, 58, 195, 92, 249, 206, 186, 197,
 234, 38, 44, 83, 13, 110, 133, 40, 132, 9, 211, 223, 205, 244, 65,
 129, 77, 82, 106, 220, 55, 200, 108, 193, 171, 250, 36, 225, 123,
 8, 12, 189, 177, 74, 120, 136, 149, 139, 227, 99, 232, 109, 233,
 203, 213, 254, 59, 0, 29, 57, 242, 239, 183, 14, 102, 88, 208, 228,
 166, 119, 114, 248, 235, 117, 75, 10, 49, 68, 80, 180, 143, 237,
 31, 26, 219, 153, 141, 51, 159, 17, 131, 20];

import binascii

def md2(message):
    "Implementa el algoritmo MD2 en Python"
    # Paso 1: obtener el padding.
    tamaño_bloque = 16
    mensaje_bytes = bytearray(mensaje, 'utf-8') #Obtenemos los bytes del mensaje. 

    relleno = tamaño_bloque - (len(mensaje_bytes) % tamaño_bloque) #Realizamos la operación de padding.
    mensaje_bytes += bytearray(relleno for _ in range(relleno)) #Añadimos el padding a los bytes del mensaje.

    # Step 2: Agregar el checksum
    L = 0
    checksum = bytearray(0 for _ in range(tamaño_bloque)) #Clear
    
    for i in range(len(mensaje_bytes) // tamaño_bloque):
        for j in range(tamaño_bloque):
            c = mensaje_bytes[i * tamaño_bloque + j]
            checksum[j] = checksum[j] ^ (S[c ^ L])
            L = checksum[j]
        mensaje_bytes += checksum

    # Paso 3: Inicializar el buffer
    tamaño_buffer = 48
    X = bytearray([0 for _ in range(tamaño_buffer)])
    n_rondas = 18

    # Step 4: Process message in 16-byte blocks
    for i in range(len(mensaje_bytes) // tamaño_bloque):
        for j in range(tamaño_bloque):
            X[tamaño_bloque + j] = mensaje_bytes[i * tamaño_bloque + j]
            X[tamaño_bloque * 2 + j] = X[tamaño_bloque + j] ^ X[j]
        t = 0
        for j in range(n_rondas):
            for k in range(tamaño_buffer):
                t = X[k] = X[k] ^ S[t]
            t = (t + j) % len(S) #Mod 256
        
    # Se devuelve el hash MD2 como una cadena de texto hexadecimal.
    return binascii.hexlify(X[:16]).decode('utf-8')

#Recuperando las entradas en una lista.
inputs = []

for entrada in fp.input():
    inputs.append(entrada.strip())

mensaje = ''.join(inputs)

print(md2(mensaje))