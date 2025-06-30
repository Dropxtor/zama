# fhEVM Python SDK

Créer le script :
```bash

nano setup_python_env.sh
```
Copiez-collez le script ci-dessus, sauvegardez (Ctrl+O, Enter, Ctrl+X).

Rendre le script exécutable :
```bash

chmod +x setup_python_env.sh
```
Exécuter le script :
```bash

./setup_python_env.sh
```

    

For now we also need to installed the fhEVM cli (which in turn requires [Rust]() to be installed):

    git clone https://github.com/zama-ai/fhevm-tfhe-cli
    cd fhevm-tfhe-cli
    cargo install --path .
    

Setting up Web3:

```python
from web3 import Web3

w3 = Web3(Web3.HTTPProvider(devnet_url, request_kwargs={"timeout": 600}))
```

Setting up a wallet (with private key):

```python
from eth_account import Account
from web3.middleware import construct_sign_and_send_raw_middleware

account = Account.from_key(signature_key)
w3.middleware_onion.add(construct_sign_and_send_raw_middleware(account))
w3.eth.default_account = account.address
```

Setting up the SDK:

```python
from fhevm import FHEVM

fhevm = FHEVM(w3, account)
```

Encrypting an input:

```python
amount = fhevm.encrypt32(args.amount)
```

Calling a view function:

```python
public_key, signature = fhevm.generate_auth_token(contract.address)
encrypted_value = contract.functions.viewFunction(public_key, signature).call({"from": account.address})
value = fhevm.open(encrypted_value)
```

