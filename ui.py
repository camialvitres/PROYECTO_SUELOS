from tabulate import tabulate


"""
    FUNCIÓN: mostrar_tabla
    PROPÓSITO: Mostrar resultados de consulta en formato de tabla organizada con medianas
    PARÁMETROS:
        datos (DataFrame): Dataset filtrado con registros a mostrar
        medianas (dict): Diccionario con valores medianos de variables edáficas
    RETORNO:
        None: La función solo imprime resultados en consola
"""

def mostrar_tabla(datos, medianas):
    if datos.empty:
        print("No se encontraron resultados para los criterios de búsqueda.")
        return
    
    columnas = ['DEPARTAMENTO', 'MUNICIPIO', 'CULTIVO', 'TOPOGRAFIA', 'PH', 'FOSFORO', 'POTASIO']
    columnas_disponibles = [col for col in columnas if col in datos.columns]
    tabla_datos = datos[columnas_disponibles]
    
    print("\n" + "="*80)
    print("RESULTADOS DE LA CONSULTA")
    print("="*80)
    print(tabulate(tabla_datos, headers='keys', tablefmt='grid', showindex=False))
    
    # Muestra las medianas
    print("\n" + "-"*40)
    print("MEDIANAS DE VARIABLES EDÁFICAS")
    print("-"*40)
    for variable, mediana in medianas.items():
        if mediana is not None:
            print(f"{variable}: {mediana:.2f}")
        else:
            print(f"{variable}: No disponible")


"""
    FUNCIÓN: obtener_entrada_usuario
    PROPÓSITO: Capturar y validar parámetros de búsqueda ingresados por el usuario
    PARÁMETROS:
        Ninguno: La función obtiene inputs directamente del usuario
    RETORNO:
        tuple: Tupla con (departamento, municipio, cultivo, limite) validados
"""
def obtener_entrada_usuario():
    print("CONSULTA DE PROPIEDADES EDÁFICAS")
    print("Estudiante: Camila Alvitres Cabeza")
    print("Por favor ingresa los siguientes parámetros para filtrar los datos:")
    print("="*60)
    
    departamento = input("Departamento (ej: Risaralda): ").strip()
    municipio = input("Municipio: ").strip()
    cultivo = input("Cultivo: ").strip()
    
    while True:
        try:
            limite = int(input("Número de registros a consultar: ").strip())
            if limite > 0:
                break
            else:
                print("Por favor ingrese un número positivo.")
        except ValueError:
            print("Por favor ingrese un número válido.")
    
    return departamento, municipio, cultivo, limite

