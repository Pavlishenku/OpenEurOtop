# Guide de Publication - OpenEurOtop v1.0.0

Ce guide détaille les étapes pour publier OpenEurOtop sur GitHub et PyPI.

## Table des matières
- [Prérequis](#prérequis)
- [Publication sur GitHub](#publication-sur-github)
- [Publication sur PyPI Test](#publication-sur-pypi-test)
- [Publication sur PyPI Production](#publication-sur-pypi-production)
- [Configuration de la documentation](#configuration-de-la-documentation)

---

## Prérequis

### 1. Comptes nécessaires
- [x] Compte GitHub : https://github.com/Pavlishenku
- [ ] Compte PyPI : https://pypi.org/account/register/
- [ ] Compte Test PyPI : https://test.pypi.org/account/register/
- [ ] Compte ReadTheDocs : https://readthedocs.org/

### 2. Tokens d'API
Vous aurez besoin de créer des tokens d'API pour l'automatisation :

#### PyPI Token
1. Connectez-vous à https://pypi.org/
2. Allez dans "Account settings" > "API tokens"
3. Créez un nouveau token nommé "OpenEurOtop-GitHub-Actions"
4. Copiez le token (il commence par `pypi-`)

#### Test PyPI Token
1. Connectez-vous à https://test.pypi.org/
2. Même processus que pour PyPI
3. Créez un token nommé "OpenEurOtop-Test"

---

## Publication sur GitHub

### Étape 1 : Initialisation du repository Git

```bash
# Dans le dossier du projet
cd C:\Users\Yoshida\Documents\OpenEurOtop

# Initialiser Git (si pas déjà fait)
git init

# Ajouter le remote
git remote add origin https://github.com/Pavlishenku/OpenEurOtop.git

# Vérifier les fichiers à ajouter
git status
```

### Étape 2 : Premier commit

```bash
# Ajouter tous les fichiers (le .gitignore filtrera automatiquement)
git add .

# Créer le commit initial
git commit -m "🎉 Release v1.0.0 - Première version stable

- Implémentation complète des méthodes EurOtop 2018
- Suite de tests exhaustive avec >95% de couverture
- Documentation Sphinx complète
- Modèles de Machine Learning inclus
- Configuration CI/CD complète
"

# Créer la branche main si nécessaire
git branch -M main

# Pousser vers GitHub
git push -u origin main
```

### Étape 3 : Créer un tag de version

```bash
# Créer un tag annoté pour la v1.0.0
git tag -a v1.0.0 -m "Version 1.0.0 - Première version stable

## Nouveautés
- Implémentation complète des formules EurOtop 2018
- Modules ML (neural networks, XGBoost)
- Documentation utilisateur et API complètes
- >100 tests unitaires avec >95% de couverture
"

# Pousser le tag
git push origin v1.0.0
```

### Étape 4 : Créer une Release GitHub

1. Allez sur https://github.com/Pavlishenku/OpenEurOtop/releases
2. Cliquez sur "Create a new release"
3. Sélectionnez le tag `v1.0.0`
4. Titre : `OpenEurOtop v1.0.0 - Première version stable`
5. Description : Copiez le contenu de la section v1.0.0 du CHANGELOG.md
6. Cochez "Set as the latest release"
7. Cliquez sur "Publish release"

### Étape 5 : Configurer les Secrets GitHub

Pour que les workflows fonctionnent :

1. Allez dans Settings > Secrets and variables > Actions
2. Ajoutez les secrets suivants :
   - `PYPI_API_TOKEN` : votre token PyPI
   - `TEST_PYPI_API_TOKEN` : votre token Test PyPI

### Étape 6 : Activer GitHub Pages

1. Allez dans Settings > Pages
2. Source : "GitHub Actions"
3. La documentation sera publiée automatiquement lors du push sur main

---

## Publication sur PyPI Test

### Préparation

```bash
# Installer les outils de build
pip install --upgrade build twine

# Nettoyer les builds précédents
rm -rf dist/ build/ *.egg-info/

# Construire le package
python -m build
```

### Vérification

```bash
# Vérifier que le package est valide
twine check dist/*

# Lister le contenu du package
tar -tzf dist/openeurotop-1.0.0.tar.gz
```

### Publication sur Test PyPI

```bash
# Méthode 1 : Avec twine directement
twine upload --repository testpypi dist/*

# Vous serez invité à entrer :
# username: __token__
# password: votre-token-test-pypi

# Méthode 2 : Avec fichier de configuration
# Créer ~/.pypirc depuis le template .pypirc.template
# puis :
twine upload --repository testpypi dist/*
```

### Test d'installation depuis Test PyPI

```bash
# Créer un environnement virtuel de test
python -m venv test_env
source test_env/bin/activate  # Linux/Mac
# OU
test_env\Scripts\activate  # Windows

# Installer depuis Test PyPI
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ openeurotop

# Tester l'installation
python -c "from openeurotop import overtopping; print(overtopping.__doc__)"

# Nettoyer
deactivate
rm -rf test_env
```

---

## Publication sur PyPI Production

⚠️ **ATTENTION** : La publication sur PyPI est **DÉFINITIVE**. Vous ne pouvez pas :
- Supprimer une version publiée
- Réutiliser un numéro de version
- Modifier un package déjà publié

### Vérifications finales

- [ ] Tests passent tous (pytest)
- [ ] Documentation à jour
- [ ] CHANGELOG.md complété
- [ ] Version dans setup.py et pyproject.toml = 1.0.0
- [ ] Package testé sur Test PyPI
- [ ] Git tag créé et pushé

### Publication

```bash
# Publication manuelle
twine upload dist/*

# OU attendre que GitHub Actions le fasse automatiquement
# lors de la création d'une Release
```

### Vérification

```bash
# Attendre 1-2 minutes que PyPI indexe le package
# puis :
pip install openeurotop

# Tester
python -c "import openeurotop; print(openeurotop.__version__)"
```

---

## Configuration de la documentation

### ReadTheDocs

1. Connectez-vous à https://readthedocs.org/
2. Cliquez sur "Import a Project"
3. Sélectionnez "OpenEurOtop" depuis votre compte GitHub
4. Configuration :
   - Name: `openeurotop`
   - Repository URL: `https://github.com/Pavlishenku/OpenEurOtop`
   - Default branch: `main`
5. Cliquez sur "Next"
6. La documentation se build automatiquement avec `.readthedocs.yaml`

### GitHub Pages

La documentation est automatiquement publiée via GitHub Actions lors de chaque push sur `main`.

URL : https://pavlishenku.github.io/OpenEurOtop/

---

## Workflow complet pour une nouvelle version

Pour les futures versions (v1.1.0, v2.0.0, etc.) :

```bash
# 1. Mettre à jour la version
# - setup.py : version="1.1.0"
# - pyproject.toml : version = "1.1.0"

# 2. Mettre à jour CHANGELOG.md
# Ajouter une section ## [1.1.0] - 2025-XX-XX

# 3. Commit des changements
git add setup.py pyproject.toml CHANGELOG.md
git commit -m "Bump version to 1.1.0"
git push

# 4. Créer et pousser le tag
git tag -a v1.1.0 -m "Version 1.1.0"
git push origin v1.1.0

# 5. Créer une Release sur GitHub
# GitHub Actions publiera automatiquement sur PyPI

# 6. Vérifier la publication
pip install --upgrade openeurotop
python -c "import openeurotop; print(openeurotop.__version__)"
```

---

## Support et ressources

- **Documentation** : https://openeurotop.readthedocs.io/
- **GitHub** : https://github.com/Pavlishenku/OpenEurOtop
- **PyPI** : https://pypi.org/project/openeurotop/
- **Issues** : https://github.com/Pavlishenku/OpenEurOtop/issues

---

## Troubleshooting

### Erreur : "File already exists"
- Vous essayez de republier la même version
- Incrémentez le numéro de version

### Erreur : "Invalid distribution"
- Vérifiez avec `twine check dist/*`
- Vérifiez que README.md est bien formatté en Markdown

### Erreur lors du build
- Nettoyez les caches : `rm -rf build/ dist/ *.egg-info/`
- Re-buildez : `python -m build`

### La documentation ne se build pas
- Vérifiez les logs sur ReadTheDocs
- Assurez-vous que `.readthedocs.yaml` est à la racine
- Vérifiez que `docs/sphinx/conf.py` existe

