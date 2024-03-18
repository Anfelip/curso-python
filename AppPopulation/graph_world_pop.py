from utils import get_population, population_by_country
from read_csv import reader_csv
from charts import generate_bar_chart
from charts import generate_pie_chart

def run():

    data = reader_csv("world_population.csv")
    data = list(filter(lambda item : item['Continent'] == 'South America', data))

    countries = list(map(lambda x: x["Country/Territory"], data))
    percentages = list(map(lambda x: x["World Population Percentage"], data))

    generate_pie_chart(countries, percentages)

    country = input("Type Country => ")

    result= population_by_country(data, country)
    
    if len(result)>0:
        country = result[0]
        keys, values = get_population(country)
        generate_bar_chart(country['Country/Territory'], keys, values)

if __name__ == '__main__':
    run()