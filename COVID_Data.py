from covid import Covid

covid = Covid()

italy = covid.get_status_by_country_name("italy")
print(italy)

deaths = covid.get_total_deaths()
print(deaths, 'deaths')