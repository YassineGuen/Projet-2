import pandas as pd
import os

# Constantes 
LIGNE_INITIALE = 18967
FIN_RODAGE_ELO = 23967
ELO_INITIAL = 1500 # Pourquoi 1500
K = 24 # Pourquoi 24

def existence_fichier(fichier):
    """
    Cette fonction vérifie si un fichier existe.

    fichier: Chemin vers le fichier CSV à vérifier
    La fonction retourne True si le fichier existe, sinon elle lève une exception.
    """

    if not os.path.isfile(fichier):
        raise FileNotFoundError(f"Le fichier {fichier} n'existe pas.")
    return True



def nettoyer_donnees(fichier_csv, lignes_a_supprimer):
    """
    Cette fonction lit un fichier CSV pour en nettoyer les données. Les entrées les plus anciennes sont supprimées,
    les lignes avec des valeurs manquantes sont retirées, et les doublons sont éliminés aussi. 

    fichier_csv: Chemin vers le fichier CSV à nettoyer
    lignes_a_supprimer: Nombre de lignes à supprimer depuis le début du fichier
    La fonction retourne un DataFrame contenant les données nettoyées.
    """

    #Vérifier l'existence du fichier CSV
    existence_fichier(fichier_csv)

    # Lire le fichier CSV
    df = pd.read_csv(fichier_csv)

    # Retirer les lignes en trop
    df_clean = df.iloc[lignes_a_supprimer:]

    # Supprimer les lignes avec des valeurs manquantes
    df_clean = df_clean.dropna()

    # Supprimer les doublons
    df_clean = df_clean.drop_duplicates()

    return df_clean




def probaba_elo(player1_elo, player2_elo):
    """
    Cette fonction calcule la probabilité de victoire d'un joueur par rapport à un autre en utilisant le score ELO.

    player1_elo: Score ELO du joueur 1
    player2_elo: Score ELO du joueur 2
    La fonction retourne la probabilité de victoire du joueur 1.
    """

    # Calculer la probabilité de victoire du joueur 1
    prob_player1 = 1 / (1 + 10 ** ((player2_elo - player1_elo) / 400))
    
    return prob_player1




def elo_calculer(df):
    """
    Cette fonction calcule le score ELO pour chaque joueur dans le DataFrame.

    df: DataFrame contenant les données des joueurs
    La fonction retourne un DataFrame avec une colonne supplémentaire pour le score ELO.
    """

    pass

    return df