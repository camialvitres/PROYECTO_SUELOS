import os
from api import cargar_datos, filtrar_datos, calcular_mediana_variables
from ui import obtener_entrada_usuario, mostrar_tabla
from utils import validar_datos


"""
    FUNCIÓN: encontrar_archivo_excel
    PROPÓSITO: Buscar el archivo Excel específico en ubicaciones predeterminadas
    PARÁMETROS:
        Ninguno: La función busca en rutas predefinidas
    RETORNO:
        str: Ruta completa al archivo si se encuentra
        None: Si el archivo no existe en ninguna ubicación esperada
"""
def encontrar_archivo_excel():
    nombre_exacto = "resultado_laboratorio_suelo.xlsx"
    
    # Primero busca en la carpeta datos/
    ruta_datos = os.path.join("datos", nombre_exacto)
    if os.path.exists(ruta_datos):
        return ruta_datos
    
    # Luego busca en la carpeta actual
    if os.path.exists(nombre_exacto):
        return nombre_exacto
    
    # Si no lo encuentra en ninguna de las dos ubicaciones
    return None



def main():
    print("Buscando archivo resultado_laboratorio_suelo.xlsx...")
    ruta_archivo = encontrar_archivo_excel()
    
    if ruta_archivo is None:
        print("ERROR: No se encontró el archivo 'resultado_laboratorio_suelo.xlsx'")
        print("Por favor, asegúrate de que:")
        print("   1. El archivo se llame EXACTAMENTE: resultado_laboratorio_suelo.xlsx")
        print("   2. Esté en la carpeta principal O en la carpeta 'datos/'")
        print("   3. La carpeta 'datos/' existe y contiene el archivo")
        return
    
    print(f"Archivo encontrado: {ruta_archivo}")
    print("Cargando datos...")
    
    df = cargar_datos(ruta_archivo)
    
    if df is None:
        print("No se pudo cargar el archivo de datos.")
        return
    
    print(f"Datos cargados correctamente")
    print(f"Número de registros: {len(df)}")
    print(f"Columnas disponibles: {list(df.columns)}")
    print()
    
    # Validar estructura
    if not validar_datos(df):
        print("El archivo no tiene la estructura esperada.")
        return
    
    # Obtener parámetros de búsqueda
    departamento, municipio, cultivo, limite = obtener_entrada_usuario()
    
    # Filtrar datos
    datos_filtrados = filtrar_datos(df, departamento, municipio, cultivo, limite)
    
    if datos_filtrados.empty:
        print(f"No se encontraron resultados para:")
        print(f"  Departamento: {departamento}")
        print(f"  Municipio: {municipio}")
        print(f"  Cultivo: {cultivo}")
        return
    
    # Calcular medianas y mostrar resultados
    medianas = calcular_mediana_variables(datos_filtrados)
    mostrar_tabla(datos_filtrados, medianas)

if __name__ == "__main__":

    main()
