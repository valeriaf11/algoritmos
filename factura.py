# Instalar reportlab si deseas exportar a PDF (solo la primera vez)
# !pip install reportlab
import json
import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

# Function to request the user's purchase details
def solicitar_detalles_compra():
    nombre_cliente = input("Nombre del cliente: ")
    productos = []
    while True:
        nombre_producto = input("Nombre del producto (o 'fin' para terminar): ")
        if nombre_producto.lower() == 'fin':
            break
        cantidad = int(input("Cantidad: "))
        precio_unitario = float(input("Precio unitario: "))
        productos.append((nombre_producto, cantidad, precio_unitario))

    # Generate unique invoice number
    numero_factura = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Request payment method
    print("\nMétodos de pago:")
    print("1. Efectivo")
    print("2. Tarjeta")
    print("3. PayPal")
    while True:
        metodo_pago = input("Seleccione un método de pago (1-3): ")
        if metodo_pago in ['Efectivo', '2', '3']:
            break
        print("❌ Opción inválida, ingrese, Tarjeta o PayPal.")
    return nombre_cliente, productos, numero_factura, metodo_pago

# Function for calculating invoice values
def calcular_factura(productos):
    subtotal = sum(cantidad * precio_unitario for _, cantidad, precio_unitario in productos)
    iva = subtotal * 0.16
    total = subtotal + iva
    return subtotal, iva, total

# Function to build invoice text (for export) - MODIFICADA
def generar_texto_factura(nombre_cliente, productos, subtotal, iva, total, metodo_pago):
    texto = "--- Factura ---\n"
    texto += f"Cliente: {nombre_cliente}\n\nProductos:\n"
    for nombre, cantidad, precio_unitario in productos:
        total_producto = cantidad * precio_unitario
        texto += f"{nombre} - {cantidad} x ${precio_unitario:.2f} = ${total_producto:.2f}\n"
    texto += f"\nSubtotal: ${subtotal:.2f}\n"
    texto += f"IVA (16%): ${iva:.2f}\n"
    texto += f"Total a pagar: ${total:.2f}\n"
    # Se agrega la línea para mostrar el método de pago:
    texto += f"Método de pago: {metodo_pago}\n"  
    texto += "----------------\n"
    return texto

# Export to TXT
def exportar_a_txt(nombre_archivo, contenido):
    with open(nombre_archivo, "w") as archivo:
        archivo.write(contenido)
    print(f"✅ Factura exportada como TXT: {nombre_archivo}")

# Export to PDF
def exportar_a_pdf(nombre_archivo, contenido):
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    width, height = letter
    y = height - 40
    for linea in contenido.split('\n'):
        c.drawString(40, y, linea)
        y -= 15
    c.save()
    print(f"✅ Factura exportada como PDF: {nombre_archivo}")

# Main function - MODIFICADA
def main():
    nombre_cliente, productos, numero_factura, metodo_pago = solicitar_detalles_compra()
    subtotal, iva, total = calcular_factura(productos)
    # Se pasa 'metodo_pago' a la función generar_texto_factura:
    texto_factura = generar_texto_factura(nombre_cliente, productos, subtotal, iva, total, metodo_pago) 
    
    # Imprimir en consola
    print(texto_factura)

    # Exportar
    exportar_a_txt("factura.txt", texto_factura)
    exportar_a_pdf("factura.pdf", texto_factura)

# Se asegura que el bloque 'if' esté a nivel de archivo y con la indentación correcta:
if _name_ == "_main_":
    main()
