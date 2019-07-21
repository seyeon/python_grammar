from urllib.request import urlopen
from html.parser import HTMLParser
from http.client import HTTPConnection


class ImageParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag != 'img':
            return
        if not hasattr(self, 'result'):
            self.result = []
        for name, value in attrs:
            if name == 'src':
                self.result.append(value)


def parse_image(data):
    parser = ImageParser()
    parser.feed(data)
    dataSet = set(x for x in parser.result)
    return dataSet


_url = 'www.google.co.kr'


def url_openTest():
    with urlopen(_url) as f:
        charset = f.info().get_param('charset')
        data = f.read().decode(charset)

    dataSet = parse_image(data)
    print("\n>>>>>>>>>> Fetch Image from", _url)
    # print('\n'.join(sorted(dataSet)))
    print(sorted(dataSet))


def httpconnectiontest():
    conn = HTTPConnection(_url)
    conn.request('GET', '/')
    r1 = conn.getresponse()
    print(r1.status, r1.reason())

    data1 = r1.read()
    print(data1.decode('utf-8'))


def main():
    httpconnectiontest()



def print_google_com():
    f = urlopen(_url)
    print(f.read(3064).decode('utf-8'))


if __name__ == '__main__':
    main()

