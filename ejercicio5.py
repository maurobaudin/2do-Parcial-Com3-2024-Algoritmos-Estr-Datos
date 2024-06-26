import os

# 1. Crear un directorio
original_dir = 'directorio_alumnos'
if not os.path.exists(original_dir):
    os.mkdir(original_dir)
    print(f"Directorio '{original_dir}' creado.")

# 2. Guardar en un archivo una lista de alumnos
alumnos = ["Juan Pérez", "María Gómez", "Carlos Sánchez", "Ana Martínez"]
file_path = os.path.join(original_dir, 'lista_alumnos.txt')
with open(file_path, 'w') as file:
    for alumno in alumnos:
        file.write(alumno + '\n')
    print(f"Archivo '{file_path}' creado y lista de alumnos guardada.")

# 3. Mover el directorio a una nueva ruta
new_dir = 'nuevo_directorio_alumnos'
if not os.path.exists(new_dir):
    os.rename(original_dir, new_dir)
    print(f"Directorio movido a '{new_dir}'.")

# 4. Borrar el archivo y el directorio
new_file_path = os.path.join(new_dir, 'lista_alumnos.txt')
if os.path.exists(new_file_path):
    os.remove(new_file_path)
    print(f"Archivo '{new_file_path}' eliminado.")

if os.path.exists(new_dir):
    os.rmdir(new_dir)
    print(f"Directorio '{new_dir}' eliminado.")