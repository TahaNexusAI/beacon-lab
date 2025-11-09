# 🧠 Laboratoire Beacon

Mini-laboratoire éducatif : **analyse du trafic HTTP local avec Python et Wireshark**.

---

## 📚 Table des matières
- [Description](#description)
- [Composants](#composants)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Capture Wireshark](#capture-wireshark)
- [Licence](#licence)

---

## 📘 Description

Ce projet démontre la communication entre un client Python et un petit serveur HTTP local.  
Il permet de visualiser les requêtes dans **Wireshark** pour comprendre le protocole **HTTP**.

---

## 🧩 Composants
| Fichier | Description |
|----------|-------------|
| `server_ping.py` | Serveur HTTP local écoutant sur `127.0.0.1:8000` |
| `beacon_http.py` | Client envoyant des requêtes périodiques au serveur |
| `capture_wifi_test.pcapng` | Exemple de capture Wireshark montrant le trafic généré |

---

## ⚙️ Installation
```bash
# Cloner le dépôt
git clone https://github.com/TahaNexusAI/beacon-lab.git
cd beacon-lab

# Lancer le serveur HTTP
python server_ping.py

# Dans un autre terminal, lancer le client
python beacon_http.py


