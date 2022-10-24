## COUNTRIES FUNCTIONS


from matplotlib.pyplot import phase_spectrum


def country_info(iso, info="name.common"):
    '''
    Function that uses Rest Countries API to retrieve country information
    - iso: string, ISO code (2 or 3 letters) of the country
    - info: string, information to be retrieved separated by a ".", Default `name.common` 
    - In case of error prints the HTTP response and returns None
    '''
    if "requests" not in dir():
        import requests
    info = info.split(".")
    url = f"https://restcountries.com/v3.1/alpha/{iso}"
    call = requests.get(url)
    json = call.json()[0]
    status = call.status_code
    if status == 200:
        response = "json"
        for e in info:
            response = response + "['" + e + "']"
        return eval(response)
    else:
        print(f"Error retriving {iso} information (http response = {status})")
        return None

def booking_country(country):
    if "requests" not in dir():
        import requests
    if "BeautifulSoup" not in dir():
        from bs4 import BeautifulSoup
    '''
    Function to scrape the number of hotels in the booking.com platform for a given country
    * The country has to be given in 2 letters ISO code
    * If the landing page of a country does not exist (404 error) return 0
    * If there's any error in the scraping returns None
    * Prints a description if there is an error (no hotels, HTTP error or page not found)
    '''
    url = f"https://www.booking.com/country/{country.lower()}.html"
    html = requests.get(url)
    if html.status_code == 200:
        soup = BeautifulSoup(html.content, "html.parser")
        text = soup.select("h2.sb-searchbox__subtitle-text")[0].getText()
        number =""
        for i in text:
            if i.isdigit():
                number = number + i
        if number:
            number = int(number)
        else:
            number = 0
            print(f"No hotels found in {country_info(country)}")
    elif html.status_code == 404:
        number = 0
        print(f"The page of {country_info(country)} doesn't exist on booking.com or it isn't considered as country")
    else:
        number= None
        print(f"There was a problem getting the information for {country_info(country)}, HTTP code {html.status_code}")
    return number

## CITIES FUNCTIONS
def bing_url(city, country):
    if "re" not in dir():
        import re
    if "requests" not in dir():
        import requests
    if "BeautifulSoup" not in dir():
        from bs4 import BeautifulSoup
    url = f"https://www.bing.com/search?q={city}+booking"
    custom_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
    req = requests.get(url, headers={"User-Agent": custom_user_agent})
    soup = BeautifulSoup(req.content, "html.parser")
    url_list = re.findall(f'https:\/\/www.booking.com\/city\/{country}\/[^"]*html', str(soup))
    if url_list:
        return url_list[0]
    else:
        return None 

def booking_city(city, country, region=False):
    '''
    Function name and scrape the number of hotels in the booking.com platform for a given city or region
    * The city has to be given as a string in english
    * If the city parameter it's a region, region prameter has to be set to True (Default False)
    * If the landing page of a city does not exist (404 error) checks if it's a region
    * If it is not a region (301 redirect) prints a notice (must be confirmed by google).
    * If there is no landing page in google search set the number to 0.
    * If there's any error in the scraping returns None.
    '''
    if "requests" not in dir():
        import requests
    if "BeautifulSoup" not in dir():
        from bs4 import BeautifulSoup
    if "unidecode" not in dir():
        from unidecode import unidecode
    city2 = unidecode(city, "utf-8")
    city2 = city2.replace(" ", "-")
    number =""
    url = f"https://www.booking.com/city/{country.lower()}/{city2.lower()}.html"
    url2 = f"https://www.booking.com/region/{country.lower()}/{city2.lower()}.html"
    if region:
        html = requests.get(url2, allow_redirects= False)
    else:
        html = requests.get(url, allow_redirects= False)
    if html.status_code == 200:
        soup = BeautifulSoup(html.content, "html.parser")
        if region:
            try:
                text = soup.select("h2.sb-searchbox__subtitle-text")[0].getText()
                for i in text:
                    if i.isdigit():
                        number = number + i
            except:
               print(f"Problem scrapping url: https://www.booking.com/region/{country.lower()}/{city2.lower()}.html")
               return None     
        else:
            try:
                text = soup.select("div.sr-snippet_header_num_properties")[0].getText()
                for i in text:
                    if i.isdigit():
                        number = number + i
            except:
                return 0
        if number:
            number = int(number)
        else:
            number = 0
            print(f"No hotels found in {city}")

    elif html.status_code == 404 and not region:
        return booking_city(city, country, region=True)
    elif html.status_code == 301:
        url3 = bing_url(city.lower(), country.lower())
        if url3:
            try:
                html2 = requests.get(url3, allow_redirects= False)
                soup2 = BeautifulSoup(html2.content, "html.parser")
                text = soup2.select("div.sr-snippet_header_num_properties")[0].getText()
                for i in text:
                    if i.isdigit():
                        number = number + i
            except:
                print(f"No hotels found in {city}")
                return 0
        else:
            print(f"No hotels found in {city}")
            number= 0
    else:
        number= None
        print(f"There was a problem getting the information for {city}, HTTP code {html.status_code}")
    return number

def clean_city(name):
    '''
    Function that cleans the names of the cities
    '''
    name.replace("-", "")
    if "/" in name:
        name = name.split("/")[0]
    if "(" in name:
         name = name.split("(")[0]
    return name.strip()

def cities_country (df, country):
    '''
    Function to Group cities by country, clean name and add booking data
    '''
    df = df[df.country == country]
    newdf = df.groupby(['city'], as_index=False).agg({"country": 'first', 'countryisocode' : 'first', 'hotel_id': 'count', "longitude": "mean", "latitude": "mean"})
    newdf['city'] = newdf['city'].apply(clean_city)
    newdf.rename(columns={'hotel_id': 'agoda_num'}, inplace=True, errors='raise')
    newdf["booking_num"] = newdf.apply(lambda x: booking_city(x["city"], x["countryisocode"]), axis=1)
    try: 
        newdf.booking_num = newdf.booking_num.astype("int64")
    except:
        newdf = newdf.dropna(axis = 0, how = 'any')
        newdf.booking_num = newdf.booking_num.astype("int64")
        newdf = newdf.reset_index()
        print("Some cities that generate a scrapping error have been eliminated")
    return newdf
