from bs4 import BeautifulSoup
import requests
import json

count = 1
quote_dict = {}

for pageNumber in range(1, 11):

    URL = f"https://quotes.toscrape.com/page/{pageNumber}"
    resp = requests.get(URL)
    if resp.status_code == 200:
        print("Connection Successufull")
    else:
        print("There was an error, Status Code: ", resp.status_code)

    htmlContent = resp.content
    htmlContent

    soup = BeautifulSoup(htmlContent, 'html')
    soup

    AllQuotes = soup.find_all('div', class_="quote")
    AllQuotes

    for Quotes in AllQuotes:

        quote = Quotes.find('span', class_="text")

        author = Quotes.find('small', class_='author')

        index = f'Quote {count}'
        quote_dict[index] = {
            'Quote': quote.contents[0],
            'Author': author.contents[0]
        }

        count += 1


with open("D:\\EduNet\\NSTI_Indore25_26\\Python\\WebPagePython\\Quotes.json", "w") as jsonFile:
    json.dump(quote_dict, jsonFile)
