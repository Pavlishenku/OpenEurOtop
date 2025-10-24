# ✅ Checklist de Publication v1.0.0

## Avant publication

### Code et Tests
- [ ] Tous les tests passent (`pytest`)
- [ ] Couverture de code > 95%
- [ ] Pas d'erreurs flake8 critiques
- [ ] Documentation à jour
- [ ] Exemples fonctionnent

### Fichiers de configuration
- [ ] `setup.py` : version = "1.0.0"
- [ ] `pyproject.toml` : version = "1.0.0"
- [ ] `CHANGELOG.md` complété pour v1.0.0
- [ ] `README.md` à jour avec badges
- [ ] `.gitignore` configuré
- [ ] `MANIFEST.in` vérifié

### Git
- [ ] Tous les changements commitées
- [ ] Branche `main` à jour
- [ ] Tag `v1.0.0` créé
- [ ] Tag poussé vers GitHub

---

## Publication GitHub

### Repository
- [ ] Dépôt créé : https://github.com/Pavlishenku/OpenEurOtop
- [ ] Remote ajouté : `git remote add origin https://github.com/Pavlishenku/OpenEurOtop.git`
- [ ] Premier push effectué : `git push -u origin main`
- [ ] Tag poussé : `git push origin v1.0.0`

### Release
- [ ] Release créée sur GitHub
- [ ] Titre : "OpenEurOtop v1.0.0 - Première version stable"
- [ ] Description copiée depuis CHANGELOG.md
- [ ] Marquée comme "Latest release"

### Configuration
- [ ] GitHub Actions activées
- [ ] Secrets configurés :
  - [ ] `PYPI_API_TOKEN`
  - [ ] `TEST_PYPI_API_TOKEN`
- [ ] GitHub Pages activé (Source: GitHub Actions)
- [ ] Branch protection sur `main` (optionnel)

---

## Publication PyPI

### Test PyPI (obligatoire)
- [ ] Build créé : `python -m build`
- [ ] Package vérifié : `twine check dist/*`
- [ ] Publié sur Test PyPI : `twine upload --repository testpypi dist/*`
- [ ] Installé et testé depuis Test PyPI
- [ ] Fonctionnalités de base vérifiées

### PyPI Production
- [ ] Vérifications finales OK
- [ ] Build propre créé
- [ ] Publié sur PyPI : `twine upload dist/*`
- [ ] Package visible sur https://pypi.org/project/openeurotop/
- [ ] Installation testée : `pip install openeurotop`

---

## Documentation

### ReadTheDocs
- [ ] Compte créé sur https://readthedocs.org/
- [ ] Projet importé depuis GitHub
- [ ] Build réussi
- [ ] Documentation accessible : https://openeurotop.readthedocs.io/

### GitHub Pages
- [ ] Workflow docs.yml exécuté avec succès
- [ ] Pages déployées
- [ ] Documentation accessible via GitHub Pages

---

## Communication

### Annonce
- [ ] README.md inclut tous les liens
- [ ] Badges ajoutés et fonctionnels
- [ ] CHANGELOG publié
- [ ] Guide de contribution publié

### Réseaux (optionnel)
- [ ] Annonce sur Twitter/X
- [ ] Post LinkedIn
- [ ] Communautés Python/Engineering

---

## Post-publication

### Vérifications
- [ ] Package installable : `pip install openeurotop`
- [ ] Import fonctionne : `import openeurotop`
- [ ] Exemples fonctionnent avec version installée
- [ ] Documentation accessible et complète
- [ ] Badges README fonctionnels

### Monitoring
- [ ] Suivre les téléchargements PyPI
- [ ] Surveiller les issues GitHub
- [ ] Répondre aux questions
- [ ] Planifier v1.1.0

---

## Commandes rapides

```bash
# Vérification complète
python build_and_publish.py check

# Build
python build_and_publish.py build

# Publication Test PyPI
python build_and_publish.py test

# Publication PyPI Production
python build_and_publish.py publish

# Git flow
git add .
git commit -m "Release v1.0.0"
git tag -a v1.0.0 -m "Version 1.0.0"
git push origin main
git push origin v1.0.0
```

---

## Liens importants

- **GitHub** : https://github.com/Pavlishenku/OpenEurOtop
- **PyPI** : https://pypi.org/project/openeurotop/
- **Test PyPI** : https://test.pypi.org/project/openeurotop/
- **ReadTheDocs** : https://openeurotop.readthedocs.io/
- **GitHub Pages** : https://pavlishenku.github.io/OpenEurOtop/

---

**Date de publication** : ________________

**Publié par** : ________________

**Notes** : 
_____________________________________________
_____________________________________________
_____________________________________________

