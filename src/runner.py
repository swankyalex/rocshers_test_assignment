import urllib.request
from urllib.parse import urlparse
from urllib.error import URLError
from pprint import PrettyPrinter

from .consts import HTTP_METHODS


class HttpRequester:
    def __init__(self):
        self.strings = []
        self.results = {}

    def reader(self) -> None:
        """Reading data from stdin"""
        while True:
            string = input("Введите ссылку: ")
            if string == '':
                break
            if self.check_string(string):
                self.strings.append(string)
            else:
                print(f'Строка {string} не является ссылкой')

    def send_request(self, url: str) -> None:
        """Sending HTTP requests to provided link"""
        self.results[url] = {}
        for method in HTTP_METHODS:
            req = urllib.request.Request(url=url, method=method)
            try:
                with urllib.request.urlopen(req) as f:
                    if f.status != 405:
                        self.results[url][method] = f.status
            except URLError as err:
                if hasattr(err, 'status'):
                    if err.status != 405:
                        self.results[url][method] = err.status

    @staticmethod
    def check_string(string: str) -> bool:
        """Checking if provided string is a correct link"""
        return True if urlparse(string).scheme else False

    def runner(self):
        """Runner function"""
        self.reader()
        for url in self.strings:
            self.send_request(url)
        PrettyPrinter(depth=2).pprint(self.results)


def main() -> None:
    http_requester = HttpRequester()
    http_requester.runner()


if __name__ == "__main__":
    main()
