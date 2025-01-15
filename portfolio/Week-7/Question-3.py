def get_country_info():
    countries = {}

    while True:
        country = input("Enter the name of a country (or type 'exit' to quit): ").strip().lower()
        if country == 'exit':
            break

        if country in countries:
            print(f"The capital of {country.title()} is {countries[country]}.")
        else:
            capital = input(f"Enter the capital city of {country.title()}: ").strip()
            countries[country] = capital
            print(f"Added {country.title()} with its capital {capital}.")

    print("\nFinal list of countries and their capitals:")
    for country, capital in countries.items():
        print(f"{country.title()}: {capital}")

get_country_info()