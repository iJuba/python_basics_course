
#there is 3 data types :

# list : can store inside all variables types 
# define :
nbr_list = [1 , 2 ,3]
print(nbr_list)
print(type(nbr_list))

#list can have multiple variable types
multi_vars_list = ['strings',123, False ]
print(multi_vars_list)
# the constrator methode
constr_list = list(['gdsc',20114, True])
 
#operations :
#get an element or an interval of elements :
#first
print(nbr_list[0])
#last 
print(nbr_list[-1])
#range
print(nbr_list[1:2])

# get the index of and element:
print(nbr_list.index(3))

#check teh existance of an element in a list : use "in" key word , the output will be a booleen var
print(2 in nbr_list)
print('hello' in nbr_list)

# add an element to an existing list 

    #basic methode
nbr_list += 'hello'   
print(nbr_list) 
    #using the append methode
nbr_list.append('run')
print(nbr_list)

    
#add a list to an other list :
str_list = ['hi', 'by',"hello"] # note : if you use : double quots ""  used each char is considered as an element , if you use : single quot '' all of the str will be considered as a single element 
    #basic methode
str_list += nbr_list    
print(str_list)
    #using the extend methode
str_list.extend(nbr_list)
print(str_list)
#inserte an elemets in a given position in te list :
nbr_list.insert(0 , '0') # the first position is the index and second is the element 
print(nbr_list)

# the pop methode gets the first elemnt and delets it from the list  

#delete a list
del str_list
#delete an element and its position 
nbr_list.remove('2') #from the accual item
del nbr_list[2] # from the position
#get the nbr of elemenst / lengh of a list 
print(len(nbr_list))

# clear elemnts of a list 
nums =[1,2,3,4,56,78 ]
nums.clear()

#sort methode 
nbr_list.sort()
print(nbr_list)
# inverse methode 
nbr_list.sort(reverse=True)
print(nbr_list)




#sets : is list but with no duplicats ; 
# define :
num_set = {1, 3, 2}
numbers = { 1, 1, True, False, 0 , 2}
print(num_set)   # the input will be in order
print(numbers)  #note ; true is a duplicate of 1 , and false is a duplicate of 0
print(type(numbers))
print(len(num_set))
print(len(numbers))
#methodes :sets have the same methodes as lists


# tuples data cant be modified 
tupl = tuple((1 , 2 , 3)) # this called paking a tuple unpaking is expalained below
tuple1 = ("hello" , 22 , True)

print(type(tupl))
print(isinstance(tuple1 , tuple))

# add an element to the tuple 

tubl_list = list(tupl)
tubl_list.append('dave')
tubl_list.extend(['heelo', True]) # the extend method used to add a list not elemenst 
tupl = tuple(tubl_list)

print(tupl)

#   all the operation of lists can be used on tuple with the same methode 

# unpacking a tuple into a variable is done like this 

(var1 , var2 , *var3 ) = tupl # var1 will have the first data of the tuple var2 will ahve the second date var3 will have all of the reamining 

print(var1)
print(var2)
print(var3)
print(tupl)

# count the occurences of a certain elemets
print(tupl.count(2))  #one  argument is needed
                       # it will count teh occurences of a given elemnt




# dictionaries :are simular to lists and sets , but instead of and index it has a key for each elemet 
#so a dict has a key and a value 

##creating a dic 
#direct methode
music = {
    "lyrics": "by dave",
    "instrumenst": "by ellys",
    "edit": "by person"
}
print(music)
#the instructor methode
band = dict(guitar="jake" , violon="ellys")
print(band)

##acces items (both methodes need the key to access the item/value/elemnt)
#direct methode
print(band["guitar"])

#the get methode
print(band.get("guitar")) 

##gett all keys
print(band.keys())

## get all items
print(band.items)

##list the keys and values in form of tuple pairs

print(band.items())

## verifie the existance of keys or item 
#keys
print("guitar" in band)
print("pino" in band)
#items
print("jake" in band) # becausse this methode is for keys
#there is no function to do that i guess / sp it can be done by a loop wich will be coverde later

## change or add value
# direct methode only to change 
band["guitar"] = "alex"
print(band)
# the update methode : add and change value
band.update({"guitar": "alexener" , "pino": "brads" })
print(band)

##remove or delete items/dict
# the pop methode 
print(band.pop("violon")) # need an arguemnt
print(band.popitem()) # need 0 argument to work # pop the last elemnt of dict
print(band)

band.update({"violon": "ellys"})
band["pino"] = "moh"
print(band)

#the del methode 

del band["pino"]
print(band) 
del music              
#print(music) #this give an error message because music doesnt exist
band.update({"violon": "ellys"})

# emtiying a dict 
music = dict(lyric="none" , instru="jaz")
print(music)
music.clear()
print(music)

# copy a dect and creating a reference 
# refence methode
band2 = band # when a change is applyed on band2 this vhange will also apply to band because both band and band2 refer to the same place in the memorie
band2.pop("violon")
print(band)
band["piano"] = "ellys"
del band2
# creat a copy using the copy methode
 
band2 = band.copy()

band2.clear()
print(band)
print(band2)
del band2
#creat acopy using teh constructor methode 
band2 = dict(band)
band2.update({'piano': 'juba'})

print(band)
print(band2)


## nested dect 
del band
member1 = {
    "name": "ellys",
    "instrument": "piano" 
}

member2 = {
    "name": "dave",
    "instrument": "drums"
}

the_band = {
    "fist": member1,
    "second": member2
}

print(the_band)
print(the_band["fist"]["name"])


## addition operations 
# update can be used whith set dic tuples and lists
    
tuple1 = tuple((6,45,33))
dict1 = {
    'ell': "d"
}
ste = set((1,2,3))
ste.update(tuple1)
ste.update(dict1) # would only add the keys
print(ste)

# merge 2 set to creat new set
set1 = set((1,2,3))
set2 = {4, 3 ,6}

set3 = set1.union(set2)
print(set3)
# keep the duplictes from set1 and set2
set4 = set1.intersection(set2)
print(set4)
# or without creating another set
set1.intersection_update(set2)
print(set1)

# keep everythin exept the duplicates
one = {1 , 2  ,3}
set2.symmetric_difference_update(one)
print(set2)
