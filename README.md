#  Análisis de Propiedades Edáficas de Suelos Colombianos

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-1.3%2B-orange?logo=pandas)](https://pandas.pydata.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

> Aplicación en Python para consultar y analizar las propiedades edáficas (pH, Fósforo, Potasio) de suelos agrícolas en Colombia, específicamente para cultivos prioritarios del Departamento de Risaralda. Este proyecto fue desarrollado como parte del curso de Programación 4 de la Universidad Tecnológica de Pereira.

# Objetivo
Permitir a usuarios consultar propiedades de suelos mediante filtros por departamento, municipio, cultivo y visualizar resultados tabulares con análisis estadístico de las variables edáficas.

##  Tabla de Contenidos

- [ Características](#-características)
- [ Instalación](#-instalación)
- [ Uso](#-uso)
- [ Arquitectura](#-arquitectura)
- [ Ejemplo](#-ejemplo)

##  Características

| Funcionalidad | Descripción |
|--------------|-------------|
|  **Búsqueda Inteligente** | Encuentra automáticamente el archivo Excel |
|  **Análisis Estadístico** | Calcula medianas de pH, Fósforo y Potasio |
|  **Filtros Avanzados** | Por departamento, municipio y cultivo |
|  **Interfaz Amigable** | Tablas formateadas y colores en consola |
|  **Validación de Datos** | Verifica estructura del archivo Excel |

##  Instalación

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/tu-usuario/proyecto-suelos.git
cd proyecto-suelos
```
2. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

## Uso

### Ejecución básica
```bash
python main.py
```
### Flujo del programa

- Busqueda automatica del archivo Excel
- Carga y validación de datos
- Consulta interactiva de parámetros
- Filtrado y análisis de datos
- Visualización de resultados

### Ejemplo de consulta
```python
# Entradas del usuario:
Departamento: Risaralda
Municipio: Pereira  
Cultivo: Café
Registros: 5
```

## Arquitectura
### Diagrama de componentes

