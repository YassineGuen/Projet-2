import pandas as pd
import os

def existence_fichier(fichier_csv):
    """
    Cette fonction vérifie si un fichier CSV existe.

    fichier_csv: Chemin vers le fichier CSV à vérifier
    La fonction retourne True si le fichier existe, sinon elle lève une exception.
    """

    if not os.path.isfile(fichier_csv):
        raise FileNotFoundError(f"Le fichier {fichier_csv} n'existe pas.")
    return True







def nettoyer_donnees(fichier_csv):
    """
    Cette fonction lit un fichier CSV, nettoie les données en supprimant les valeurs manquantes
    et les doublons, puis retourne un DataFrame pandas propre.

    fichier_csv: Chemin vers le fichier CSV à nettoyer
    La fonction retourne un DataFrame contenant les données nettoyées.
    """

    #Vérifier l'existence du fichier CSV
    existence_fichier(fichier_csv)

    
    # Lire le fichier CSV
    df = pd.read_csv(fichier_csv)

    # Retirer les lignes en trop
    df_clean = df.iloc[18968:]

    # Supprimer les lignes avec des valeurs manquantes
    df_clean = df_clean.dropna()

    # Supprimer les doublons
    df_clean = df_clean.drop_duplicates()

    print(df_clean)

print(nettoyer_donnees("atp_tennis-selected-columns.csv"))

