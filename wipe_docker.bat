@echo off
echo [1/3] Arresto di tutti i container in corso...
FOR /f "tokens=*" %%i IN ('docker ps -q') DO docker stop %%i

echo [2/3] Rimozione di tutti i container, immagini e reti...
echo [3/3] Eliminazione di tutti i volumi (Dati persistenti)...
docker system prune -a --volumes -f

echo.
echo Operazione completata! Docker e stato riportato allo stato originale.
pause
