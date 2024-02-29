Smart Serre
Ce projet consiste en une serre intelligente capable de surveiller et de contrôler divers paramètres environnementaux pour optimiser la croissance des plantes. Les capteurs utilisés sont les suivants :

Capteur de température
Capteur d'humidité de sol
Capteur de mouvement PIR
Capteur de gaz
Capteur ultrasonique
Le projet est écrit en C++ et utilise une combinaison de matériel et de logiciel pour fonctionner de manière autonome.

Fonctionnalités
Surveillance en temps réel de la température et de l'humidité de l'air et du sol.
Détection de mouvement pour la sécurité et la gestion de l'énergie.
Surveillance des niveaux de gaz pour garantir un environnement sain pour les plantes.
Contrôle de l'arrosage basé sur les niveaux d'humidité du sol.
Notification d'alertes et de rapports via une interface utilisateur conviviale.
Installation
Cloner le dépôt : git clone https://github.com/Project_Arduino/Project_Arduino.git
Installer les dépendances : cd Project_Arduino && make install
Compiler le code : make
Connecter les capteurs au Raspberry Pi ou à tout autre microcontrôleur compatible.
Exécuter le programme : ./Project_Arduino
Configuration
Modifier le fichier config.h pour définir les seuils de température, d'humidité et de gaz.
Configurer les notifications et les rapports en fonction de vos besoins.
Contribution
Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue pour signaler un bug ou proposer une nouvelle fonctionnalité
