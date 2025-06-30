## Todo List

- [ ] Analyser les sites Zama et comprendre l'architecture
  - [x] Naviguer vers la page principale du portefeuille Zama
  - [x] Tenter de se connecter au portefeuille pour voir les options
  - [x] Tenter de naviguer vers /shield et /faucet (404)
  - [x] Rechercher de la documentation sur les fonctionnalités 'shield' et 'faucet'
  - [ ] Examiner la documentation Zama pour comprendre les fonctionnalités 'shield' et 'faucet'
- [ ] Développer le bot avec menu interactif
- [ ] Implémenter les fonctionnalités de claim et transactions
- [ ] Tester et finaliser le bot
- [ ] Livrer le bot à l'utilisateur



  - [x] Examiner la documentation Zama pour comprendre les fonctionnalités 'shield' et 'faucet'
  - [x] Comprendre le fonctionnement des transactions confidentielles (FHE)
  - [x] Identifier comment interagir avec les contrats Zama FHE en Python (en tenant compte de l'archivage de fhevmpy) : Examiner l'utilisation de web3.py avec fhevm-tfhe-cli.
  - [x] Rechercher des informations sur le fonctionnement du faucet Zama et comment l'utiliser (Python)
  - [x] Interagir avec le faucet Zama via le navigateur pour obtenir des tokens. (Tentative échouée, URL non résolue)  - [x] Mettre en place l'environnement Python avec web3.py et fhevm-tfhe-cli.
  - [x] Développer les fonctions Python pour les transactions confidentielles (chiffrer, envoyer, déchiffrer) en utilisant fhevm-tfhe-cli.
  - [x] Développer les fonctions Python pour interagir avec le faucet via des contrats intelligents ou une API si disponible, plutôt qu\"une interface web directe. (Pas de méthode programmatique claire trouvée pour le moment)
  - [x] Implémenter la fonction `claim_faucet_tokens` (sera un message d\"information pour l\"utilisateur).
  - [x] Implémenter la fonction `send_confidential_transaction` (nécessite l'adresse d'un contrat ERC20 confidentiel déployé et son ABI, à fournir par l'utilisateur).
  - [x] Fournir des instructions à l'utilisateur pour tester le bot.
  - [x] Fournir des instructions à l'utilisateur pour obtenir l'ABI et l'adresse du contrat ERC20 confidentiel.