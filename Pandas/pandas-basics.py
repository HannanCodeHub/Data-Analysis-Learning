import pandas as pd

data = {
    "Name": ["hannan", "basit", "sohail", "wasif", "ahmed", "burak" , "mohid" , "hamza"],
    "Age": [22,34,44,23,45,33,56,67],
    "City": ["hyderabad", "islammabad", "karachi", "sukkur", "larkana", "mirpurkhas", "lahore", "rawalpindi"],
    "Salary":[90000,85000,45000,33500,99000,56000,77000,90000],
    "Perf: Score" :[90,80,30,20,95,50,70,90]
}



df = pd.DataFrame(data)

df.to_csv("trail.csv",  index=False)

#to excel:
df.to_csv("trail.xlsx",  index=False)

#to json:
df.to_csv("trail.json",  index=False)

#initial 2 values:
print(df.head(2))

#to know about data:
print(df.info())

#descriptive statistics for numerical column:
print(df.describe())

#to know shape and column of data :
print(df)
print (f'Shape :{df.shape}')
print (f'Columns Name :{df.columns}')

#select specific colums filter rows and manipulate data:
print("Sample Data Frame")
print(df)
print("Single column return series:")
name = df['Name']
print(name)

#selecting multiple columns:
subset = df[["Name", "Salary"]]
print ("\n subset with name and salary:")
print(subset)

#rows filter:
high_salary = df[df[("Salary")] > 50000]
print("Employee's Salary Greater than 50,000:")
print(high_salary)

#multiple rows filtering :
filtered = df[(df["Age"]> 30) & (df["Salary"] > 50000)]
print("Employee's Salary > 50,000 and age > 30")
print(filtered)

filtered2 = df[(df["Age"]> 35) | (df["Perf: Score"] > 80)]
print("printing employee's with age > 30 or P.S > 80")
print(filtered2)

#adding column:
df ["Bonus"] = df["Salary"] * 0.1
print(df)

#adding column using insert():
#df.insert(index, column_name , data)
df.insert(0,"EmployeeId", [101,102,103,104,105,106,107,108])
print(df)

#updating values : .loc[row_index, column ]= new value
df.loc[3,"Salary"] = 55000
print(df)

#increasing salary and bonus by 5%:
df[["Salary", "Bonus"]] = df[["Salary", "Bonus"]] * 1.05

print(df)

#removing columns:
print("modified data:")
df.drop(columns = ["Perf: Score"], inplace=True)
print(df)

#handling missing data:

data= {
    "Name": ["hannan", "baqir" , "sohail", "wasif", "ahmed", "burak" , "mohid" , "hamza"],
    "Age": [22,None,44,23,45,33,56,67],
    "City": ["hyderabad", None, "karachi", "sukkur", "larkana", "mirpurkhas", "lahore", "rawalpindi"],
    "Salary":[90000,None,45000,33500,99000,56000,77000,90000],
    "Perf: Score" :[90,None,30,20,95,None,70,90]
}

df = pd.DataFrame(data)
print(df)

print ("new missing values:")

#finding missing data:
print(df.isnull())
print(df.isnull().sum())

#remove missing values:
# df.dropna(inplace = True)
# print(df)

#filling missing values, fillna(value, inplace = true):
# df = df.astype(object)
# df.fillna(0, inplace=True)

print(df)

#fill the null value with some other val relatable:
# df['Age'] = df['Age'].fillna(df['Age'].mean())
# print(df)

# df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
# print(df)

#Interpolation:
df['Age'] = df['Age'].interpolate(methods= 'True')
print("after interpolation:")
print(df)

#Sorting:
df.sort_values(by = "Name" , ascending = True,  inplace = True)
print("sorted by names:")
print(df)

#multiple sorting:
# df.sort_values(by = ["Name" , "Salary"] , ascending = [True, False],  inplace = True)
# print("sorted by names:")
# print(df)

#aggregrate functions:
avg_salary = df["Salary"].mean()
print("avg salary is : ", int(avg_salary))

#grouping:
# grouped = df.groupby('Age')['Salary'].sum()
# print("grouped salary:" , grouped)

#Multiple Grouping:
grouped = df.groupby(['Age' , 'Name'])['Salary'].sum()
print( grouped)

#Merging & Joining:

#customer dataframe:
df_customers = pd.DataFrame({
    'customerID' : [101,102,104,105],
    'customerName': ["basil", "saif", "kohinoor", "imsha"]
})

#order dataframe:
df_orders = pd.DataFrame({
    'customerID' : [101,103,107,105],
    'OrderAmount': [8900,5400,4300,900]
})

print(df_customers)
print(df_orders)

#merge:
# df_merged = pd.merge(df_customers, df_orders , on ='customerID', how = 'inner')
# print("inner join:")
# print(df_merged)

#concatenation (vertically)
df_concat = pd.concat([df_orders, df_customers] , ignore_index = True)
print(df_concat)

# #concatenation (horizontally)
df_concat = pd.concat([df_orders, df_customerName] , axis = 1 , ignore_index = True)
print(df_concat)