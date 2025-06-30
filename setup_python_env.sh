#!/bin/bash

# Script pour configurer un environnement Python et installer les dépendances

set -e  # Arrête le script en cas d'erreur

echo "Mise à jour des paquets..."
sudo apt update

# Vérifie si Python 3.10 est requis, sinon utilise Python 3.12
PYTHON_VERSION="3.12"
if command -v python3.10 >/dev/null 2>&1; then
    PYTHON_VERSION="3.10"
    echo "Python 3.10 détecté, utilisation de cette version."
elif command -v python3.12 >/dev/null 2>&1; then
    PYTHON_VERSION="3.12"
    echo "Python 3.12 détecté, utilisation de cette version."
else
    echo "Installation de Python 3.10 via deadsnakes PPA..."
    sudo apt install -y software-properties-common
    sudo add-apt-repository -y ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install -y python3.10 python3.10-venv python3.10-dev python3.10-distutils
    PYTHON_VERSION="3.10"
fi

# Installation des dépendances nécessaires
echo "Installation des paquets Python nécessaires..."
sudo apt install -y python${PYTHON_VERSION} python${PYTHON_VERSION}-venv python${PYTHON_VERSION}-dev python3-full

# Création de l'environnement virtuel
echo "Création de l'environnement virtuel avec Python $PYTHON_VERSION..."
python${PYTHON_VERSION} -m venv venv

# Activation de l'environnement virtuel
echo "Activation de l'environnement virtuel..."
source venv/bin/activate

# Mise à jour de pip
echo "Mise à jour de pip..."
pip install --upgrade pip

# Installation des dépendances depuis requirements.txt
if [ -f "requirements.txt" ]; then
    echo "Installation des dépendances depuis requirements.txt..."
    pip install -r requirements.txt
else
    echo "Erreur : requirements.txt non trouvé dans le répertoire courant."
    exit 1
fi

echo "Configuration terminée ! Environnement virtuel activé avec Python $PYTHON_VERSION."
echo "Pour désactiver l'environnement virtuel, tapez 'deactivate'."
