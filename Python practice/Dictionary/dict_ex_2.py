# filtering dictionary examples
# 1. Given key convert its value in upper case
city_names = {'Anand' : 0 , 'Khambhat' : 0 , 'Surat' : 0 , 'Baroda' : 0}
for k in city_names:
    city_names[k] = k.upper()
print(city_names)
  
    
# 2. Given key find its value's length
city_names1 = {'Anand' : '' , 'Khambhat' : '' , 'Surat' : '' , 'Baroda' : ''}
for k in city_names1:
    city_names1[k] = len(k)
print(city_names1)


# 3. Dictionary inside list 
# From this do filtering :- find products whose units_sold are more than 100.
sales_data = [{"product": "Pen", "price": 10, "units_sold": 10},
    {"product": "Notebook", "price": 50, "units_sold": 90},
    {"product": "Pencil", "price": 5, "units_sold": 300},
    ]
for i in sales_data:
    if i['units_sold'] > 100 :
        print(f"Product details whose units sold are more than 100 : {i}")
print(f"Length of list : {len(sales_data)}")


# 4. fetch/filter only those product whose units_sold are more then 100
sales_data = {
    "Pen": {"product_discription": "Pentonic Pen", "price": 10, "units_sold": 150},
    "Notebook" : {"product_discription": "DOMS Notebook", "price": 50, "units_sold": 90},
    "Pencil" :  {"product_discription": "DOMS Pencil", "price": 5, "units_sold": 300},
}
for i,v in sales_data.items():
   if v['units_sold'] > 100:
    print(f"{i} - {v}")


