import csv

# Carga de Datos
ventas = [
    {"fecha": "2024-01-01", "producto": "Producto A", "cantidad": 10, "precio": 100.0},
    {"fecha": "2024-01-02", "producto": "Producto B", "cantidad": 20, "precio": 200.0},
    {"fecha": "2024-01-03", "producto": "Producto A", "cantidad": 15, "precio": 100.0},
    {"fecha": "2024-01-04", "producto": "Producto C", "cantidad": 30, "precio": 300.0},
    {"fecha": "2024-01-05", "producto": "Producto B", "cantidad": 25, "precio": 200.0},
]

# Cálculo de Ingresos Totales
ingresos_totales = 0
for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta["precio"]

# Análisis del Producto Más Vendido
ventas_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    if producto in ventas_por_producto:
        ventas_por_producto[producto] += venta["cantidad"]
    else:
        ventas_por_producto[producto] = venta["cantidad"]
producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)

# Promedio de Precio por Producto
precios_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    if producto in precios_por_producto:
        precios_por_producto[producto] = (precios_por_producto[producto][0] + venta["cantidad"] * venta["precio"], precios_por_producto[producto][1] + venta["cantidad"])
    else:
        precios_por_producto[producto] = (venta["cantidad"] * venta["precio"], venta["cantidad"])
for producto, precio_cantidad in precios_por_producto.items():
    precios_por_producto[producto] = precio_cantidad[0] / precio_cantidad[1]

# Ventas por Día
ingresos_por_dia = {}
for venta in ventas:
    fecha = venta["fecha"]
    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += venta["cantidad"] * venta["precio"]
    else:
        ingresos_por_dia[fecha] = venta["cantidad"] * venta["precio"]

# Representación de Datos
resumen_ventas = {}
for venta in ventas:
    producto = venta["producto"]
    if producto in resumen_ventas:
        resumen_ventas[producto]["cantidad_total"] += venta["cantidad"]
        resumen_ventas[producto]["ingresos_totales"] += venta["cantidad"] * venta["precio"]
    else:
        resumen_ventas[producto] = {
            "cantidad_total": venta["cantidad"],
            "ingresos_totales": venta["cantidad"] * venta["precio"],
            "precio_promedio": 0
        }
for producto, datos in resumen_ventas.items():
    datos["precio_promedio"] = datos["ingresos_totales"] / datos["cantidad_total"]

# Generar archivo CSV
with open('resultados.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # Lista de ventas original
    writer.writerow(["Lista de Ventas Original"])
    writer.writerow(["Fecha", "Producto", "Cantidad", "Precio"])
    for venta in ventas:
        writer.writerow([venta["fecha"], venta["producto"], venta["cantidad"], venta["precio"]])
    
    # Ingresos totales generados
    writer.writerow(["Ingresos Totales Generados"])
    writer.writerow([ingresos_totales])
    
    # Producto más vendido y su cantidad total vendida
    writer.writerow(["Producto Más Vendido y Su Cantidad Total Vendida"])
    writer.writerow([producto_mas_vendido, ventas_por_producto[producto_mas_vendido]])
    
    # Precio promedio de venta por producto
    writer.writerow(["Precio Promedio de Venta por Producto"])
    writer.writerow(["Producto", "Precio Promedio"])
    for producto, precio in precios_por_producto.items():
        writer.writerow([producto, precio])
    
    # Ingresos totales por día
    writer.writerow(["Ingresos Totales por Día"])
    writer.writerow(["Fecha", "Ingresos Totales"])
    for fecha, ingresos in ingresos_por_dia.items():
        writer.writerow([fecha, ingresos])
    
    # Resumen de ventas por producto
    writer.writerow(["Resumen de Ventas por Producto"])
    writer.writerow(["Producto", "Cantidad Total", "Ingresos Totales", "Precio Promedio"])
    for producto, datos in resumen_ventas.items():
        writer.writerow([producto, datos["cantidad_total"], datos["ingresos_totales"], datos["precio_promedio"]])