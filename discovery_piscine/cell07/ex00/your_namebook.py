def array_of_names(persons):
    full_names = []
    
    for first_name, last_name in persons.items():
        formatted_name = "{} {}".format(first_name.capitalize(), last_name.capitalize())
        full_names.append(formatted_name)
        
    return full_names

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))