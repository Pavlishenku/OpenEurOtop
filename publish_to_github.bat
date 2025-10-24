@echo off
REM Script de publication sur GitHub pour Windows
REM Usage: publish_to_github.bat

echo ========================================
echo Publication OpenEurOtop v1.0.0
echo ========================================
echo.

REM Vérifier que Git est installé
where git >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ERREUR: Git n'est pas installe ou n'est pas dans le PATH
    echo Installez Git depuis https://git-scm.com/
    pause
    exit /b 1
)

REM Vérifier qu'on est dans le bon dossier
if not exist "openeurotop" (
    echo ERREUR: Le dossier openeurotop n'existe pas
    echo Assurez-vous d'etre dans le dossier racine du projet
    pause
    exit /b 1
)

echo.
echo 1. Verification du statut Git...
git status

echo.
echo 2. Initialisation du repository (si necessaire)...
git init
git branch -M main

echo.
echo 3. Ajout du remote GitHub...
git remote remove origin 2>nul
git remote add origin https://github.com/Pavlishenku/OpenEurOtop.git

echo.
echo 4. Ajout de tous les fichiers...
git add .

echo.
echo 5. Creation du commit...
git commit -m "Release v1.0.0 - Premiere version stable"

echo.
echo 6. Push vers GitHub...
git push -u origin main

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ATTENTION: Le push a echoue. Cela peut etre normal si c'est la premiere fois.
    echo Essayez de vous authentifier et relancez le script.
    echo.
    echo Si vous utilisez l'authentification par token:
    echo - Username: votre nom d'utilisateur GitHub
    echo - Password: votre Personal Access Token (pas votre mot de passe!)
    echo.
    echo Pour creer un token: https://github.com/settings/tokens
    pause
    exit /b 1
)

echo.
echo 7. Creation du tag v1.0.0...
git tag -a v1.0.0 -m "Version 1.0.0 - Premiere version stable"

echo.
echo 8. Push du tag...
git push origin v1.0.0

echo.
echo ========================================
echo SUCCES!
echo ========================================
echo.
echo Le code a ete pousse sur GitHub!
echo.
echo PROCHAINES ETAPES:
echo 1. Allez sur https://github.com/Pavlishenku/OpenEurOtop
echo 2. Verifiez que tout est present
echo 3. Creez une Release depuis le tag v1.0.0
echo 4. Configurez les Secrets GitHub (PYPI_API_TOKEN)
echo.
echo Consultez GUIDE_PUBLICATION.md pour plus de details
echo.
pause

