@echo off
echo [1/6] Pulizia cache Python...
for /d /r . %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d"

echo [2/6] Reset completo Git locale...
if exist .git rd /s /q .git

echo [3/6] Inizializzazione nuovo repository...
git init

echo [4/6] Aggiunta file e creazione Commit...
:: Forza l'aggiunta di tutti i file
git add --all
:: Il commit DEVE avere successo per creare il ramo main
git commit -m "RentalCars rel 1.0.0 "

echo [5/6] Configurazione ramo Main e Remote...
git branch -M main
:: MODIFICA L'URL QUI SOTTO
git remote add origin https://github.com/7mbrini/rentalcars-tesi

echo [6/6] Caricamento forzato su GitHub...
:: Adesso il ramo main esiste e puo' essere inviato
git push -f origin main

echo.
echo ==========================================
echo    RESET GITHUB COMPLETATO CON SUCCESSO!
echo ==========================================
pause
