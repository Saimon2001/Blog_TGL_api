import requests

def fetch_data_from_external_api():
    response = requests.get("https://restcountries.com/v3.1/all")
    data = response.json()
    #print(data)
    return data

def extract_data( country_list ):
    new_list = list()
    for country in country_list:
        
        language_names = [] 
        try:
            for language_code, language_name in country['languages'].items():
                language_names.append(language_name)  
        except Exception as e:
            language_names.append('none')
            
        try:
            for year, value in country['gini'].items():
                gini = value 
        except Exception as e:
            gini = 0

        
        id = country['altSpellings'][0]
        name_common = country['name']['common']
        name_official = country['name']['official']
        independent = country.get('independent', None)
        languages = ",".join(language_names)
        region = country['region']
        subregion = country.get('subregion', None)
        flag_svg = country['flags']['svg']
        flag_icon = country['flag']
        population = country['population']
        gini = gini
        
        
        new_list.append([
            id, name_common, name_official,
            independent, region, subregion, flag_svg,
            flag_icon, population, languages, gini])
    
    print(new_list[0])
    return new_list
