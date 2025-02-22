import requests
import time
import os
from art import text2art
from colorama import Fore, Back, Style, init

# Inicializar colorama
init()

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_banner():
    banner = """
  ___ ___                        _________                      
 /   |   \   ____ ___  ________  \_   ___ \  _________________  
/    ~    \_/ __ \\  \/  /\__  \ /    \  \/ /  _ \_  __ \____ \ 
\    Y    /\  ___/ >    <  / __ \\     \___(  <_> )  | \/  |_> >
 \___|_  /  \___  >__/\_ \(____  /\______  /\____/|__|  |   __/ 
       \/       \/      \/     \/        \/             |__|    
    """
    print(Fore.MAGENTA + banner + Style.RESET_ALL)
    print("\nHexaCorp - Cliente HTTPS Simple")
    print(Fore.RED + "\n[1]" + Style.RESET_ALL + " Enviar solicitud HTTPS única")
    print(Fore.RED + "[2]" + Style.RESET_ALL + " Enviar solicitudes HTTPS múltiples")
    print(Fore.RED + "[3]" + Style.RESET_ALL + " Obtener información de IP")
    print(Fore.RED + "[0]" + Style.RESET_ALL + " Salir")

def hacer_solicitud(numero_solicitudes=1):
    url = input("\nDirección web (ejemplo: https://ejemplo.com): ")
    
    # Verificar si la URL comienza con HTTPS
    if not url.startswith('https://'):
        if url.startswith('http://'):
            url = 'https://' + url[7:]
        else:
            url = 'https://' + url
        print(f"\nURL modificada a HTTPS: {url}")
    
    for i in range(numero_solicitudes):
        try:
            print(f"\nEnviando solicitud HTTPS {i+1}...")
            response = requests.get(url, verify=True)  # verify=True asegura la verificación SSL
            print(f"\nEstado de la respuesta {i+1}: {response.status_code}")
            print(f"Tiempo de respuesta: {response.elapsed.total_seconds():.2f} segundos")
            
            if response.status_code == 200:
                print("✅ Solicitud exitosa")
            else:
                print("⚠️ La solicitud no fue exitosa")
                
        except requests.exceptions.SSLError:
            print(f"\n❌ Error SSL: El sitio no soporta HTTPS o el certificado no es válido")
        except requests.exceptions.RequestException as e:
            print(f"\n❌ Error al hacer la solicitud {i+1}: {e}")
    
    input("\nPresiona Enter para continuar...")

def obtener_info_ip():
    ip = input("\nIngrese la dirección IP (ejemplo: 8.8.8.8): ")
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        if response.status_code == 200:
            data = response.json()
            if data["status"] == "success":
                print("\n=== Información de la IP ===")
                print(f"IP: {data.get('query', 'N/A')}")
                print(f"Ciudad: {data.get('city', 'N/A')}")
                print(f"Región: {data.get('regionName', 'N/A')}")
                print(f"País: {data.get('country', 'N/A')}")
                print(f"ISP: {data.get('isp', 'N/A')}")
                print(f"Organización: {data.get('org', 'N/A')}")
                print(f"AS: {data.get('as', 'N/A')}")
                print(f"Latitud: {data.get('lat', 'N/A')}")
                print(f"Longitud: {data.get('lon', 'N/A')}")
                print(f"Zona Horaria: {data.get('timezone', 'N/A')}")
            else:
                print("\n⚠️ La IP proporcionada no es válida")
        else:
            print("\n⚠️ No se pudo obtener la información de la IP")
    except Exception as e:
        print(f"\n❌ Error al obtener la información: {e}")
    
    input("\nPresiona Enter para continuar...")

def main():
    while True:
        limpiar_pantalla()
        mostrar_banner()
        
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == "1":
            hacer_solicitud()
        elif opcion == "2":
            hacer_solicitud(30)
        elif opcion == "3":
            obtener_info_ip()
        elif opcion == "0":
            print("\n¡Hasta luego!")
            break
        else:
            print("\nOpción no válida")
            time.sleep(1)

if __name__ == "__main__":
    main()