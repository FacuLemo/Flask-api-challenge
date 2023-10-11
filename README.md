# Puede fallar
dijo tusam.
# 
Hay que tener en cuenta que el archivo '.env' y las carpetas 'migrations' y 'venv' están contemplados dentro del .gitignore y por eso no están.
La base de datos local tiene por nombre 'autoevaluacion'

RECORDAR que para que funcione la creacion de tablas en las migraciones, el archivo /migrations/env.py tiene que tener la siguiente línea:
```bash
from app.models.models import (User,Post,Comment,Category)
```

