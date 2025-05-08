import pickle 
#emp={'empl':120,'name':'tarun','age':17}
f=open('employee.dat','wb')
pickle.load(f)
print("successfully added")
f.close()