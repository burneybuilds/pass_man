# PassMan

PassMan is a lightweight local password manager built as a CLI learning project. It stores account metadata and encrypted passwords in a local SQLite database, using a user-supplied master key to derive an encryption key with Argon2id and encrypt data with AES-GCM.

## What it does

- Store a password entry for a website/service
- Save the associated website name, email, and username
- Encrypt each password before saving it
- Retrieve and decrypt stored passwords using the master key
- Manage entries from the command line
- Keep everything local on the machine, with no remote service

## Project overview

This project is intentionally small and focused on the core mechanics of password storage:

- `pas_man/main.py` contains the interactive CLI loop and command handlers
- `pas_man/cipher.py` handles key derivation and encryption/decryption
- `pas_man/db.py` creates the SQLite database and table if needed
- `pas_man/db_read.py` fetches stored records
- `pas_man/db_write.py` inserts, updates, and deletes entries
- `pas_man/validate.py` validates inputs and checks master-key/password correctness

## How encryption works

The project uses a two-step flow:

1. The user provides a master key.
2. That master key is transformed with Argon2id using a random salt.
3. The derived key is used with AES-GCM to encrypt the password.
4. The ciphertext, salt, and nonce are stored in the SQLite database.

When a password is retrieved, the same master key and stored salt are used to derive the key again, then AES-GCM decrypts the value.

## Setup

### Prerequisites

- Python 3.12+
- pip

### Install dependencies

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

## Running the app

After installation, you can start the CLI with:

```bash
passman
```

You can also run it directly:

```bash
python -m pas_man.main
```

## CLI commands

The interactive menu supports these commands:

- `show` — show a stored password for a website/email pair
- `add` — add a new password entry
- `del` — delete a stored entry
- `edit` — update a password entry
- `exit` — leave the program

### Example flow

1. Run `passman`
2. Choose `add`
3. Enter:
   - website name
   - email
   - username
   - password
   - master key
4. The program stores the encrypted password and metadata in the SQLite database

To retrieve it later:

1. Run `passman`
2. Choose `show`
3. Enter the website name, email, and master key
4. The password is decrypted and displayed

## Database

The app creates and uses a local SQLite database automatically. The code currently targets:

```text
db/main.db
```

The table created is named `password` and stores:

- `website_name`
- `email`
- `user_name`
- `password`
- `salt`
- `nonce`
- `created_at`
- `updated_at`

## Security notes

This project is a learning-focused implementation and should be treated as a personal utility, not a production-grade password manager.

Important notes:

- It stores data locally only
- It does not replace professional password manager security models
- It should be used with caution and regular backups
- The database contains encrypted values, but the security model is still simple and educational

## Development notes

The repository also contains a few basic tests under `tests/`, though the project is still quite minimal and experimental in scope.

## Status

PassMan is a small, local, Python-based CLI project meant to explore password management concepts, encryption, and SQLite-backed storage in a practical way.