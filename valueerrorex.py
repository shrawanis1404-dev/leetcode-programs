try:
   print(x)
except NameError:
   print("value x is not defined")
except:
   print("something else went wrong")