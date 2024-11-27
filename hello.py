from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs

def main():
    req = Request(
    url='https://glints.com/id/job-category/administrative-human-resources', 
    headers={'User-Agent': 'Mozilla/5.0'}
)
    webpage = urlopen(req).read()
    print(webpage)


if __name__ == "__main__":
    main()
