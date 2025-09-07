import pandas as pd


"""
    FUNCIÓN: validar_datos
    PROPÓSITO: Validar que el DataFrame tenga la estructura y columnas requeridas para el análisis
    PARÁMETROS:
        df (DataFrame): Dataset a validar
    RETORNO:
        bool: True si el dataset tiene la estructura esperada, False en caso contrario
"""
def validar_datos(df):
    columnas_requeridas = ['DEPARTAMENTO', 'MUNICIPIO', 'CULTIVO', 'TOPOGRAFIA']
    columnas_variables = [
        'PH AGUA:SUELO 2,5:1,0', 
        'FÓSFORO (P) BRAY II MG/KG', 
        'POTASIO (K) INTERCAMBIABLE CMOL(+)/KG'
    ]
    
    for col in columnas_requeridas:
        if col not in df.columns:
            print(f"❌ Columna faltante: {col}")
            return False
    
    variables_presentes = [col for col in columnas_variables if col in df.columns]
    if len(variables_presentes) == 0:
        print("❌ No se encontraron las variables edáficas (PH, Fósforo, Potasio)")
        return False
    
    return True


"""
    FUNCIÓN: obtener_cultivos_disponibles
    PROPÓSITO: Obtener lista de cultivos disponibles para un departamento y municipio específicos
    PARÁMETROS:
        df (DataFrame): Dataset completo de análisis de suelos
        departamento (str): Nombre del departamento a consultar
        municipio (str): Nombre del municipio a consultar
    RETORNO:
        list: Lista ordenada de cultivos disponibles en la ubicación especificada
        list vacía: Si no hay datos o ocurre error
"""
def obtener_cultivos_disponibles(df, departamento, municipio):
    try:
        filtro_depto = df[df['DEPARTAMENTO'].str.lower() == departamento.lower()]
        filtro_mun = filtro_depto[filtro_depto['MUNICIPIO'].str.lower() == municipio.lower()]
        
        cultivos = filtro_mun['CULTIVO'].unique()
        return sorted([cultivo for cultivo in cultivos if pd.notna(cultivo)])
    except:
        return []