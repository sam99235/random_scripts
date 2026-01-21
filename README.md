# 🧰 random_scripts

Ce dépôt contient une collection de **scripts utilitaires et fichiers de configuration** orientés **administration système Linux** et **sécurité**.  
Il regroupe différents outils permettant de renforcer un système, automatiser des tâches et gérer certains services critiques.

---

## 📂 Contenu du dépôt

### 🔐 Sécurité & Durcissement système

- **SSH CONFIG**  
  Fichier de configuration SSH personnalisé.  
  Utilisé pour renforcer la sécurité des connexions SSH (protocoles, algorithmes, options par défaut).

- **ssh service hardening**  
  Script ou notes de durcissement du service SSH (restriction d’accès, sécurisation des paramètres sensibles).

- **pre-login-banner**  
  Bannière affichée avant la connexion (SSH ou console).  
  Généralement utilisée pour afficher un message légal ou d’avertissement.

- **grub_passwd**  
  Script permettant de configurer un **mot de passe GRUB** afin d’empêcher la modification des options de démarrage.

- **block_usb_storage**  
  Script destiné à **bloquer les périphériques de stockage USB** pour éviter la fuite ou l’injection de données.

---

### 🔥 Pare-feu & Réseau

- **ipables script.txt**  
  Script contenant des règles **iptables** pour configurer un pare-feu Linux (filtrage réseau, sécurité).

---

### ⚙️ Automatisation & Services système

- **security-upgrade.service**  
  Service systemd permettant d’automatiser les **mises à jour de sécurité**.

- **security-upgrade.timer**  
  Timer systemd associé au service de mise à jour pour une exécution périodique.

- **upgrade-notify.sh**  
  Script shell pour **notifier ou gérer les mises à jour système**.

- **services.txt**  
  Liste ou documentation des services système à activer, désactiver ou surveiller.

---
