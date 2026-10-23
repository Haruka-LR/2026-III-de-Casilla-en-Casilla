# 2026-III-de-Casilla-en-Casilla

## Ejecutar en desarrollo

El proyecto usa Supabase como base de datos mediante la variable `DATABASE_URL`
definida en el archivo `.env` de la raíz del repositorio. No compartas ese archivo
ni guardes credenciales en el código fuente.

Desde la carpeta `De_Casilla_en_Casilla`, ejecuta:

```powershell
python manage.py migrate
python manage.py runserver
```