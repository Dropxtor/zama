from web3 import Web3
from eth_account import Account
from web3.middleware import construct_sign_and_send_raw_middleware
import subprocess
import json

# Configuration
DEVNET_URL = "https://devnet.zama.ai"
# Replace with your private key (for testing only, never hardcode in production)
PRIVATE_KEY = "YOUR_PRIVATE_KEY"

# Connect to Zama Devnet
w3 = Web3(Web3.HTTPProvider(DEVNET_URL, request_kwargs={"timeout": 600}))

# Setup account
account = Account.from_key(PRIVATE_KEY)
w3.middleware_onion.add(construct_sign_and_send_raw_middleware(account))
w3.eth.default_account = account.address

print(f"Connected to Zama Devnet: {w3.is_connected()}")
print(f"Account address: {account.address}")

# Load the Confidential ERC20 contract ABI (assuming it's compiled and ABI is available)
# For now, we'll use a placeholder. In a real scenario, you'd compile MyConfidentialERC20.sol
# and get its ABI.
# Example ABI structure (simplified):
CONTRACT_ABI = json.loads("""
[
    {
        "inputs": [],
        "name": "name",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "symbol",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "balanceOf",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]
""")

# Replace with the actual deployed contract address on Zama Devnet
CONTRACT_ADDRESS = "0x..."

# Create contract instance
# confidential_erc20_contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

# Function to encrypt data using fhevm-tfhe-cli
def encrypt_data(value: int) -> str:
    try:
        # Assuming fhevm-tfhe-cli is in your PATH
        result = subprocess.run(["fhevm-tfhe-cli", "encrypt", str(value)], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error encrypting data: {e}")
        print(f"Stderr: {e.stderr}")
        return ""

# Function to decrypt data using fhevm-tfhe-cli
def decrypt_data(encrypted_value: str) -> str:
    try:
        result = subprocess.run(["fhevm-tfhe-cli", "decrypt", encrypted_value], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error decrypting data: {e}")
        print(f"Stderr: {e.stderr}")
        return ""

# Placeholder for Faucet interaction
def claim_faucet_tokens():
    print("La réclamation de jetons du Faucet ne peut pas être automatisée pour le moment via une API ou un contrat intelligent connu.")
    print("Veuillez visiter https://portfolio.demo.zama.ai/faucet manuellement pour réclamer des jetons si le site fonctionne.")

# Placeholder for confidential transaction
def send_confidential_transaction():
    print("Fonctionnalité d'envoi de transaction confidentielle à implémenter.")
    print("Nécessite l'adresse du contrat ERC20 confidentiel et l'ABI.")
    print("Exemple: confidential_erc20_contract.functions.transfer(recipient_address, encrypted_amount).transact({'from': account.address})")

# Main interactive menu
def main_menu():
    while True:
        print("\n--- Menu Principal du Bot Zama ---")
        print("1. Vérifier la connexion et l'adresse du compte")
        print("2. Chiffrer une valeur")
        print("3. Déchiffrer une valeur")
        print("4. Réclamer des jetons du Faucet")
        print("5. Envoyer une transaction confidentielle")
        print("6. Quitter")

        choice = input("Entrez votre choix: ")

        if choice == "1":
            print(f"Connecté au Devnet Zama: {w3.is_connected()}")
            print(f"Adresse du compte: {account.address}")
        elif choice == "2":
            try:
                value_to_encrypt = int(input("Entrez la valeur entière à chiffrer: "))
                encrypted = encrypt_data(value_to_encrypt)
                if encrypted:
                    print(f"Valeur chiffrée: {encrypted}")
            except ValueError:
                print("Valeur entière invalide.")
        elif choice == "3":
            encrypted_string = input("Entrez la chaîne chiffrée à déchiffrer: ")
            decrypted = decrypt_data(encrypted_string)
            if decrypted:
                print(f"Valeur déchiffrée: {decrypted}")
        elif choice == "4":
            claim_faucet_tokens()
        elif choice == "5":
            send_confidential_transaction()
        elif choice == "6":
            print("Fermeture du Bot Zama.")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main_menu()


