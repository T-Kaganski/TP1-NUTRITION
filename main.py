<<<<<<< HEAD
################################################################
#                      TP1 NUTRITION_CSV                       #
#           par Tal Kaganski, Brandon Arsenault-Henry          #
#                   et Guillaume Crête                         #
################################################################

def caseMain():
    choix = ["1", "2", "3", "4", "5", "6"]  # liste des choix possibles
    menu()

    titre = input("Choisissez une option: ")

    if titre in choix:  # Vérifie dans la liste de choix si l'entrée est valide
        match titre:
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass
            case '4':
                pass
            case '5':
                pass
            case '6':
                print("Voulez-vous quitter?")
                if input("oui"):
                    print("Au revoir!")
                else:
                    pass

def menu():
        print("************************************************************************")
        print("**                                                                    **")
        print("**     BIENVENUE DANS L'APPLICATION DE MODIFICATION DE TABLEAU        **")
        print("**                                                                    **")
        print("************************************************************************")
        print("1 - Afficher l'ensemble des aliments depuis le fichier Nutrition.csv")
        print("2 - Afficher les aliments en fonction d'une valeur nutritive a la fois")
        print("3 - Afficher les valeurs nutritives d'un aliment (Recherche par ID)")
        print("4 - Modifier une valeur nutritive d'un aliment (par ID)")
        print("5 - Ajouter un aliment")
        print("6 - Quitter")
        print("************************************************************************")


=======
################################################################
#                      TP1 NUTRITION_CSV                       #
#           par Tal Kaganski, Brandon Arsenault-Henry          #
#                   et Guillaume Crête                         #
################################################################

def caseMain():
    choix = ["1", "2", "3", "4", "5", "6"]  # liste des choix possibles
    menu()

    titre = input("Choisissez une option: ")

    if titre in choix:  # Vérifie dans la liste de choix si l'entrée est valide
        match titre:
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass
            case '4':
                pass
            case '5':
                pass
            case '6':
                print("Voulez-vous quitter?")
                if input("oui"):
                    print("Au revoir!")
                else:
                    pass

def menu():
        print("************************************************************************")
        print("**                                                                    **")
        print("**     BIENVENUE DANS L'APPLICATION DE MODIFICATION DE TABLEAU        **")
        print("**                                                                    **")
        print("************************************************************************")
        print("1 - Afficher l'ensemble des aliments depuis le fichier Nutrition.csv")
        print("2 - Afficher les aliments en fonction d'une valeur nutritive a la fois")
        print("3 - Afficher les valeurs nutritives d'un aliment (Recherche par ID)")
        print("4 - Modifier une valeur nutritive d'un aliment (par ID)")
        print("5 - Ajouter un aliment")
        print("6 - Quitter")
        print("************************************************************************")


>>>>>>> afbd48e542b1411346dede9bf8182dc87ed215ca
caseMain()