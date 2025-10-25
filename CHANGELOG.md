# Changelog

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/lang/fr/).

## [1.0.0] - 2025-10-24

### Nouveautes majeures
- Premiere version stable de production
- Implementation complete des methodes EurOtop 2018
- Suite de tests exhaustive avec couverture de code > 95%
- Documentation Sphinx complete avec guides utilisateur et API
- Modeles de Machine Learning pour la prediction de franchissement
- Exemples et cas d'etudes pratiques

### Modules ajoutés
- neural_network.py : Reseau de neurones pour prediction de franchissement
- neural_network_clash.py : Modele neural specialise base sur la base CLASH
- xgboost_model.py : Modele XGBoost optimise pour franchissement
- probabilistic.py : Analyses probabilistes et statistiques
- special_cases.py : Cas speciaux (bermes, structures composites)
- case_studies.py : Cas d'etudes documentes du guide EurOtop
- validation.py : Outils de validation des parametres d'entree

### Fonctionnalites
- Support complet des digues a talus (lisses, rugueuses, avec bermes)
- Support des murs verticaux et structures composites
- Calculs de run-up et franchissement individuel par vague
- Facteurs de reduction pour plus de 15 types de revetements
- Analyses d'influence parametrique
- Export des resultats et visualisations

### Documentation
- Guide utilisateur complet en francais
- Documentation API Sphinx avec exemples
- Notebooks Jupyter interactifs
- Cas d'etudes detailles du manuel EurOtop
- Formules techniques documentees

### Tests et qualite
- Plus de 100 tests unitaires
- Tests d'integration pour validation physique
- Couverture de code > 95%
- Validation contre cas de reference EurOtop

### Performances
- Modeles ML pre-entraines inclus
- Optimisation des calculs numeriques
- Support batch pour calculs multiples

### Infrastructure
- Configuration PyPI complete
- Documentation ReadTheDocs prete
- CI/CD configure
- Gestion semantique des versions

## [0.1.0] - 2025-10-23

### Ajoute
- Implementation initiale du package OpenEurOtop
- Module overtopping avec les fonctions principales
- Module wave_parameters avec calculs de parametres de vagues
- Module reduction_factors avec facteurs de reduction
- Module constants avec les constantes et coefficients EurOtop
- Fichiers d'exemples complets dans examples/exemple_basic.py
- Tests unitaires dans tests/test_overtopping.py
- Documentation complete dans README.md
- Configuration du package avec setup.py

### References
- EurOtop (2018). Manual on wave overtopping of sea defences and related structures.
  www.overtopping-manual.com

