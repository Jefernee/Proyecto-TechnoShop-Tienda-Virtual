


# TechnoShop MX - Tienda Virtual

## Descripción del proyecto
TechnoShop MX es una tienda en línea que inicia vendiendo celulares, audífonos y accesorios.  
El proyecto busca gestionar productos, pedidos, clientes y reseñas de manera eficiente usando **FastAPI**, **Beanie** y **MongoDB**.

Hasta ahora se ha configurado:

- Entorno virtual `venv` con Python 3.13.3
- Dependencias instaladas: FastAPI, Beanie, Motor, PyMongo, python-dotenv, uvicorn, entre otras.
- Estructura inicial de carpetas y archivos:
```
techno_shop/
├─ app/
│  ├─ main.py
│  ├─ config.py
│  └─ models/        <-- aquí van los modelos (clientes, productos, pedidos, etc.)
├─ requirements.txt
└─ README.md


````
- Configuración de Visual Studio Code con entorno `venv` activado y sin errores en importaciones.
- Conexión inicial a MongoDB y prueba de arranque de servidor FastAPI con `uvicorn`.

---

## Instalación

1. Clonar el repositorio:
 ```bash
 git clone https://github.com/TuUsuario/TechnoShop-FastAPI.git
 cd TechnoShop-FastAPI
````

2. Crear y activar entorno virtual:

   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # Windows PowerShell
   ```

3. Instalar dependencias:

   ```bash
   pip install -r requirements.txt
   ```

---

## Uso

1. Asegurarse de que MongoDB esté corriendo.
2. Levantar el servidor FastAPI:

   ```bash
   uvicorn app.main:app --reload
   ```
3. Acceder a la documentación interactiva en:

   ```
   http://127.0.0.1:8000/docs
   ```

---

## Estructura de la base de datos

Se usarán colecciones en MongoDB:

* **Clientes**: `_id`, `nombre`, `correo`, `telefono`, `direccion`, `puntos_fidelidad`, `participa_rifa`
* **SistemaPuntos**: `_id`, `cliente_id`, `puntos_acumulados`, `fecha_actualizacion`
* **Productos**: `_id`, `nombre`, `precio`, `descripcion`, `categoria`, `imagen`, `estado`
* **Pedidos**: `_id`, `cliente_id`, `fecha_pedido`, `estatus`, `forma_pago`
* **DetallePedido**: `_id`, `pedido_id`, `producto_id`, `cantidad`, `precio_unitario`
* **Reseñas**: `_id`, `cliente_id`, `producto_id`, `comentario`, `fecha`, `calificacion`
* **Inventario**: `_id`, `producto_id`, `cantidad_disponible`
* **Descuentos**: `_id`, `producto_id`, `cantidad_minima`, `porcentaje_descuento`, `fecha_inicio`, `fecha_fin`

---

## Estado actual del proyecto

* Proyecto funcional con FastAPI y conexión a MongoDB.
* API levantada y accesible localmente.
* Archivos y entorno virtual configurados correctamente.
* Listo para implementar modelos, rutas y lógica de negocio.

---

## Comandos útiles

* Activar entorno virtual:

  ```bash
  .\venv\Scripts\Activate.ps1
  ```
* Levantar API:

  ```bash
  uvicorn app.main:app --reload
  ```
* Instalar dependencias:

  ```bash
  pip install -r requirements.txt
  ```




