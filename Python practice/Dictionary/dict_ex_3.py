# Nested Dictionary example
cars_data = {
    "Ev" : { "Maruti" : {"Baleno" : {"Price" : 120000 , "model" : "IPO" } ,
                          "Scross" : {"price" : 110000 , "model" : "ads"}
                        }, 
             "Hyundai" : { "i10" : {"Price" : 13000, "model" : "autometic"} ,
                            "Creta" : {"price" : 70000, "model" : "Manual"}
                         } ,
             "KIA" :    {  "Sonet" : { "Price" : 730000 , "model" : "ADAS"} ,
                           "Syros" : {"price": 100000 , "model" : "Base model"} 
                        }         
            } ,
    "Petrol" : { "Maruti" : {"Baleno" : {"Price" : 120000 , "model" : "IPO" } ,
                              "Scross" : {"price" : 110000 , "model" : "ads"}
                            }, 
                  "Hyundai": { "i10" : {"Price" : 13000, "model" : "autometic"} ,
                              "Creta" : {"price" : 70000, "model" : "Manual"}
                            } ,
                  "KIA" :   {  "Sonet" : { "Price" : 730000 , "model" : "ADAS"} ,
                              "Syros" : {"price": 100000 , "model" : "Base model"} 
                            },
                  "TATA" :  {  "Altroz" : {"Price" : 630000 , "model" : "Top model"} ,
                               "Punch" : {" price" : 550000 , "model" : "AMT"}
                            }
                },
    "Diesel" : { "Maruti" : {"Baleno" : {"Price" : 120000 , "model" : "IPO" } ,
                              "Scross" : {"price" : 110000 , "model" : "ads"}
                            }, 
                  "Hyundai": { "i10" : {"Price" : 13000, "model" : "autometic"} ,
                              "Creta" : {"price" : 70000, "model" : "Manual"}
                            } ,
                  "KIA" :   {  "Sonet" : { "Price" : 730000 , "model" : "ADAS"} ,
                              "Syros" : {"price": 100000 , "model" : "Base model"} 
                            }
                }
}
tata_cars = cars_data["Petrol"]["TATA"]
print(tata_cars) # first way simple way
# both gives same answer
for k,v in tata_cars.items(): # systematic way 
    print(f"{k} --> {v}")

    