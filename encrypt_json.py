import csv
import json
import random
import hashlib

ORIGINS = ['BOG', 'CTG', 'MDE']
DESTINITAIONS = ['BOG', 'CTG', 'MDE']
LANGUAGES = ['ES', 'EN']
CURRENCIES = ['COP', 'USD']


def save_json_to_csv(json_data):
    """Guarda la informacion contenida en un json en un archivo con un nombre unico.

    Args:
        json_data (_type_): json que contiene la informacion.
    """
    csv_filename = "encrypted_json.csv"

    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Strings"])
        writer.writerow([json_data])



def create_random_json(number_jsons:int):
    """Funcion que crea un json apartir de las listas creadas al principio del codigo.

    Args:
        number_jsons (int): Recibe un numero entero que indica la cantidad de jsons a crear.
    """
    array_of_json = []
    for iteration in range(1, number_jsons + 1):
        random_json = {
            "currency": random.choice(CURRENCIES),
            "originCity": random.choice(ORIGINS),
            "destinationCity": random.choice(DESTINITAIONS),
            "module": "IBE",
            "language": random.choice(LANGUAGES),
            "radixToken": "null",
            "promotionCode": "null",
        }
        encrypted_info = hashlib.sha1(json.dumps(random_json).encode()).hexdigest()
        array_of_json.append(encrypted_info)

    long_json = []
    for random_json in array_of_json:
        random_dict = {"encrypted_info":random_json}
        long_json.append(random_dict)
    print(long_json)
    save_json_to_csv(long_json)


if __name__ == "__main__":
    create_random_json(3)
