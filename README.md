<div align="center">

# 🌊 OpenEurOtop

**Implémentation Python du guide EurOtop 2018 pour le calcul du franchissement de vagues**

[![PyPI](https://img.shields.io/pypi/v/openeurotop?color=blue)](https://pypi.org/project/openeurotop/)
[![Python](https://img.shields.io/pypi/pyversions/openeurotop)](https://pypi.org/project/openeurotop/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Documentation](https://readthedocs.org/projects/openeurotop/badge/?version=latest)](https://openeurotop.readthedocs.io/)
[![GitHub Stars](https://img.shields.io/github/stars/Pavlishenku/OpenEurOtop?style=social)](https://github.com/Pavlishenku/OpenEurOtop)

[📖 Documentation](https://openeurotop.readthedocs.io/) • [🐍 PyPI](https://pypi.org/project/openeurotop/) • [💻 GitHub](https://github.com/Pavlishenku/OpenEurOtop) • [🐛 Issues](https://github.com/Pavlishenku/OpenEurOtop/issues)

</div>

---

## 🚀 Quick Start

```bash
pip install openeurotop
```

```python
from openeurotop import overtopping

# Calcul du franchissement pour une digue à talus
q = overtopping.digue_talus(
    Hm0=2.5,      # Hauteur significative (m)
    Tm_10=6.0,    # Période moyenne (s)
    h=10.0,       # Profondeur d'eau (m)
    Rc=3.0,       # Revanche (m)
    alpha_deg=30  # Pente du talus (°)
)

print(f"Débit de franchissement : {q:.6f} m³/s/m")
```

---

## 📋 À propos

**OpenEurOtop** est une bibliothèque Python complète implémentant les méthodes de calcul du manuel [EurOtop 2018](http://www.overtopping-manual.com) pour l'évaluation du franchissement de vagues sur les ouvrages côtiers.

### ✨ Caractéristiques principales

- 🌊 **Formules EurOtop 2018** - Implémentation complète et validée
- 🏗️ **Types de structures** - Digues à talus, murs verticaux, structures composites
- 🎯 **Facteurs de réduction** - Support de >15 types de revêtements
- 🤖 **Machine Learning** - Modèles pré-entraînés (Neural Networks, XGBoost)
- 📊 **Analyses avancées** - Probabilistes, statistiques, run-up
- ✅ **Tests & qualité** - >100 tests unitaires, >95% de couverture
- 📚 **Documentation complète** - Guides, API, exemples, notebooks Jupyter

---

## 📦 Installation

### Installation standard

```bash
pip install openeurotop
```

### Avec fonctionnalités Machine Learning

```bash
pip install openeurotop[ml]
```

### Pour le développement

```bash
git clone https://github.com/Pavlishenku/OpenEurOtop.git
cd OpenEurOtop
pip install -e .[dev]
pytest  # Lancer les tests
```

**Support** : Python 3.8+ • Windows, Linux, macOS

---

## 💡 Exemples

### Digue à talus avec enrochements

```python
from openeurotop import overtopping, reduction_factors

# Facteur de rugosité pour enrochements
gamma_f = reduction_factors.gamma_f_roughness(
    type_revetement="enrochements_2couches"
)

q = overtopping.digue_talus(
    Hm0=3.0,
    Tm_10=7.0,
    h=12.0,
    Rc=4.5,
    alpha_deg=35,
    gamma_f=gamma_f
)
```

### Mur vertical

```python
from openeurotop import overtopping

q = overtopping.mur_vertical(
    Hm0=2.5,
    Tm_10=6.0,
    h=10.0,
    Rc=3.0,
    h_structure=12.0
)
```

### Prédiction avec Machine Learning

```python
from openeurotop import neural_network_clash

# Utiliser le modèle neural pré-entraîné
predictor = neural_network_clash.CLASHPredictor()
q_predicted = predictor.predict(
    Hm0=2.5, Tm_10=6.0, h=10.0, Rc=3.0, 
    alpha_deg=30, gamma_f=1.0
)
```

➡️ **Plus d'exemples** : [Documentation](https://openeurotop.readthedocs.io/) • [Notebooks](examples/)

---

## 📚 Documentation

| Ressource | Description | Lien |
|-----------|-------------|------|
| 📖 **Documentation complète** | API, guides, tutoriels | [ReadTheDocs](https://openeurotop.readthedocs.io/) |
| 🚀 **Guide de démarrage** | Installation et premiers pas | [Quickstart](https://openeurotop.readthedocs.io/quickstart/) |
| 👤 **Guide utilisateur** | Utilisation détaillée | [User Guide](docs/GUIDE_UTILISATEUR.md) |
| 🔬 **Formules techniques** | Documentation scientifique | [Formules](docs/FORMULES_TECHNIQUES.md) |
| 💻 **Exemples de code** | Scripts et notebooks Jupyter | [Examples](examples/) |
| 🐛 **Signaler un bug** | Issues et discussions | [GitHub Issues](https://github.com/Pavlishenku/OpenEurOtop/issues) |

---

## 🛠️ Modules disponibles

| Module | Description |
|--------|-------------|
| `overtopping` | Calculs de franchissement (digues, murs, structures composites) |
| `wave_parameters` | Paramètres de vagues (longueur d'onde, cambrure, Iribarren) |
| `reduction_factors` | Facteurs de réduction (rugosité, berme, obliquité, etc.) |
| `run_up` | Calculs de run-up |
| `probabilistic` | Analyses probabilistes et statistiques |
| `neural_network` | Modèles de Machine Learning pré-entraînés |
| `case_studies` | Cas d'études du manuel EurOtop |
| `validation` | Outils de validation des paramètres |

---

## 🎓 Référence scientifique

**EurOtop Manual (2018)**  
*"Manual on wave overtopping of sea defences and related structures"*  
Van der Meer, J.W., Allsop, N.W.H., Bruce, T., De Rouck, J., Kortenhaus, A., Pullen, T., Schüttrumpf, H., Troch, P. and Zanuttigh, B.

🔗 [www.overtopping-manual.com](http://www.overtopping-manual.com)

### Citation

Si vous utilisez OpenEurOtop dans vos travaux, veuillez citer :

```bibtex
@software{openeurotop2025,
  title = {OpenEurOtop: Python Implementation of EurOtop Wave Overtopping Manual},
  author = {OpenEurOtop Contributors},
  year = {2025},
  url = {https://github.com/Pavlishenku/OpenEurOtop},
  version = {1.0.0},
  doi = {10.5281/zenodo.XXXXXXX}
}
```

---

## 🤝 Contribution

Les contributions sont les bienvenues ! 

- 🐛 **Bug reports** : [Ouvrir une issue](https://github.com/Pavlishenku/OpenEurOtop/issues)
- 💡 **Suggestions** : [Discussions](https://github.com/Pavlishenku/OpenEurOtop/discussions)
- 🔧 **Pull requests** : Consultez le [guide de contribution](CONTRIBUTING.md)

### Pour les développeurs

```bash
git clone https://github.com/Pavlishenku/OpenEurOtop.git
cd OpenEurOtop
pip install -e .[dev]
pytest                    # Tests
pytest --cov=openeurotop  # Avec couverture
```

---

## 📄 Licence

Ce projet est sous licence **MIT** - voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## 🔗 Liens utiles

- **Package PyPI** : https://pypi.org/project/openeurotop/
- **Code source** : https://github.com/Pavlishenku/OpenEurOtop
- **Documentation** : https://openeurotop.readthedocs.io/
- **Issues** : https://github.com/Pavlishenku/OpenEurOtop/issues
- **Changelog** : [CHANGELOG.md](CHANGELOG.md)

---

<div align="center">

**Fait avec ❤️ pour la communauté de l'ingénierie côtière**

⭐ **Si vous aimez ce projet, n'hésitez pas à lui donner une étoile !** ⭐

</div>
