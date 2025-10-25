# Tests

Ce dossier contient les tests unitaires pour le package OpenEurOtop.

## Execution des tests

### Avec pytest (recommande)

```bash
pip install pytest
pytest
```

### Sans pytest

```bash
cd tests
python test_overtopping.py
```

## Tests inclus

Le fichier test_overtopping.py contient 12 tests :

1. test_digue_talus_basic - Test basique pour digue a talus
2. test_digue_talus_revanche_elevee - Test avec differentes revanches
3. test_effet_rugosite - Verification de l'effet de la rugosite
4. test_mur_vertical - Test pour mur vertical
5. test_structure_composite - Test pour structure composite
6. test_iribarren_number - Calcul du nombre d'Iribarren
7. test_gamma_f_roughness - Facteurs de rugosite
8. test_gamma_beta_obliquity - Facteur d'obliquite
9. test_wave_length - Calcul de longueur d'onde
10. test_volumes_franchissement - Calcul de volumes
11. test_digue_en_enrochement - Test pour enrochement
12. test_coherence_methodes - Coherence entre methodes

## Ajout de nouveaux tests

Pour ajouter de nouveaux tests, creez des fonctions commencant par test_ dans un fichier test_*.py.

Exemple :

```python
def test_ma_nouvelle_fonction():
    result = ma_fonction(param1, param2)
    assert result > 0, "Le resultat doit etre positif"
    print(f"test_ma_nouvelle_fonction: result = {result}")
```

