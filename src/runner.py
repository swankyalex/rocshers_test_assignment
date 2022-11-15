import urllib.request
from urllib.parse import urlparse
from urllib.error import URLError
import pprint

HTTP_METHODS = [
    'GET',
    'HEAD',
    'POST',
    'PUT',
    'DELETE',
    'CONNECT',
    'OPTIONS',
    'TRACE',
    'PATCH'
]


def check_string(string: str) -> bool:
    """Checking if provided string is a correct link"""
    if urlparse(string).scheme:
        return True
    return False


def reader() -> list:
    """Reading data from stdin"""
    strings = []
    while True:
        string = input()
        if string == '':
            break
        if check_string(string):
            strings.append(string)
        else:
            print(f'Строка {string} не является ссылкой')
    return strings


def send_request(url: str, results: dict) -> None:
    """Sending HTTP requests to provided link"""
    results[url] = {}
    for method in HTTP_METHODS:
        req = urllib.request.Request(url=url, method=method)
        try:
            with urllib.request.urlopen(req) as f:
                if f.status != 405:
                    results[url][method] = f.status
        except URLError as err:
            if hasattr(err, 'status'):
                if err.status != 405:
                    results[url][method] = err.status


def main() -> None:
    """Runner function"""
    results = {}
    strings = reader()
    for url in strings:
        send_request(url, results)
    pp = pprint.PrettyPrinter(depth=2)
    pp.pprint(results)


if __name__ == "__main__":
    main()
