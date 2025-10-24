# 🚀 OpenEurOtop v1.0.0 - Démarrage de la publication

**Tout est prêt ! Suivez ces étapes pour publier OpenEurOtop v1.0.0**

---

## ✅ Vérification terminée

Le script de vérification a confirmé que tous les fichiers sont en place et correctement configurés.

```bash
python pre_publish_check.py
# ✓ TOUS LES CONTRÔLES SONT PASSÉS !
```

---

## 📋 Étapes rapides de publication

### Option A : Utiliser le script automatique (RECOMMANDÉ pour Windows)

```cmd
publish_to_github.bat
```

Ce script va :
1. Initialiser Git (si nécessaire)
2. Ajouter le remote GitHub
3. Commiter tous les fichiers
4. Pousser sur GitHub
5. Créer et pousser le tag v1.0.0

### Option B : Commandes manuelles

```bash
# 1. Initialiser et configurer Git
git init
git branch -M main
git remote add origin https://github.com/Pavlishenku/OpenEurOtop.git

# 2. Premier commit
git add .
git commit -m "🎉 Release v1.0.0 - Première version stable"

# 3. Push vers GitHub
git push -u origin main

# 4. Créer et pousser le tag
git tag -a v1.0.0 -m "Version 1.0.0 - Première version stable"
git push origin v1.0.0
```

---

## 🌐 Après le push GitHub

### 1. Créer une Release GitHub

1. Allez sur : https://github.com/Pavlishenku/OpenEurOtop/releases/new
2. Sélectionnez le tag : `v1.0.0`
3. Titre : `OpenEurOtop v1.0.0 - Première version stable`
4. Description : Copiez le contenu de la section v1.0.0 dans `CHANGELOG.md`
5. Cochez "Set as the latest release"
6. Cliquez "Publish release"

### 2. Configurer les Secrets GitHub (pour CI/CD automatique)

1. Allez dans : Settings > Secrets and variables > Actions
2. Cliquez "New repository secret"
3. Ajoutez :
   - Name: `PYPI_API_TOKEN`
   - Value: Votre token PyPI (créé sur https://pypi.org/manage/account/token/)
4. Répétez pour :
   - Name: `TEST_PYPI_API_TOKEN`
   - Value: Votre token Test PyPI (créé sur https://test.pypi.org/manage/account/token/)

### 3. Activer GitHub Pages

1. Allez dans : Settings > Pages
2. Source : "GitHub Actions"
3. La documentation sera publiée automatiquement sur chaque push

---

## 📦 Publication sur PyPI

### Test PyPI (OBLIGATOIRE avant production)

```bash
# 1. Construire le package
python build_and_publish.py build

# 2. Publier sur Test PyPI
python build_and_publish.py test

# 3. Tester l'installation
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ openeurotop
python -c "import openeurotop; print('OK')"
```

### PyPI Production (après validation sur Test PyPI)

```bash
python build_and_publish.py publish
```

**OU** attendre que GitHub Actions le fasse automatiquement lors de la création de la Release.

---

## 📚 Documentation

### ReadTheDocs

1. S'inscrire sur : https://readthedocs.org/
2. Importer le projet depuis GitHub
3. La configuration `.readthedocs.yaml` fera le reste

---

## 📊 Vérifications post-publication

### GitHub ✓
- [ ] Code visible sur https://github.com/Pavlishenku/OpenEurOtop
- [ ] Release v1.0.0 créée
- [ ] Workflows GitHub Actions actifs (onglet Actions)
- [ ] GitHub Pages déployée

### PyPI ✓
- [ ] Package visible sur https://pypi.org/project/openeurotop/
- [ ] Installation fonctionne : `pip install openeurotop`
- [ ] Import fonctionne : `python -c "import openeurotop"`

### Documentation ✓
- [ ] ReadTheDocs accessible
- [ ] GitHub Pages accessible
- [ ] Liens dans README fonctionnels

---

## 🎯 Checklist complète

Consultez `PUBLICATION_CHECKLIST.md` pour une checklist détaillée imprimable.

---

## 📖 Documentation détaillée

- **Guide complet** : `GUIDE_PUBLICATION.md`
- **Checklist** : `PUBLICATION_CHECKLIST.md`
- **Résumé technique** : `RELEASE_v1.0.0_SUMMARY.md`

---

## ⚡ Commandes de référence rapide

```bash
# Vérification pré-publication
python pre_publish_check.py

# Build du package
python build_and_publish.py build

# Publication Test PyPI
python build_and_publish.py test

# Publication PyPI Production
python build_and_publish.py publish

# Publication GitHub (Windows)
publish_to_github.bat
```

---

## 🆘 Aide et support

Si vous rencontrez des problèmes :

1. Consultez `GUIDE_PUBLICATION.md` section "Troubleshooting"
2. Vérifiez les logs GitHub Actions
3. Testez sur Test PyPI avant production
4. Les fichiers temporaires (htmlcov, .coverage, etc.) sont normalement exclus par .gitignore

---

## 🎉 C'est parti !

Vous êtes prêt à publier OpenEurOtop v1.0.0 !

**Commencez par :**
```cmd
publish_to_github.bat
```

**Puis suivez les instructions ci-dessus.**

Bonne publication ! 🚀

