#!/usr/bin/env python
"""
Script de build et publication pour OpenEurOtop

Usage:
    python build_and_publish.py check       # Vérifier le package
    python build_and_publish.py build       # Construire le package
    python build_and_publish.py test        # Publier sur Test PyPI
    python build_and_publish.py publish     # Publier sur PyPI (production)
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path


def run_command(cmd, check=True):
    """Exécute une commande shell et affiche le résultat"""
    print(f"\n🔧 Exécution : {cmd}")
    print("-" * 60)
    result = subprocess.run(cmd, shell=True, check=check)
    return result.returncode == 0


def clean():
    """Nettoie les fichiers de build précédents"""
    print("\n🧹 Nettoyage des fichiers de build...")
    dirs_to_clean = ['build', 'dist', 'openeurotop.egg-info', 'htmlcov', '.pytest_cache']
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"   ✓ Supprimé : {dir_name}/")
    
    # Nettoyer les fichiers __pycache__
    for pycache in Path('.').rglob('__pycache__'):
        shutil.rmtree(pycache)
    
    print("   ✓ Nettoyage terminé")


def check():
    """Vérifie que le package est prêt pour publication"""
    print("\n🔍 Vérification du package...")
    
    checks = []
    
    # 1. Vérifier que les tests passent
    print("\n1️⃣ Exécution des tests...")
    if run_command("pytest tests/ -v", check=False):
        checks.append(("Tests unitaires", True))
    else:
        checks.append(("Tests unitaires", False))
    
    # 2. Vérifier la qualité du code
    print("\n2️⃣ Vérification du code avec flake8...")
    if run_command("flake8 openeurotop --count --select=E9,F63,F7,F82 --show-source --statistics", check=False):
        checks.append(("Qualité du code", True))
    else:
        checks.append(("Qualité du code", False))
    
    # 3. Vérifier que les fichiers importants existent
    print("\n3️⃣ Vérification des fichiers essentiels...")
    required_files = [
        'README.md',
        'LICENSE',
        'CHANGELOG.md',
        'setup.py',
        'pyproject.toml',
        'requirements.txt',
        'MANIFEST.in',
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if not missing_files:
        checks.append(("Fichiers essentiels", True))
    else:
        print(f"   ❌ Fichiers manquants : {', '.join(missing_files)}")
        checks.append(("Fichiers essentiels", False))
    
    # 4. Vérifier que la version est cohérente
    print("\n4️⃣ Vérification de la version...")
    version_ok = True
    try:
        with open('setup.py') as f:
            setup_content = f.read()
            if 'version="1.0.0"' not in setup_content:
                print("   ⚠️  Version dans setup.py n'est pas 1.0.0")
                version_ok = False
        
        with open('pyproject.toml') as f:
            toml_content = f.read()
            if 'version = "1.0.0"' not in toml_content:
                print("   ⚠️  Version dans pyproject.toml n'est pas 1.0.0")
                version_ok = False
        
        checks.append(("Cohérence version", version_ok))
    except Exception as e:
        print(f"   ❌ Erreur : {e}")
        checks.append(("Cohérence version", False))
    
    # Résumé
    print("\n" + "=" * 60)
    print("📊 RÉSUMÉ DES VÉRIFICATIONS")
    print("=" * 60)
    for name, status in checks:
        icon = "✅" if status else "❌"
        print(f"{icon} {name}")
    
    all_passed = all(status for _, status in checks)
    
    if all_passed:
        print("\n🎉 Toutes les vérifications sont passées !")
        print("   Vous pouvez procéder au build avec : python build_and_publish.py build")
        return True
    else:
        print("\n⚠️  Certaines vérifications ont échoué.")
        print("   Veuillez corriger les erreurs avant de continuer.")
        return False


def build():
    """Construit le package"""
    print("\n📦 Construction du package...")
    
    clean()
    
    if not run_command("python -m build"):
        print("\n❌ Erreur lors du build")
        return False
    
    print("\n✅ Build terminé avec succès")
    
    # Vérifier le package
    print("\n🔍 Vérification du package construit...")
    if not run_command("twine check dist/*"):
        print("\n❌ Le package a des erreurs")
        return False
    
    # Afficher le contenu
    print("\n📄 Contenu du package :")
    run_command("tar -tzf dist/openeurotop-1.0.0.tar.gz", check=False)
    
    print("\n✅ Package prêt pour publication !")
    print("   - Test PyPI : python build_and_publish.py test")
    print("   - PyPI Prod : python build_and_publish.py publish")
    
    return True


def test_publish():
    """Publie sur Test PyPI"""
    print("\n🚀 Publication sur Test PyPI...")
    
    if not os.path.exists('dist'):
        print("❌ Le dossier dist/ n'existe pas.")
        print("   Exécutez d'abord : python build_and_publish.py build")
        return False
    
    print("\n⚠️  Vous allez publier sur Test PyPI")
    response = input("Continuer ? (o/N) : ")
    if response.lower() != 'o':
        print("Publication annulée")
        return False
    
    if run_command("twine upload --repository testpypi dist/*", check=False):
        print("\n✅ Publication sur Test PyPI réussie !")
        print("\n📥 Pour tester l'installation :")
        print("   pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ openeurotop")
        return True
    else:
        print("\n❌ Erreur lors de la publication")
        return False


def publish():
    """Publie sur PyPI production"""
    print("\n🚀 Publication sur PyPI PRODUCTION...")
    
    if not os.path.exists('dist'):
        print("❌ Le dossier dist/ n'existe pas.")
        print("   Exécutez d'abord : python build_and_publish.py build")
        return False
    
    print("\n" + "⚠️ " * 20)
    print("ATTENTION : Vous allez publier sur PyPI PRODUCTION")
    print("Cette action est IRRÉVERSIBLE !")
    print("Assurez-vous que :")
    print("  - Tous les tests passent")
    print("  - La documentation est à jour")
    print("  - Le CHANGELOG est complet")
    print("  - Le package a été testé sur Test PyPI")
    print("⚠️ " * 20 + "\n")
    
    response = input("Taper 'PUBLIER' pour continuer : ")
    if response != 'PUBLIER':
        print("Publication annulée")
        return False
    
    if run_command("twine upload dist/*", check=False):
        print("\n🎉 Publication sur PyPI réussie !")
        print("\n📥 Pour installer :")
        print("   pip install openeurotop")
        print("\n🌐 Lien PyPI :")
        print("   https://pypi.org/project/openeurotop/")
        return True
    else:
        print("\n❌ Erreur lors de la publication")
        return False


def main():
    """Point d'entrée principal"""
    if len(sys.argv) < 2:
        print(__doc__)
        return
    
    command = sys.argv[1].lower()
    
    commands = {
        'check': check,
        'build': build,
        'test': test_publish,
        'publish': publish,
        'clean': clean,
    }
    
    if command not in commands:
        print(f"❌ Commande inconnue : {command}")
        print(__doc__)
        return
    
    commands[command]()


if __name__ == '__main__':
    main()

