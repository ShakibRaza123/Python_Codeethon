# initializing list 
a = ['Raj','Pankaj','Shreyas'] 

# initializing remove list 
b = ['Sandeep','Vikas','Raj'] 

# printing original list 
print ("The original list is A : " + str(a)) 

# printing remove list 
print ("The original list is B: " + str(b)) 

# using remove() to perform task 
# handled exceptions. 
for i in b: 
	try: 
		a.remove(i) 
	except ValueError: 
		pass

# printing result 
print ("The list after performing remove operation is : " + str(a)) 
