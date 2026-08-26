# PassMan

PassMan is a small command-line password manager written in Python. It keeps account details in a local SQLite database and encrypts saved passwords before storing them. There is no cloud service or remote account: your vault stays on the machine where PassMan runs.

This is an educational project for exploring password storage, authenticated encryption, and SQLite-backed CLI applications. It is not intended to replace a production password manager.

## Features

- Add accounts with a website, email, username, and password
- View a saved password after providing the website, email, and master key
- Edit an existing password after verification
- Delete an account after verification
- Create the local database automatically on first use

## Requirements

- Python 3.12 or newer
- pip

## Installation

Create and activate a virtual environment, then install the project dependencies.

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
```

### macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

## Run PassMan

After installation, start the interactive CLI with:

```bash
passman
```

You can also run the module directly:

```bash
python -m pas_man.main
```

At the `<Pas-Man>` prompt, use one of these commands:

| Command | Action |
| --- | --- |
| `add` | Create a new account entry |
| `show` | Find and decrypt an account password |
| `edit` | Replace an existing password |
| `del` | Delete an account entry |
| `exit` | Close the application |

### Basic workflow

1. Run `passman` and enter `add`.
2. Provide the website, email, username, and password.
3. Enter a master key. PassMan uses it to encrypt the password.
4. Later, use `show` with the same website, email, and master key to display the password.

## Encryption and storage

For each password, PassMan:

1. Generates a random salt.
2. Derives a 32-byte encryption key from the master key with Argon2id.
3. Encrypts the password with AES-GCM and a random nonce.
4. Stores the encrypted value, salt, and nonce in SQLite.

The website, email, username, and dates are stored as database metadata and are not encrypted. The database is created automatically at:

```text
pas_man/db/main.db
```

## Development

Run the tests with:

```bash
python -m pytest -q
```

The repository contains tests for input validation and encryption/decryption behavior.

## Security warning

PassMan is a learning-focused utility with a simple security model. Use it only with data you are comfortable storing locally, choose a strong master key, and keep backups of the database. Do not treat it as a production-grade password manager.

## Project structure

- `pas_man/main.py` - interactive CLI and command handlers
- `pas_man/cipher.py` - Argon2id key derivation and AES-GCM encryption
- `pas_man/db.py` - SQLite connection and table creation
- `pas_man/db_read.py` - database reads
- `pas_man/db_write.py` - inserts, updates, and deletes
- `pas_man/validate.py` - input and credential validation