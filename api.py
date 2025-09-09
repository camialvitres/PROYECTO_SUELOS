import pandas as pd
import numpy as np

"""
FUNCIÓN: cargar_datos
PROPÓSITO: Carga y prepara los datos desde el archivo Excel
PARÁMETROS:
  - ruta_archivo: Ruta completa al archivo Excel
RETORNO:
  - DataFrame de pandas con datos cargados y columnas estandarizadas
  - None si ocurre error durante la carga
MANEJO DE ERRORES: Captura excepciones y provee mensajes descriptivos
"""
def cargar_datos(ruta_archivo):
    try:
        df = pd.read_excel(ruta_archivo)
        # Limpiar nombres de columnas
        df.columns = df.columns.str.strip().str.upper()
        return df
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return None

def filtrar_datos(df, departamento, municipio, cultivo, limite):
    try:
        df_filtrado = df.copy()
        
        # Aplicar filtros progresivamente
        if departamento:
            df_filtrado = df_filtrado[df_filtrado['DEPARTAMENTO'].str.lower() == departamento.lower()]
        
        if municipio:
            df_filtrado = df_filtrado[df_filtrado['MUNICIPIO'].str.lower() == municipio.lower()]
        
        if cultivo:
            df_filtrado = df_filtrado[df_filtrado['CULTIVO'].str.lower() == cultivo.lower()]
        
        return df_filtrado.head(limite)
        
    except Exception as e:
        print(f"Error al filtrar datos: {e}")
        return pd.DataFrame()

"""
    FUNCIÓN: calcular_mediana_variables
    PROPÓSITO: Calcular medidas estadísticas de medianas para variables edáficas principales
    PARÁMETROS:
        df (DataFrame): Dataset con registros de análisis de suelos a analizar
    RETORNO:
        dict: Diccionario con medianas calculadas en formato {'PH': valor, 'FOSFORO': valor, 'POTASIO': valor}
        None: Si el DataFrame está vacío o no se pueden calcular las medianas
"""
def calcular_mediana_variables(df):
    if df.empty:
        return None
    
    variables = {
        'PH': 'PH AGUA:SUELO 2,5:1,0',
        'FOSFORO': 'FÓSFORO (P) BRAY II MG/KG', 
        'POTASIO': 'POTASIO (K) INTERCAMBIABLE CMOL(+)/KG'
    }
    
    medianas = {}
    
    for var_nombre, var_columna in variables.items():
        if var_columna in df.columns:
            # Convertir a numérico, manejando errores
            df[var_columna] = pd.to_numeric(df[var_columna], errors='coerce')
            medianas[var_nombre] = df[var_columna].median()
        else:
            medianas[var_nombre] = None
    

    return medianas

