# nuevainglaterra
Ejemplo simple con django para control de inventarios usando el panel administrativo de django


Crear el entorno virtual con nombre ENV_NUEVA_INGLATERRA
```bash
python3 -m venv ENV_NUEVA_INGLATERRA
```

Activar el entorno virtual
```bash
source ENV_NUEVA_INGLATERRA/bin/activate
```
Instalar dependencias
```bash
pip install -r requirements.txt
```

Crear las migraciones de modelos nuevos
```bash
python manage.py makemigrations
```

Correr las migraciones
```bash
python manage.py migrate
```

Crear super usuario
```bash
python manage.py createsupersuser
```

Levantar el servidor
```bash
python manage.py runserver
```

