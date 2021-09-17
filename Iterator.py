from pprint import pprint
import json

def iterator(countries):
    country_number = 0
    while country_number < len(countries):
        yield countries[country_number]['name']['common']
        country_number += 1


if __name__ == '__main__':

    HOST = 'https://wikipedia.org/wiki/'
    my_dict = {}

    with open(r"countries.json", encoding="utf-8") as f:
        file_content = f.read()
        countries = json.loads(file_content)

    for country in iterator(countries):
        my_dict[country] = str(HOST + country.replace(" ", "_"))

    pprint(my_dict)

    with open('countries&links.json', 'w') as f:
        f.write(json.dumps(my_dict))

