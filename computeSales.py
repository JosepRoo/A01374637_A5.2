"""Calcula el total de ventas basado en el catálogo de precios y los registros de ventas."""

import json
import sys
import time

def load_json_data(filename):
    """Carga datos desde un archivo JSON."""
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Archivo no encontrado: {filename}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error al decodificar JSON en el archivo: {filename}")
        sys.exit(1)

def calculate_sales_total(prices_catalog, sales_records):
    """Calcula el total de ventas basado en el catálogo de precios y los registros de ventas."""
    total_sales = 0
    for sale in sales_records:
        product = sale.get("Product")
        quantity = sale.get("Quantity")
        product_price = prices_catalog.get(product, 0)
        total_sales += product_price * quantity
    return total_sales

def main(prices_file, sales_file):
    """Función principal."""
    start_time = time.time()

    # Cargar el catálogo de precios y registros de ventas desde los archivos JSON
    prices_catalog = {product["title"]: product["price"] for product in load_json_data(prices_file)}
    sales_records = load_json_data(sales_file)

    # Calcular el total de ventas
    total_sales = calculate_sales_total(prices_catalog, sales_records)

    # Escribir los resultados en la pantalla y en el archivo
    results_str = f"Total de ventas: ${total_sales:.2f}"
    print(results_str)

    with open("SalesResults.txt", "w", encoding="utf-8") as results_file:
        results_file.write(results_str + "\n")

    end_time = time.time()
    elapsed_time = end_time - start_time
    time_str = f"Tiempo total de ejecución: {elapsed_time:.2f} segundos"
    print(time_str)
    with open("SalesResults.txt", "a", encoding="utf-8") as results_file:
        results_file.write(time_str)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python computeSales.py priceCatalogue.json salesRecord.json")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
