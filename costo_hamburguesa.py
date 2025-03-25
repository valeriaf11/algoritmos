#Calculate the selling price of a hamburger
# Ingredient costs
pan = 6  #Bimbo bread
carne = 20  # Approximately 80 grams 
queso = 8 # 1 slice of Cheese 
jitomate = 2  # 2 slices of tomato 
lechuga = 14  # 2 lettuce leaves 
cebolla = 2  # 2 slices of onion 
catsup = 0.77  # 15 grams of Clemente Jacques ketchup 
mayonesa = 1.30  # 15 grams of McCormick mayonnaise
mostaza = 0.85  # 10 grams of McCormick mustard 

# Fixed costs
empaque = 4
energia = 1
mano_obra = 23
alquiler = 4000  # Monthly rent

# Estimated monthly hamburger sales
hamburguesas_al_mes = 450  # Now 450 hamburgers are sold per month
alquiler_por_hamburguesa = alquiler / hamburguesas_al_mes  # Rental cost per hamburger

# Calculation of the total cost for each hamburger
costo_total = (pan + carne + queso + jitomate + lechuga + cebolla +
               catsup + mayonesa + mostaza + empaque + energia +
               mano_obra + alquiler_por_hamburguesa)

# Desired profit margin (percentage)
margen_ganancia = 30  # 30% profit

# Final sale price
precio_venta = costo_total * (1 + margen_ganancia / 100)

# Result
print(f"Costo total por hamburguesa: ${costo_total:.2f}")
print(f"Precio de venta con {margen_ganancia}% de ganancia: ${precio_venta:.2f}")
