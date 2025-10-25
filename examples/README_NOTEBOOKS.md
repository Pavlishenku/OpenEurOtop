# Notebooks et Exemples - OpenEurOtop

## Suite d'exemples pour ingenieurs

Cette collection de notebooks compare systematiquement les 3 methodes de calcul disponibles dans OpenEurOtop :

1. Formules empiriques EurOtop (reference scientifique)
2. Neural Network CLASH (R2 = 0.67)
3. XGBoost optimise (R2 = 0.88)

---

## Liste des Notebooks

### 01. Introduction Comparative

Fichier : notebook_01_introduction_comparative.py

Contenu :
- Exemple simple sur digue a talus
- Variation de la revanche
- Comparaison sur plusieurs scenarios
- Graphiques comparatifs
- Interpretation des resultats

Pour qui : Debutants, decouverte du package
Duree : environ 10 minutes

---

### 02. Digues a Talus - Cas Complet

Fichier : notebook_02_digues_talus_complete.py

Contenu :
- Design complet d'une digue portuaire
- Calcul du nombre d'Iribarren
- Optimisation de la revanche
- Influence de la rugosite (5 types)
- Recommandations de design

Pour qui : Ingenieurs en conception
Duree : environ 20 minutes

---

### 03. Murs Verticaux

Fichier : notebook_03_murs_verticaux.py

Contenu :
- Calcul pour ouvrages verticaux
- Comparaison mur vertical vs talus
- Variation de la revanche
- Limites pour differentes zones

Pour qui : Design de quais et digues verticales
Duree : environ 15 minutes

---

## Utilisation

### Option 1 : Executer comme script Python

```bash
cd examples
python notebook_01_introduction_comparative.py
```

Les graphiques seront sauvegardes automatiquement.

### Option 2 : Convertir en Jupyter Notebook

```bash
# Installer jupytext si necessaire
pip install jupytext

# Convertir en notebook
jupytext --to notebook notebook_01_introduction_comparative.py

# Ou convertir tous les fichiers
jupytext --to notebook notebook_*.py
```

### Option 3 : Ouvrir directement dans Jupyter

Jupyter Lab et VSCode peuvent ouvrir les fichiers .py avec le format "percent" comme des notebooks.

---

## Resultats Attendus

### Graphiques Generes

Chaque notebook genere des graphiques PNG de haute qualite :

1. Comparaison des 3 methodes (barres)
2. Influence de la revanche (courbes)
3. Scenarios multiples (barres groupees)
4. Influence de la rugosite (2 panels)
5. Optimisation (courbes avec seuils)

### Tableaux Comparatifs

Tableaux pandas avec :
- Debits pour chaque methode
- Ecarts en pourcentage
- Recommandations

---

## Performances Comparees

| Methode          | R2   | RMSE | Stabilite | Recommandation |
|------------------|------|------|-----------|----------------|
| EurOtop          | -    | -    | Oui       | DESIGN         |
| XGBoost          | 0.88 | 0.46 | Oui       | Verification   |
| Neural Network   | 0.67 | 0.69 | Limite    | Recherche      |

---

## Conseils d'Utilisation

### Pour le Design

Toujours utiliser les formules EurOtop
- Validees scientifiquement
- Domaine de validite connu
- Recommandees par normes

### Pour la Verification

XGBoost acceptable
- Rapide pour tester plusieurs variants
- Ecart moyen < 20% vs EurOtop
- Toujours valider avec EurOtop

### Pour la Recherche

Comparer les 3 methodes
- Identifier les cas limites
- Analyser les divergences
- Ameliorer les modeles

---

## Cas d'Usage Typiques

### 1. Etude de Pre-Dimensionnement

```python
# Tester rapidement plusieurs configurations
for Rc in [1.0, 2.0, 3.0, 4.0]:
    q_xgb = predict_with_xgboost(Hm0, Tm_10, h, Rc, alpha)['q']
    print(f"Rc={Rc}m : q={q_xgb:.6f}")

# Puis affiner avec EurOtop
q_final = overtopping.digue_talus(Hm0, Tm_10, h, Rc_optimal, alpha)
```

### 2. Analyse de Sensibilite

```python
# Varier plusieurs parametres
import itertools
Hm0_list = [2.0, 2.5, 3.0]
Rc_list = [2.0, 3.0, 4.0]

for Hm0, Rc in itertools.product(Hm0_list, Rc_list):
    q_e = overtopping.digue_talus(Hm0, Tm_10, h, Rc, alpha)
    q_x = predict_with_xgboost(Hm0, Tm_10, h, Rc, alpha)['q']
    print(f"Hm0={Hm0}, Rc={Rc}: EurOtop={q_e:.6f}, XGB={q_x:.6f}")
```

### 3. Comparaison de Variantes

```python
# Comparer differentes rugosites
rugosites = [('Beton', 1.0), ('Enrochements', 0.5), ('Tetrapodes', 0.4)]

for name, gf in rugosites:
    results = compare_all_methods(Hm0, Tm_10, h, Rc, alpha, gamma_f=gf)
    print(f"\n{name} (gamma_f={gf}):")
    print(f"  EurOtop: {results['empirical']['q']:.6f}")
    print(f"  XGBoost: {results['xgboost']['q']:.6f}")
```

---

## Personnalisation

### Ajouter vos Propres Parametres

```python
# Au debut du notebook, definir vos valeurs
MES_CONDITIONS = {
    'Hm0': 3.2,
    'Tm_10': 7.8,
    'h': 11.5,
    'Rc': 2.8,
    'alpha_deg': 32.0,
    'gamma_f': 0.55
}

# Puis utiliser partout
q = overtopping.digue_talus(**MES_CONDITIONS)
```

### Modifier les Graphiques

```python
# Changer les couleurs
COLORS = {
    'eurotop': '#FF5722',  # Orange
    'xgboost': '#4CAF50',  # Vert
    'neural': '#9C27B0'    # Violet
}

# Ajuster la taille
plt.figure(figsize=(16, 10))
```

---

## References

### Guide EurOtop 2018
- Chapitre 5 : Digues a talus
- Chapitre 6 : Murs verticaux
- Chapitre 7 : Structures composites

### Base CLASH
- Van der Meer et al. (2005)
- 10,533 tests physiques
- Source pour Neural Network et XGBoost

### Documentation OpenEurOtop
- ../docs/ : Documentation Sphinx complete
- ADVANCED_MODELS_RESULTS.md : Resultats detailles
- FINAL_IMPLEMENTATION_SUMMARY.md : Vue d'ensemble

---

## Quick Start

```bash
# Cloner et installer
git clone <repo>
cd OpenEurOtop
pip install -e .

# Installer dependances notebooks
pip install matplotlib pandas jupytext

# Lancer un exemple
cd examples
python notebook_01_introduction_comparative.py

# Les images sont generees dans le repertoire courant
```

---

## Support

### Questions Frequentes

Q: XGBoost donne des resultats tres differents d'EurOtop ?
R: C'est normal pour certains cas extremes. XGBoost est entraine sur CLASH qui a ses limites. Toujours valider avec EurOtop pour le design.

Q: Puis-je utiliser XGBoost pour le design final ?
R: Non. Les formules EurOtop sont la reference scientifique. XGBoost sert de verification rapide.

Q: Le Neural Network donne de mauvais resultats ?
R: Normal, R2=0.67 seulement. Preferer XGBoost (R2=0.88) ou EurOtop.

Q: Comment ajouter l'obliquite des vagues ?
R: Utiliser le parametre gamma_beta :
```python
q = overtopping.digue_talus(Hm0, Tm_10, h, Rc, alpha, gamma_beta=0.9)
```

---

## Contributions

Vos retours sont les bienvenus :
- Signaler des bugs
- Proposer de nouveaux exemples
- Partager vos cas d'usage
- Ameliorer la documentation

---

OpenEurOtop v0.3.0-beta
Developpe pour les ingenieurs cotiers
Base CLASH : 9,324 tests physiques
XGBoost optimise : R2 = 0.88
