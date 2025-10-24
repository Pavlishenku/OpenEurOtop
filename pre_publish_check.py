#!/usr/bin/env python
"""
Script de vérification pré-publication pour OpenEurOtop v1.0.0
Vérifie que tout est en ordre avant la publication sur GitHub et PyPI
"""

import os
import sys
from pathlib import Path


class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'


def check_mark(status):
    """Retourne un symbole selon le statut"""
    # Utiliser des caractères ASCII pour compatibilité Windows
    return f"{Colors.GREEN}[OK]{Colors.END}" if status else f"{Colors.RED}[FAIL]{Colors.END}"


def print_header(title):
    """Affiche un titre formaté"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'=' * 60}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{title}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'=' * 60}{Colors.END}\n")


def check_file_exists(filepath, description):
    """Vérifie qu'un fichier existe"""
    exists = os.path.exists(filepath)
    print(f"{check_mark(exists)} {description}: {filepath}")
    return exists


def check_file_contains(filepath, text, description):
    """Vérifie qu'un fichier contient un texte"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            contains = text in content
            print(f"{check_mark(contains)} {description}")
            if not contains:
                print(f"   {Colors.YELLOW}WARNING: '{text}' non trouve dans {filepath}{Colors.END}")
            return contains
    except Exception as e:
        print(f"{check_mark(False)} {description}")
        print(f"   {Colors.RED}Erreur: {e}{Colors.END}")
        return False


def check_no_temp_files():
    """Vérifie qu'il n'y a pas de fichiers temporaires qui seront commitées"""
    print_header("Vérification des fichiers temporaires")
    
    # Fichiers qui ne devraient PAS être commitées
    temp_patterns = [
        '*.egg-info/',
        'build/',
        'dist/',
        '__pycache__/',
        '.pytest_cache/',
        'htmlcov/',
        '.coverage',
        'coverage.xml',
    ]
    
    issues = []
    for pattern in temp_patterns:
        path = Path(pattern.rstrip('/'))
        if path.exists():
            issues.append(pattern)
            print(f"{check_mark(False)} {pattern} existe (devrait etre dans .gitignore)")
    
    if not issues:
        print(f"{check_mark(True)} Pas de fichiers temporaires detectes")
        return True
    else:
        print(f"\n{Colors.YELLOW}WARNING: {len(issues)} fichier(s) temporaire(s) detecte(s){Colors.END}")
        print(f"   Ces fichiers seront ignores par Git grace au .gitignore")
        return True  # Ce n'est pas bloquant grâce au gitignore


def main():
    """Fonction principale"""
    print(f"\n{Colors.BOLD}OpenEurOtop v1.0.0 - Vérification pré-publication{Colors.END}")
    
    all_checks = []
    
    # 1. Fichiers essentiels
    print_header("1. Fichiers essentiels")
    all_checks.append(check_file_exists('README.md', 'README'))
    all_checks.append(check_file_exists('LICENSE', 'License'))
    all_checks.append(check_file_exists('CHANGELOG.md', 'Changelog'))
    all_checks.append(check_file_exists('setup.py', 'Setup script'))
    all_checks.append(check_file_exists('pyproject.toml', 'PyProject config'))
    all_checks.append(check_file_exists('requirements.txt', 'Requirements'))
    all_checks.append(check_file_exists('MANIFEST.in', 'Manifest'))
    
    # 2. Configuration Git et CI/CD
    print_header("2. Configuration Git et CI/CD")
    all_checks.append(check_file_exists('.gitignore', '.gitignore'))
    all_checks.append(check_file_exists('.github/workflows/ci.yml', 'CI Workflow'))
    all_checks.append(check_file_exists('.github/workflows/docs.yml', 'Docs Workflow'))
    all_checks.append(check_file_exists('.github/workflows/publish.yml', 'Publish Workflow'))
    
    # 3. Documentation
    print_header("3. Documentation")
    all_checks.append(check_file_exists('CONTRIBUTING.md', 'Contribution guide'))
    all_checks.append(check_file_exists('GUIDE_PUBLICATION.md', 'Publication guide'))
    all_checks.append(check_file_exists('PUBLICATION_CHECKLIST.md', 'Publication checklist'))
    all_checks.append(check_file_exists('.readthedocs.yaml', 'ReadTheDocs config'))
    
    # 4. Scripts et outils
    print_header("4. Scripts et outils")
    all_checks.append(check_file_exists('build_and_publish.py', 'Build script'))
    all_checks.append(check_file_exists('publish_to_github.bat', 'GitHub publish script (Windows)'))
    all_checks.append(check_file_exists('.pypirc.template', 'PyPI config template'))
    
    # 5. Code source
    print_header("5. Code source")
    all_checks.append(check_file_exists('openeurotop/__init__.py', 'Package __init__'))
    all_checks.append(check_file_exists('openeurotop/overtopping.py', 'Module overtopping'))
    all_checks.append(check_file_exists('openeurotop/wave_parameters.py', 'Module wave_parameters'))
    all_checks.append(check_file_exists('openeurotop/reduction_factors.py', 'Module reduction_factors'))
    
    # 6. Vérification des versions
    print_header("6. Vérification des versions")
    all_checks.append(check_file_contains('setup.py', 'version="1.0.0"', 'Version dans setup.py = 1.0.0'))
    all_checks.append(check_file_contains('pyproject.toml', 'version = "1.0.0"', 'Version dans pyproject.toml = 1.0.0'))
    all_checks.append(check_file_contains('CHANGELOG.md', '[1.0.0]', 'Version 1.0.0 dans CHANGELOG'))
    
    # 7. Vérification README
    print_header("7. Vérification README.md")
    all_checks.append(check_file_contains('README.md', '![PyPI version]', 'Badge PyPI dans README'))
    all_checks.append(check_file_contains('README.md', 'pip install openeurotop', 'Instructions installation'))
    all_checks.append(check_file_contains('README.md', 'github.com/Pavlishenku/OpenEurOtop', 'URL GitHub correcte'))
    
    # 8. Vérification .gitignore
    print_header("8. Vérification .gitignore")
    all_checks.append(check_file_contains('.gitignore', '*.md', 'Exclusion fichiers .md temporaires'))
    all_checks.append(check_file_contains('.gitignore', '*.txt', 'Exclusion fichiers .txt temporaires'))
    all_checks.append(check_file_contains('.gitignore', '.pypirc', 'Exclusion .pypirc (sécurité)'))
    all_checks.append(check_file_contains('.gitignore', 'venv_*/', 'Exclusion environnements virtuels'))
    
    # 9. Fichiers temporaires
    all_checks.append(check_no_temp_files())
    
    # Résumé final
    print_header("RÉSUMÉ")
    
    total = len(all_checks)
    passed = sum(all_checks)
    failed = total - passed
    
    print(f"Total de verifications : {total}")
    print(f"{Colors.GREEN}Reussies : {passed}{Colors.END}")
    if failed > 0:
        print(f"{Colors.RED}Echouees : {failed}{Colors.END}")
    
    print()
    
    if all(all_checks):
        print(f"{Colors.GREEN}{Colors.BOLD}SUCCESS: TOUS LES CONTROLES SONT PASSES !{Colors.END}")
        print(f"\n{Colors.BOLD}Le projet est pret pour la publication.{Colors.END}")
        print(f"\nProchaines etapes :")
        print(f"1. Executer : {Colors.BLUE}publish_to_github.bat{Colors.END} (ou commandes Git manuelles)")
        print(f"2. Creer une Release sur GitHub")
        print(f"3. Publier sur Test PyPI : {Colors.BLUE}python build_and_publish.py test{Colors.END}")
        print(f"4. Publier sur PyPI : {Colors.BLUE}python build_and_publish.py publish{Colors.END}")
        print(f"\nConsultez {Colors.BLUE}GUIDE_PUBLICATION.md{Colors.END} pour les details")
        return 0
    else:
        print(f"{Colors.YELLOW}WARNING: CERTAINES VERIFICATIONS ONT ECHOUE{Colors.END}")
        print(f"\nVeuillez corriger les problemes avant de publier.")
        print(f"Consultez les messages ci-dessus pour plus de details.")
        return 1


if __name__ == '__main__':
    sys.exit(main())

