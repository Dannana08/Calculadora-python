import os
from collections import Counter

# CAMBIA esta ruta por la de tu carpeta Mods
ruta_mods = r"C:\Users\PC Gamer\AppData\Roaming\ModrinthApp\profiles\COBBLEVERSE - MODPACK BKN 1.0.0\mods"

archivos = []

# Recorre todas las subcarpetas
for carpeta_actual, subcarpetas, nombres_archivos in os.walk(ruta_mods):
    for archivo in nombres_archivos:
        archivos.append(archivo)

# Cuenta repetidos por nombre exacto
contador = Counter(archivos)

# Guardar lista completa
with open("lista_mods.txt", "w", encoding="utf-8") as f:
    f.write("=== LISTA COMPLETA DE MODS ===\n")
    for archivo in sorted(archivos):
        f.write(f"{archivo}\n")

    f.write("\n=== ARCHIVOS REPETIDOS ===\n")
    repetidos = False
    for archivo, cantidad in contador.items():
        if cantidad > 1:
            repetidos = True
            f.write(f"{archivo} (x{cantidad})\n")

    if not repetidos:
        f.write("No se encontraron archivos repetidos por nombre.\n")

print("Listo. Se creó el archivo 'lista_mods.txt' en la misma carpeta donde ejecutaste el script.")