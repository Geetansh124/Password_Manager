# Password Manager

<div align="center"><img src="https://img.shields.io/badge/Password%20Manager-Security%20Practice-0f172a?style=for-the-badge" alt="Password manager" /> <img src="https://img.shields.io/badge/Python-Cryptography-3776ab?style=for-the-badge&logo=python&logoColor=white" alt="Python" /> <img src="https://img.shields.io/badge/Focus-Privacy-dc2626?style=for-the-badge" alt="Privacy" /></div>

A Python security project for learning how password storage, encryption boundaries, and local credential workflows should be designed.

## Security model

```mermaid
flowchart LR
    P[Master password] --> K[Derived key]
    K --> E[Encrypted vault]
    E --> D[Decrypted only when needed]
    D --> C[Clipboard or controlled output]
```

## Important

This repository is educational. Do not use it as a production password manager without a serious security review, audited cryptography, secure key handling, and protected backups. Never commit real credentials.

## Getting started

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

Use test data only while experimenting.
