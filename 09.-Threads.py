import threading
import time

# Función que será ejecutada por el hilo
def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)  # Espera 1 segundo

# Creamos un hilo
thread = threading.Thread(target=print_numbers)

# Iniciamos el hilo
thread.start()

# Esperamos a que el hilo termine antes de continuar
thread.join()

print("Hilo terminado.")
