def get_caffeine(drink):

    drinks = {
        'Coffee': '95 mg',
        'Redbull': '147 mg',
        'Tea': '11 mg',
        'Soda': '21 mg'
    }

    return drinks[drink] if drink in drinks else "Not found" 

if __name__ == "__main__":
    print(get_caffeine("Coffee"))
    print(get_caffeine("Agua sapo"))


