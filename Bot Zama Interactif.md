# Bot Zama Interactif

Ce bot Python vous permet d'interagir avec le Devnet Zama pour chiffrer/déchiffrer des valeurs et simuler des interactions avec un faucet et des transactions confidentielles.

## Prérequis

Avant d'utiliser ce bot, assurez-vous d'avoir les éléments suivants installés sur votre système. Les commandes d'installation sont fournies pour les systèmes basés sur Debian/Ubuntu. Pour d'autres distributions Linux ou systèmes d'exploitation, veuillez consulter leur documentation respective.

-   **Python 3.10 ou une version ultérieure** (la version 3.11 est utilisée dans cet environnement, mais des versions plus récentes devraient également fonctionner. `fhevmpy` mentionnait Python 3.10 comme recommandé, mais `fhevm-tfhe-cli` est un outil Rust et n'a pas cette restriction directe).
    ```bash
    # Vérifier la version de Python
    python3 --version
    # Si Python n'est pas installé ou est une version plus ancienne, vous pouvez l'installer via apt:
    sudo apt-get update
    sudo apt-get install -y python3.11 python3-pip
    ```
-   **`pip`**: Le gestionnaire de paquets de Python. Il est généralement inclus avec l'installation de Python 3. Si ce n'est pas le cas, vous pouvez l'installer séparément.
    ```bash
    # Vérifier si pip est installé
    pip3 --version
    # Si pip n'est pas installé
    sudo apt-get install -y python3-pip
    ```
-   **`git`**: Un système de contrôle de version, nécessaire pour cloner les dépôts GitHub.
    ```bash
    sudo apt-get update
    sudo apt-get install -y git
    ```
-   **`curl`**: Un outil en ligne de commande pour transférer des données avec des URL. Il est souvent préinstallé sur les systèmes Linux.
    ```bash
    sudo apt-get update
    sudo apt-get install -y curl
    ```
-   **`build-essential`**: Un paquet qui contient les outils de compilation nécessaires (comme `gcc`, `g++`, `make`) pour compiler des logiciels à partir du code source, y compris les projets Rust.
    ```bash
    sudo apt-get update
    sudo apt-get install -y build-essential
    ```
-   **`Rust` et `Cargo`**: Le langage de programmation Rust et son gestionnaire de paquets/système de construction. `fhevm-tfhe-cli` est écrit en Rust et nécessite ces outils pour être compilé et installé. L'installation de Rust/Cargo est détaillée dans la section suivante.

## Installation

Suivez ces étapes pour configurer votre environnement et le bot:

1.  **Cloner le dépôt `fhevm-tfhe-cli` et installer Rust/Cargo:**

    `fhevm-tfhe-cli` est un outil en ligne de commande développé par Zama pour interagir avec les fonctionnalités de chiffrement/déchiffrement de fhEVM. Vous pouvez trouver le dépôt sur [GitHub](https://github.com/zama-ai/fhevm-tfhe-cli).

    Exécutez les commandes suivantes dans votre terminal. Ces commandes vont d'abord installer Rust et Cargo, puis cloner le dépôt `fhevm-tfhe-cli` et enfin compiler et installer l'outil.

    ```bash
    # Installer Rust et Cargo
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
    # Charger les variables d'environnement de Cargo pour que 'cargo' soit reconnu
    source "$HOME/.cargo/env"
    # Mettre à jour les paquets du système et installer build-essential (nécessaire pour la compilation Rust)
    sudo apt-get update
    sudo apt-get install -y build-essential
    # Cloner le dépôt fhevm-tfhe-cli
    git clone https://github.com/zama-ai/fhevm-tfhe-cli
    # Naviguer dans le dossier du dépôt et installer l'outil
    cd fhevm-tfhe-cli
    cargo install --path .
    # Revenir au répertoire précédent
    cd ..
    ```

2.  **Installer les dépendances Python:**

    Le bot utilise `web3.py` pour interagir avec la blockchain Ethereum (et donc le Devnet Zama compatible EVM), `eth-account` pour la gestion des comptes et la signature des transactions, et `py-solc-x` pour la compilation des contrats Solidity.
    -   `web3.py`: [Documentation officielle](https://web3py.readthedocs.io/en/stable/)
    -   `eth-account`: Fait partie de la suite `web3.py`.
    -   `py-solc-x`: [Documentation PyPI](https://pypi.org/project/py-solc-x/)

    Exécutez la commande suivante pour les installer:

    ```bash
    pip install web3 eth-account py-solc-x
    ```

3.  **Mettre à jour le fichier `zama_bot.py`:**

    Ouvrez le fichier `zama_bot.py` dans votre éditeur de texte préféré. Vous devrez y apporter deux modifications importantes:

    -   **Votre clé privée**: Remplacez `YOUR_PRIVATE_KEY` par votre clé privée Ethereum. **ATTENTION: Ne partagez jamais votre clé privée et ne l'utilisez pas pour des fonds réels sur un réseau principal.** Ce bot est conçu à des fins de test uniquement sur le Devnet Zama. Pour générer une clé privée de test, vous pouvez utiliser des outils comme `ganache` ou des bibliothèques comme `eth-account`.

        ```python
        PRIVATE_KEY = "VOTRE_CLÉ_PRIVÉE_ICI" # Exemple: "0x..."
        ```

    -   **Adresse et ABI du contrat ERC20 confidentiel (Optionnel)**: Si vous prévoyez d'utiliser la fonctionnalité d'envoi de transactions confidentielles, vous devrez avoir déployé un contrat ERC20 confidentiel sur le Devnet Zama. Une fois déployé, mettez à jour `CONTRACT_ADDRESS` avec l'adresse de votre contrat et `CONTRACT_ABI` avec l'ABI (Application Binary Interface) de votre contrat. L'ABI est une description JSON des fonctions et événements du contrat.

        ```python
        CONTRACT_ADDRESS = "0x...VOTRE_ADRESSE_DE_CONTRAT_DÉPLOYÉ..."
        CONTRACT_ABI = json.loads("""
        [...VOTRE_ABI_DE_CONTRAT_JSON_ICI...]
        """)
        ```
        Pour obtenir l'ABI de votre contrat, vous devrez le compiler (par exemple, avec Hardhat ou Remix) et récupérer le fichier JSON de l'ABI.

## Utilisation du Bot

Pour lancer le bot, exécutez la commande suivante dans votre terminal:

```bash
python zama_bot.py
```

Un menu interactif s'affichera, vous permettant de choisir différentes actions:

-   **Vérifier la connexion et l'adresse du compte:** Confirme que le bot est connecté au Devnet Zama et affiche l'adresse de votre compte.
-   **Chiffrer une valeur:** Utilise `fhevm-tfhe-cli` pour chiffrer une valeur entière que vous fournissez. La valeur chiffrée sera affichée.
-   **Déchiffrer une valeur:** Utilise `fhevm-tfhe-cli` pour déchiffrer une chaîne chiffrée que vous fournissez. La valeur déchiffrée sera affichée.
-   **Réclamer des jetons du Faucet:** Cette fonction affichera un message vous informant que la réclamation de jetons via le bot n'est pas possible pour le moment. Vous devrez visiter manuellement le faucet Zama si une interface web est disponible et fonctionnelle. L'URL du faucet Zama est généralement [https://faucet.zama.ai/](https://faucet.zama.ai/), mais elle a été inaccessible lors de la création de ce bot.
-   **Envoyer une transaction confidentielle:** Cette fonction est un espace réservé. Pour qu'elle fonctionne, vous devrez avoir déployé un contrat ERC20 confidentiel sur le Devnet Zama et fourni son adresse et son ABI dans le fichier `zama_bot.py`.
-   **Déployer un contrat ERC20 confidentiel:** Cette option vous permet de déployer un contrat `MyConfidentialERC20.sol` (fourni avec le bot) sur le Devnet Zama. Le bot vous demandera le nom du token, son symbole et l'approvisionnement initial. Après un déploiement réussi, l'adresse et l'ABI du contrat seront automatiquement mises à jour dans le bot pour les transactions confidentielles. Assurez-vous que le fichier `MyConfidentialERC20.sol` est présent dans le même répertoire que `zama_bot.py`.

## Informations sur le Faucet et les Transactions Confidentielles

### Faucet Zama

Actuellement, l'interaction programmatique avec le faucet Zama n'a pas été clairement identifiée. La page web du faucet (`https://faucet.zama.ai/`) semble ne pas être résolue ou accessible directement. Si vous souhaitez obtenir des jetons de test, veuillez vérifier la documentation officielle de Zama ou leurs canaux communautaires pour la méthode la plus récente et fonctionnelle.

### Transactions Confidentielles (ERC20 Confidentiel)

Pour envoyer des transactions confidentielles, vous devez interagir avec un contrat ERC20 confidentiel déployé sur le Devnet Zama. Vous devrez:

1.  **Déployer votre propre contrat ERC20 confidentiel:** Zama fournit des exemples et des modèles (par exemple, le [dépôt `fhevm-hardhat-template` sur GitHub](https://github.com/zama-ai/fhevm-hardhat-template) avec `MyConfidentialERC20.sol`) qui peuvent être utilisés pour déployer un tel contrat. Suivez leur documentation pour le déploiement, notamment la section [Hardhat dans la documentation fhEVM](https://docs.zama.ai/fhevm/getting-started/overview-1/hardhat).
2.  **Obtenir l'adresse du contrat et l'ABI:** Une fois votre contrat déployé, vous obtiendrez son adresse et son Application Binary Interface (ABI). L'ABI est une description JSON des fonctions et événements du contrat. Vous pouvez généralement la trouver dans le dossier `artifacts` après la compilation de votre contrat Hardhat.
3.  **Mettre à jour `zama_bot.py`:** Collez l'adresse du contrat et l'ABI dans les variables `CONTRACT_ADDRESS` et `CONTRACT_ABI` du fichier `zama_bot.py`.

Une fois ces étapes effectuées, vous pourrez implémenter la logique d'envoi de transactions confidentielles dans la fonction `send_confidential_transaction` en utilisant l'instance du contrat et les fonctions de chiffrement fournies par `fhevm-tfhe-cli`.


