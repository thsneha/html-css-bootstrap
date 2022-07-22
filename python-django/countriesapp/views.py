import json
with open("countries.json","r",encoding="utf8") as f:
    data=json.load(f)
print(len(data))

country_names=[country["name"] for country in data]
print(country_names)
def get_country_details_by_name(cname):
    global data
    data=[country for country in data if country["name"]==cname]
    return data
print(get_country_details_by_name('Albania'))

def get_currency_by_countryname(cname):
    cname=[country["currencies"][0]["name"]for country in data if country["name"]==cname]
    return cname
print(get_currency_by_countryname("Albania"))

def get_languages_by_country(cname):
    return[lang["name"]for country in data for lang in country["languages"] if country["name"]==cname]
print(get_languages_by_country("Albania"))