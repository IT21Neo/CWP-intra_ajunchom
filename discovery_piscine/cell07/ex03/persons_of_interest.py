def famous_births(historical_figures):
    sorted_figures = sorted(historical_figures.items(), key=lambda item: item[1]["date_of_birth"])

    for key, person in sorted_figures:
        print("{} is a great scientist born in {}.".format(person["name"], person["date_of_birth"]))

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)