# 2026-III-de-Casilla-en-Casilla

## Ejecutar en desarrollo

Por defecto, Django usa SQLite en `De_Casilla_en_Casilla/db.sqlite3`, por lo que
no necesita conectarse a Supabase para iniciar localmente. Desde la carpeta
`De_Casilla_en_Casilla`, ejecuta:

```powershell
python manage.py migrate
python manage.py runserver
```

Para usar Supabase en lugar de SQLite, configura `DJANGO_USE_SQLITE=False` y
`DATABASE_URL` con una URL de conexión vigente del proyecto, obtenida desde el
panel de Supabase. No guardes credenciales en el código fuente.