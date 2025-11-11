dict1 =  {1:0,2:0,3:0,4:0}
dict2  = {k : k**2 for k in dict1.keys()}
print(dict2)

# To find length of given state using comprehensive
state_city = {'Gujarat':0 , 'Maharashtra':0,'Rajasthan':0,'Orrisa':0}
state_city_length = {k:len(k) for k in state_city.keys()}
print(state_city_length)

# Convert capital into upper whose state's len is more than 7
state_city = {'Gujarat':'Ghandhinagar' , 'Maharashtra':'Mumbai','Rajasthan':'Udaipur','Orrisa':'Bhuneshwar'}
state_capital_upper = {k:v.upper() for k,v in state_city.items() if len(k) >7}
print(state_capital_upper)

# write Even and Odd corresponding to key's given.
no_dict = {1:0 , 2:0 , 3:0 , 4:0 , 5:0}
dict_even_odd = {k:"EVEN" if k%2 == 0 else "ODD" for k in no_dict.keys()}
print(dict_even_odd)

# covert capital into uppercase whose len > 7 and len < 7 then in lower case
state_city = {'Gujarat':'Ghandhinagar' , 'Maharashtra':'Mumbai','Rajasthan':'Udaipur','Orrisa':'Bhuneshwar'}
state_capital_upper = {k:v.upper() if len(v) > 7 else v.lower()  for k,v in state_city.items()}
print(state_capital_upper)
