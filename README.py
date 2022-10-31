# Botilleria


class Product
{
	#Atributos

	id= #Codigo de barra del producto (marca, nombre del producto)
	supplier='' #Distribuidor 
	price= #Precio del producto
	content= #Contenido del producto (En gramos o en mililitros)
	category[''] #Categoria con la que se guardara el producto(Alcohol, abarrotes, dulces, etc...)
	

	#Metodos

	change_supplier() #Cambiar distruibor o mantenerlo
	change_category() #aaa
}

class Inventory
{
	#Atributos
	
	product_id= #Codigo de barra del producto (Marca, nombre del producto)
	product_category= #Categoria de los productos
	quantity_category= #Cantidad de producto en 'N' categoria
	stock= #Cantidad de producto
	purchase_price= #Precio de compra de producto
	sale_price= #Precio de venta
	amount_sold= #Cantidad de producto vendido
	total_sales= #Cantidad de ventas de producto
	
	#Métodos
	
	show_info() #Mostrar los datos del producto
	change_info() #Actualizar datos del producto
	update_quantity([enteroption]) #Actualizacion de cantidades (categoria,stock)
	update_sale_price() #Actualizar el precio de venta del producto
	update_purchase_price() #Actualizar el precio de compra
	add_producto() #nuevo producto ingresado
	add_category() #Nueva categoria creada
	profit() #Ganancia de las ventas
	
	
	
}
