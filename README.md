# Almacenes Nueva Inglaterra
Ejemplo simple con django para control de inventarios(basado en un caso de estudio) usando el panel administrativo de django


## Requerimientos:

Python 3.7.4 o superior

## Configuraciones

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
python manage.py createsuperuser
```

Levantar el servidor
```bash
python manage.py runserver
```

Registrar los tipos de movimientos disponibles:
1. Compras
2. Ventas
3. Devoluciones