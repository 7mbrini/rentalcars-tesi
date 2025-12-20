@echo off
echo [1/5] Spegnimento container e rimozione volumi...
docker-compose down -v

echo [2/5] Pulizia profonda del sistema Docker...
docker system prune -f

echo [3/5] Pulizia cache Python (Windows)...
for /d /r . %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d"

echo [4/5] Ricostruzione e avvio (senza cache)...
docker-compose up --build -d

echo [5/5] Applicazione migrazioni database...
:: Attendiamo qualche secondo che il database sia pronto
timeout /t 15
docker-compose exec web python manage.py migrate

set DJANGO_SUPERUSER_PASSWORD=admin
docker-compose exec web python manage.py createsuperuser --noinput --username admin --email admin@example.com

echo.
echo ==========================================
echo    RESET COMPLETATO CON SUCCESSO!
echo ==========================================
pause
