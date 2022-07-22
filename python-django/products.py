products=[
    {"p_id":100,"p:name":"a52s","brand":"samsung","brand":"5g","price":37000},
    {"p_id": 101, "p:name": "a5", "brand": "samsung", "brand": "5g", "price": 32000},
    {"p_id": 102, "p:name": "iphone12", "brand": "apple", "brand": "4g", "price": 67000},
    {"p_id":103,"p:name":"iphone13","brand":"apple","brand":"4g","price":87000},
    {"p_id": 104, "p:name": "mi11i", "brand": "mi", "brand": "4g", "price": 21000},
    {"p_id": 105, "p:name": "redminote10", "brand": "mi", "brand": "4g", "price": 17000},
    {"p_id": 106, "p:name": "redmi10pro", "brand": "mi", "brand": "4g", "price": 20000},
    {"p_id": 107, "p:name": "motoedge", "brand": "motorola", "brand": "5g", "price": 27000},
    {"p_id": 108, "p:name": "motofusion", "brand": "samsung", "brand": "5g", "price": 37000},
]
#print all mobiles available in range of 15k-20k

mobile_filter=[mob for mob in products if mob["price"] in range(15000,20001)]
print(mobile_filter)

#print all 5g band mobiles
five_mobiles=[mob for mob in products if mob["brand"]=="5g"]
print(five_mobiles)

#sort mobiles based on price order by desc


products.sort(key=lambda mob:mob["price"],reverse=True)
print(products)

#costly mobile
costly_mob=max(products,key=lambda mob:mob["price"])
print(costly_mob)
#cheapest mob
costly_mob=min(products,key=lambda mob:mob["price"])
print(costly_mob)
