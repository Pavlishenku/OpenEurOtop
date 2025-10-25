# Guide Utilisateur - OpenEurOtop

## Introduction

OpenEurOtop est une implementation Python du guide EurOtop (2018) pour le calcul du franchissement de vagues sur les ouvrages cotiers.

## Installation

```bash
# Installation depuis le repertoire local
cd OpenEurOtop
pip install -e .

# Ou installation des dependances uniquement
pip install -r requirements.txt
```

## Concepts de base

### Debit de franchissement moyen

Le debit de franchissement moyen q (en m3/s/m) represente le volume d'eau franchissant la crete d'un ouvrage par unite de temps et par metre lineaire.

### Parametres principaux

- Hm0 : Hauteur significative spectrale des vagues (m)
- Tm-1,0 : Periode spectrale moyenne (s)
- h : Profondeur d'eau au pied de l'ouvrage (m)
- Rc : Revanche (freeboard) - hauteur de crete au-dessus du niveau d'eau (m)
- alpha : Angle de pente du talus (degres)

### Facteurs de reduction

- gamma_f : Facteur de rugosite (rugosite du revetement)
- gamma_beta : Facteur d'obliquite (angle d'incidence des vagues)
- gamma_b : Facteur de berme (presence d'une berme)

## Exemples d'utilisation

### 1. Cas simple : Digue a talus lisse

```python
from openeurotop import overtopping

# Calcul du franchissement
q = overtopping.digue_talus(
    Hm0=2.5,      # Hauteur significative (m)
    Tm_10=6.0,    # Periode moyenne (s)
    h=10.0,       # Profondeur d'eau (m)
    Rc=3.0,       # Revanche (m)
    alpha_deg=35.0,  # Pente (degres)
    gamma_f=1.0,  # Surface lisse
    gamma_beta=1.0,  # Vagues perpendiculaires
    gamma_b=1.0   # Pas de berme
)

print(f"Debit de franchissement : {q:.6f} m3/s/m")
print(f"Debit de franchissement : {q*1000:.3f} l/s/m")
```

### 2. Digue en enrochement

```python
from openeurotop import overtopping

# Methode 1 : Avec calcul automatique des facteurs
result = overtopping.digue_talus_detailed(
    Hm0=3.0,
    Tm_10=7.0,
    h=12.0,
    Rc=4.0,
    alpha_deg=33.7,
    type_revetement="enrochement_2couches"
)

print(f"Debit : {result['q']*1000:.3f} l/s/m")
print(f"Facteur de rugosite : {result['gamma_f']:.2f}")
print(f"Nombre d'Iribarren : {result['xi']:.3f}")

# Methode 2 : Fonction specialisee
q = overtopping.digue_en_enrochement(
    Hm0=3.0,
    Tm_10=7.0,
    h=12.0,
    Rc=4.0,
    alpha_deg=33.7,
    Dn50=1.5,  # Diametre nominal des blocs
    n_layers=2,
    permeability="permeable"
)
```

### 3. Mur vertical

```python
from openeurotop import overtopping

q = overtopping.mur_vertical(
    Hm0=2.0,
    Tm_10=5.5,
    h=8.0,
    Rc=2.5
)

print(f"Debit : {q*1000:.3f} l/s/m")
```

### 4. Structure composite (talus + mur)

```python
from openeurotop import overtopping

q = overtopping.structure_composite(
    Hm0=2.8,
    Tm_10=6.5,
    h=10.0,
    Rc=5.0,
    alpha_lower_deg=30.0,
    h_transition=2.0,  # Hauteur de transition
    gamma_f_lower=0.9,  # Beton rugueux en partie basse
    gamma_f_upper=1.0   # Mur lisse en partie haute
)
```

### 5. Prise en compte de l'obliquite

```python
from openeurotop import overtopping, reduction_factors

# Calcul du facteur d'obliquite
beta = 30  # Angle d'obliquite (degres)
gamma_beta = reduction_factors.gamma_beta_obliquity(beta)

# Calcul avec obliquite
q = overtopping.digue_talus(
    Hm0=2.5, Tm_10=6.0, h=10.0, Rc=3.0, alpha_deg=35.0,
    gamma_beta=gamma_beta
)

print(f"Obliquite : {beta} degres")
print(f"Facteur gamma_beta : {gamma_beta:.3f}")
print(f"Debit : {q*1000:.3f} l/s/m")
```

### 6. Calcul de volumes

```python
from openeurotop import overtopping

# D'abord calculer le debit
q = overtopping.digue_talus(
    Hm0=2.5, Tm_10=6.0, h=10.0, Rc=3.0, alpha_deg=35.0
)

# Puis calculer les volumes pour une tempete de 4 heures
volumes = overtopping.calcul_volumes_franchissement(q, duree_tempete_heures=4.0)

print(f"Volume total : {volumes['volume_total_m3_per_m']:.2f} m3/m")
print(f"Volume total : {volumes['volume_liters_per_m']:.0f} litres/m")
```

## Types de revetements disponibles

Le facteur de rugosite gamma_f peut etre obtenu automatiquement pour les types suivants :

```python
from openeurotop import reduction_factors

types_disponibles = [
    "lisse",                    # gamma_f = 1.00 - Beton lisse, asphalte
    "beton_rugueux",           # gamma_f = 0.90 - Beton avec rugosite
    "beton_colonne",           # gamma_f = 0.85 - Beton avec colonnes
    "enrochement_1couche",     # gamma_f = 0.55 - Enrochement 1 couche
    "enrochement_2couches",    # gamma_f = 0.50 - Enrochement 2 couches
    "enrochement_impermeable", # gamma_f = 0.45 - Enrochement sur noyau impermeable
    "cubes",                   # gamma_f = 0.47 - Cubes de beton
    "tetrapodes",              # gamma_f = 0.38 - Tetrapodes
    "accropode",               # gamma_f = 0.46 - Accropode
    "xbloc",                   # gamma_f = 0.45 - X-bloc
    "core_loc",                # gamma_f = 0.44 - Core-Loc
]

# Utilisation
gamma_f = reduction_factors.gamma_f_roughness("tetrapodes")
print(f"gamma_f pour tetrapodes : {gamma_f}")
```

## Parametres de vagues

```python
from openeurotop import wave_parameters

# Longueur d'onde en eau profonde
L0 = wave_parameters.wave_length_deep_water(T=6.0)

# Longueur d'onde pour une profondeur donnee
L = wave_parameters.wave_length(T=6.0, h=10.0)

# Cambrure de la vague
s0 = wave_parameters.wave_steepness(Hm0=2.5, Tm_10=6.0)

# Nombre d'Iribarren
xi = wave_parameters.iribarren_number(alpha_deg=35.0, Hm0=2.5, Tm_10=6.0)

# Conversion entre periodes spectrales
periodes = wave_parameters.spectral_period_conversion(Tp=7.2)
print(f"Tp = {periodes['Tp']:.1f} s")
print(f"Tm-1,0 = {periodes['Tm_10']:.1f} s")
print(f"Tm0,1 = {periodes['Tm01']:.1f} s")
```

## Statistiques par vagues individuelles

```python
from openeurotop import overtopping

# Estimation du franchissement par vagues individuelles
stats = overtopping.discharge_individual_waves(
    Hm0=2.5, Tm_10=6.0, h=10.0, Rc=2.0, alpha_deg=35.0,
    N_waves=2400  # Nombre de vagues pendant la tempete
)

print(f"Debit moyen : {stats['q_mean']*1000:.3f} l/s/m")
print(f"Proportion de vagues franchissantes : {stats['P_overtopping']*100:.1f}%")
print(f"Nombre de vagues franchissantes : {stats['N_overtopping_waves']}")
print(f"Volume moyen par vague franchissante : {stats['V_per_overtopping_wave']:.3f} m3/m")
```

## Limites et validite

### Domaines de validite

Les formules EurOtop sont valides dans les plages suivantes :

- Rc/Hm0 : 0.5 a 3.5 (recommande)
- Pente alpha : 10 a 90 degres
- Nombre d'Iribarren xi : 1 a 7 (selon le type de structure)

### Precautions

1. Extrapolation : Soyez prudent en dehors des domaines de validite
2. Structures complexes : Les structures tres complexes peuvent necessiter des etudes specifiques
3. Conditions extremes : Pour des conditions extremes, validez avec des essais physiques
4. Incertitudes : Les resultats ont une incertitude intrinseque (voir EurOtop 2018)

## Bonnes pratiques

### 1. Verification des resultats

Toujours verifier la coherence physique des resultats :

```python
# Verifier que le debit diminue avec la revanche
q1 = overtopping.digue_talus(Hm0=2.5, Tm_10=6.0, h=10.0, Rc=2.0, alpha_deg=35.0)
q2 = overtopping.digue_talus(Hm0=2.5, Tm_10=6.0, h=10.0, Rc=4.0, alpha_deg=35.0)
assert q2 < q1, "Plus de revanche devrait donner moins de franchissement"
```

### 2. Etudes parametriques

Pour une etude parametrique :

```python
import numpy as np
import matplotlib.pyplot as plt

revanches = np.linspace(1.0, 5.0, 20)
debits = []

for Rc in revanches:
    q = overtopping.digue_talus(
        Hm0=2.5, Tm_10=6.0, h=10.0, Rc=Rc, alpha_deg=35.0
    )
    debits.append(q * 1000)  # Conversion en l/s/m

plt.figure(figsize=(10, 6))
plt.plot(revanches, debits, 'b-', linewidth=2)
plt.xlabel('Revanche Rc (m)')
plt.ylabel('Debit de franchissement q (l/s/m)')
plt.grid(True)
plt.title('Franchissement en fonction de la revanche')
plt.show()
```

### 3. Documentation des calculs

Toujours documenter vos calculs :

```python
import json

calcul = {
    "projet": "Digue de protection",
    "date": "2025-10-23",
    "parametres": {
        "Hm0": 2.5,
        "Tm_10": 6.0,
        "h": 10.0,
        "Rc": 3.0,
        "alpha_deg": 35.0,
        "type_revetement": "enrochement_2couches"
    },
    "resultats": {}
}

result = overtopping.digue_talus_detailed(**calcul["parametres"])
calcul["resultats"] = result

# Sauvegarder
with open("calcul_franchissement.json", "w") as f:
    json.dump(calcul, f, indent=2, default=float)
```

## References

EurOtop (2018). Manual on wave overtopping of sea defences and related structures.
www.overtopping-manual.com

## Support

Pour des questions ou des problemes :
- Consultez les exemples dans le dossier examples/
- Executez les tests dans le dossier tests/
- Referez-vous au manuel EurOtop original pour plus de details theoriques
