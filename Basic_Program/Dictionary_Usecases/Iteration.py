#Author :: AMISONEJI
#Sample Program for ascennding and descending a dictionary.

#Python program to iterate over dictionaries using for loops

D={"Sonu":1,"Monu":2,"Chintu":3,"Shivu":4}
for key,values in D.items():
    print(key,values)

# Python program to match key values in two dictionaries.
   
D1={'key1': 1, 'key2': 3, 'key3': 2}
D2={'key1': 1, 'key2': 2}

for i in D1.values():
    if i in D2.values():
        print ( "key present",i)
