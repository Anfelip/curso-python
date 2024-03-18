from utils import get_population, population_by_country
from read_csv import reader_csv
from charts import generate_bar_chart
from charts import generate_pie_chart
def run():
    data = reader_csv("world_population.csv")
    country = input("Type Country => ")

    result= population_by_country(data, country)
    
    if len(result)>0:
        country = result[0]
        keys, values = get_population(country)
        generate_bar_chart(country, keys, values)
        generate_pie_chart(country, keys, values)
if __name__ == '__main__':
    run()