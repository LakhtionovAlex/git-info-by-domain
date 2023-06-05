import requests
import socket
import folium


def get_info_by_url(domain):
    try:
        ip = socket.gethostbyname(domain)
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        data = {
            'IP': response.get('query'),
            'Country': response.get('country'),
            'City': response.get('city'),
            'Lat': response.get('lat'),
            'Lon': response.get('lon'),
            'Isp': response.get('isp'),
            'Org': response.get('org')
        }
        for key, value in data.items():
            if value == '0.0.0.0':
                print('Please enter domain')
                break
            else:
                print(f'{key} : {value}')

            my_map = folium.Map(location=[response.get('lat'), response.get('lon')], zoom_start=15)
            my_map.save(f'{response.get("query")}_{response.get("city")}.html')

    except requests.exceptions.ConnectionError:
        print('Please check your connection')

    except socket.gaierror:
        print('Please enter the correct domain')


def main():
    domain = input('Please input a target Domain: ')
    get_info_by_url(domain=domain)


if __name__ == '__main__':
    main()
