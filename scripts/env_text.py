import pandas as pd

# check environment
for l in "alphabet":
   print(l)

# read a data file
d = pd.read_cv("../../data_store/data/student_data.csv")

# deadline stuff here
print("Working hard!")

# existing code on main
for i, r in d.iterrows():
    print(r['column'])

print(d.info())

# adding something on merge_test branch
print("Hello branch")


# resolve merge conflict
print("Now we're done!")

