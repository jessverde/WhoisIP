import requests

def get_ip_info(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        response.raise_for_status()
        data = response.json()
        return {
            'country': data.get('country'),
            'city': data.get('city'),
            'countryCode': data.get('countryCode'),
            'continent': data.get('continent')
        }
    except requests.RequestException as e:
        print(f'Error: {e}')
        return None

# List of IP addresses to look up
ip_addresses = ['Insert your IP here']

# Loop through the list of IP addresses and print out information
for ip in ip_addresses:
    info = get_ip_info(ip)
    if info:
        print(f"Details for IP: {ip}")
        print(f"Country: {info['country']}")
        print(f"City: {info['city']}")
        print(f"Country Code: {info['countryCode']}")
        print(f"Continent: {info['continent']}")
        print('---------------------------------')

