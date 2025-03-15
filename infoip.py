import requests
import sys

def banner():
        print("""██╗██████╗       ██╗███╗   ██╗███████╗ ██████╗
██║██╔══██╗      ██║████╗  ██║██╔════╝██╔═══██╗
██║██████╔╝█████╗██║██╔██╗ ██║█████╗  ██║   ██║
██║██╔═══╝ ╚════╝██║██║╚██╗██║██╔══╝  ██║   ██║
██║██║           ██║██║ ╚████║██║     ╚██████╔╝
╚═╝╚═╝           ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝""")
banner()


def get_ip_details(ip):
    """Obtém detalhes do IP usando a API ipwhois.app"""
    url = f"https://ipwhois.app/json/{ip}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_ip_details(details):
    """Exibe os detalhes do IP formatados"""
    print("\nDetalhes do IP:\n")
    print(f"IP: {details.get('ip', 'N/A')}")
    print(f"País: {details.get('country', 'N/A')}")
    print(f"Cidade: {details.get('city', 'N/A')}")
    print(f"Região: {details.get('region', 'N/A')}")
    print(f"Latitude: {details.get('latitude', 'N/A')}")
    print(f"Longitude: {details.get('longitude', 'N/A')}")
    print(f"Provedor: {details.get('isp', 'N/A')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 infoip.py <IP>")
        sys.exit(1)

    ip = sys.argv[1]
    ip_details = get_ip_details(ip)

    if ip_details and ip_details.get('success', False):
        display_ip_details(ip_details)
    else:
        print("Falha ao obter detalhes do IP ou IP inválido.")
