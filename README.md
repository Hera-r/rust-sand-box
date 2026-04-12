# Rust Pool

Rust Pool is an intensive, practice based learning platform for the Rust programming language. It is designed as a local training environment (piscine) to help developers progress from beginner to advanced levels through structured, hands on challenges. 

*Designed meticulously for maximum pedagogy and security.*

## Architecture

The platform operates using two main services isolated in local Docker containers:
* A Django web application providing the user interface, tutorials, and progression tracking.
* An isolated runner microservice responsible for safely compiling and executing submitted Rust code.

## Execution and Setup

To run Rust Pool locally, you must provide the necessary environmental configuration.

1. Create a file named .env at the root of the project with the following required variables:

DJANGO_SECRET_KEY=your_secret_key_here
DJANGO_DEBUG=False
RUNNER_URL=http://runner:8001

2. Use the provided Makefile to manage the platform lifecycle:

* make up : Builds and starts the Docker environment in the background.
* make down : Stops the application.
* make clean : Radically purges all containers, images, and system caches.
* make reset : Resets the environment and rebuilds without cache.

Once started, the application is accessible at http://localhost:8000.


# Rust Pool (Version Francaise)

Rust Pool est une plateforme d'apprentissage intensive et pratique dediee au langage de programmation Rust. Elle est concue comme un environnement d'entrainement local (piscine) pour accompagner les developpeurs du niveau debutant au niveau avance a travers des defis structures.

## Architecture

La plateforme est composee de deux services principaux isoles dans des conteneurs Docker locaux :
* Une application web Django fournissant l'interface utilisateur, les tutoriels et le suivi de progression.
* Un microservice runner isole responsable de la compilation et de l'execution securisee du code Rust soumis.

## Execution et Installation

Pour executer Rust Pool localement, vous devez fournir la configuration environnementale requise.

1. Creez un fichier nomme .env a la racine du projet contenant les variables obligatoires suivantes :

DJANGO_SECRET_KEY=votre_cle_secrete_ici
DJANGO_DEBUG=False
RUNNER_URL=http://runner:8001

2. Utilisez le Makefile fourni pour gerer le cycle de vie de la plateforme :

* make up : Construit et demarre l'environnement Docker en arriere plan.
* make down : Arrete l'application.
* make clean : Purge radicalement tous les conteneurs, images et caches systeme.
* make reset : Reinitialise l'environnement et reconstruit sans cache.

Une fois demarree, l'application est accessible via http://localhost:8000.
