from datetime import datetime
import json
import copy


filename = "data.json"

def get_date()-> str:
    return datetime.today().strftime('%Y-%m-%d')

def extract_data(filename: str)-> dict:
    with open(filename, "r") as f:
        data = json.load(f)
    return data
 
def save_data(data: dict, filename: str)-> None:
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
        
def save_backup(data: dict, date: str)-> None:
    with open(f"./saves/{date}.json", "w") as f:
        json.dump(data, f, indent=4)

def add_set(data: dict, date: str, type: str, exercice: str, reps: int, weight: float)-> dict:
    if date not in data["data"]:
        data["data"][date] = {}
        value = copy.deepcopy(data["head"][type]["builder"])
        data["data"][date][type] = value
    data["data"][date][type][exercice]["Reps"] = reps
    data["data"][date][type][exercice]["Weight"] = weight
    data["data"][date][type][exercice]["RM"] = weight * (1 + 0.0333 * reps)
    data["head"][type]["save"][exercice]["Reps"] = reps
    data["head"][type]["save"][exercice]["Weight"] = weight
    data["head"][type]["save"][exercice]["RM"] = weight * (1 + 0.0333 * reps)

def get_data(data: dict, date: str)-> dict:
    return data["data"][date]

def get_all_exercices(data: dict)-> dict:
    return data["head"]["all_exercices"]

def get_types(data: dict)-> dict:
    return data["head"]["types"]

def get_exercices(data: dict, type: str)-> dict:
    return data["head"][type]["exercices"]

def get_save(data: dict, type: str)-> dict:
    return data["head"][type]["save"]

def main():
    run = True
    separator = "-" * 50
    data = extract_data(filename)
    today = get_date()
    while run:
        
        print(separator)
        print("Bonjour, bienvenue dans votre gestionnaire d'entrainement")
        menu = """
        1. Ajouter des données
        2. Afficher les dernières series
        3. Quitter et sauvegarder
        """
        print(menu)
        choice = input("Votre choix: ")
        print(separator)
        if choice == "1":
            print("""
                  1. Pour aujourd'hui
                  2. Pour une autre date
                  """)
            print(separator)
            choice = input("Votre choix: ")
            if choice == "1":
                date = today
                print("Pour quel type d'entrainement?")
                types = get_types(data)
                print(types)
                print("Voici les entrainements proposés")
                print(separator)
                for type in types:
                    print(type, data["head"][type]["exercices"])
                    print(separator)
                ty = input("Votre choix (U1, L1, U2): ")
                if ty not in types:
                    print("Veillez entrer un choix valide")
                    continue
            elif choice == "2":
                date = input("Entrez la date au format (AAAA-MM-JJ): ")
                if len(date) != 10:
                    print("Veillez entrer une date valide")
                    continue
                print("Pour quel type d'entrainement?")
                types = get_types(data)
                print(types)
                print("Voici les entrainements proposés")
                print(separator)
                for type in types:
                    print(type, data["head"][type]["exercices"])
                    print(separator)
                ty = input("Votre choix (U1, L1, U2): ")
                if ty not in types:
                    print("Veillez entrer un choix valide")
                    continue
            else:
                print("Veillez entrer un choix valide")
                continue
            while True:
                print(separator)
                menu = """ 
                1. Ajouter une serie
                2. Voir exerices
                3. Terminer
                """
                print(menu)
                choice = input("Votre choix: ")
                if choice == "1":
                    exercices = get_exercices(data, ty)
                    exercices_list = list(exercices.keys())
                    for exercice in exercices:
                        print(exercice)
                    exercice = input(f"Votre exercice ({exercices_list[0]}, {exercices_list[1]}, {exercices_list[2]} ): ")
                    if exercice not in exercices.keys():
                        print("Veillez entrer un choix valide")
                        continue
                    reps = int(input("Nombre de repetitions: "))
                    weight = float(input("Poids: "))
                    add_set(data, date, ty, exercice, reps, weight)
                    save_data(data, filename)
                elif choice == "2":
                    exercices = get_exercices(data, ty)
                    print(separator)
                    print(f"Voici les exercies de la séance {ty}")
                    for exercice in exercices:
                        print(f"{exercice}: {data['head'][ty]['exercices'][exercice]}")
                elif choice == "3":
                    break
                else:
                    print("Veillez entrer un choix valide")
                    print(separator)
        elif choice == "2":
            print("""Veillez choisir le type d'entrainement
                1. U1
                2. L1
                3. U2
                4. annuler
                  """)
            choice = input("Votre choix (1, 2, 3 ou 4): ")
            if choice == "1":
                print(separator)
                print("Voici les exercices de la séance U1")
                print(get_save(data, "U1"))
                print(separator)
            elif choice == "2":
                print(separator)
                print("Voici les exercices de la séance L1")
                print(get_save(data, "L1"))
                print(separator)
            elif choice == "3":
                print(separator)
                print("Voici les exercices de la séance U2")
                print(get_save(data, "U2"))
                print(separator)
            elif choice == "4":
                continue
            else:
                print("Veillez entrer un choix valide")
                
        elif choice == "3":
            print("Au revoir")
            save_data(data, filename)
            save_backup(data, today)
            run = False
        else:
            print("Veillez entrer un choix valide")

    
if __name__ == "__main__":
    main()

