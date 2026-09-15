import pandas as pd
# slicing using index lebles
data=[10,20,30,40,50]
s=pd.Series(data,index=["a","b","c","d","e"])
slice_by_levesls=s['b':'d']
print(slice_by_levesls)


# creating serias by two lit value and keys
data=[10,20,30,40]
index=['india','usa','uk','France']
# creating the series
series=pd.Series(data,index=index)
print(series)

print(f'index:{series.index}')
print(f'values:{series.values}')

# return or set the name of the series

series.name='demo'
print('name:')
print(series.name)
print(series.shape)
# attributes
# check whether the series is empty or no t
print(series.empty)  # empty --. is empty string
print(series.hasnans)
print(series.isnull())
print(series.isnull().sum())
print(series.unique())
print(series.ndim)


# methods of series

marks=[86,90,92,89,78]
students=['alice','bob','charlie','david','eva']
student_series=pd.Series(marks,index=students)
print(student_series)

# print ----head
print(student_series.head(1))
print(student_series.tail(1))

# print describe
print(student_series.describe())


# value count __ return a series containing counts of unique values

print(student_series.value_counts())



# sort values
print(student_series.sort_index())

# drop a value
print(student_series.drop('charlie'))  # remove a series it does not change the actual series


# replace ()
print(student_series.replace(85,86))


# not null
#res=student_series.notnull.sum()


# dropping an element with inplece Without inplace:
# ○ The drop method returns a new Series.
# ○ The original Series remains unchanged.
# ● With inplace=True:
# ○ The drop method modifies the original Series directly.
# ○ No new Series is returned.
student_series.drop('charlie',inplace=True)
print(student_series)


# addition of two series

seriesA = pd.Series([1,2,3,4,5], index =['a', 'b', 'c', 'd', 'e'])
print('seriesA:')
print(seriesA)
seriesB = pd.Series([10,20,-10,-50,100],index = ['z', 'y', 'a',
'c', 'e'])
print('seriesB')
print(seriesB)

# Performing addition
result_addition = seriesA + seriesB
print("Addition of seriesA and seriesB:")
print(result_addition)
