# OpenEurOtop

Implementation Python du guide EurOtop 2018 pour le calcul du franchissement de vagues.

## Installation

```bash
pip install openeurotop
```

## Utilisation

```python
from openeurotop import overtopping

# Calcul du franchissement pour une digue a talus
q = overtopping.digue_talus(
    Hm0=2.5,      # Hauteur significative (m)
    Tm_10=6.0,    # Periode moyenne (s)
    h=10.0,       # Profondeur d'eau (m)
    Rc=3.0,       # Revanche (m)
    alpha_deg=30  # Pente du talus (degres)
)

print(f"Debit de franchissement : {q:.6f} m3/s/m")
```

## Caracteristiques

- Formules EurOtop 2018 completes et validees
- Types de structures : digues a talus, murs verticaux, structures composites
- Facteurs de reduction : rugosites, bermes, obliquite
- Modeles de Machine Learning pre-entraines (Neural Networks, XGBoost)
- Analyses probabilistes et statistiques
- Tests unitaires avec couverture > 95%

## Documentation

- Documentation complete : https://openeurotop.readthedocs.io/
- Guide utilisateur : docs/GUIDE_UTILISATEUR.md
- Formules techniques : docs/FORMULES_TECHNIQUES.md
- Exemples : examples/

## Support

Python 3.8+ - Windows, Linux, macOS

## Modules

- overtopping : Calculs de franchissement
- wave_parameters : Parametres de vagues
- reduction_factors : Facteurs de reduction
- run_up : Calculs de run-up
- probabilistic : Analyses probabilistes
- neural_network : Modeles de Machine Learning
- case_studies : Cas d'etudes EurOtop
- validation : Validation des parametres

## Reference scientifique

EurOtop Manual (2018)
"Manual on wave overtopping of sea defences and related structures"
Van der Meer, J.W., Allsop, N.W.H., Bruce, T., De Rouck, J., Kortenhaus, A., 
Pullen, T., Schuttrumpf, H., Troch, P. and Zanuttigh, B.

http://www.overtopping-manual.com

## Licence

MIT License - voir fichier LICENSE
