import panda as pd # Importing pandas library
import numpy as np # Importing numpy library

# Creating a dataframe
df = pd.DataFrame(np.arange(0,20).reshape(5,4), index=['Row1','Row2','Row3','Row4','Row5'], columns=['Column1','Column2','Column3','Column4'])

# Creating a dataframe from a dictionary
df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4], 'Product Name' : ["t-shirt", "t-shirt" , "skirt" , "skirt" ,] , "Color" : ["blue", "green" , "red", "black"]
  
  # add Product Name and Color here
})

print(df1)

# Creating a dataframe from a list of lists with column names
df2 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  [3, "San Francisco" , 90],
  [4, "Sacramento", 115]
  # Fill in rows 3 and 4
],
  columns=["Store ID" , "Location" , "Number of Employees"

    #add column names here
  ])

print(df2)