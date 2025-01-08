import pandas as pd
mobile_time =[2,3,4,5,6]
rest_hours =[5,6,7,8,9]
study_hours =[4,5,6,7,8]
stu_name =["jasmine","charitha","vivek","saketh","teju"]
dict1 = {
    "mobile_time":mobile_time,
    "rest_hours":rest_hours,
    "study_hours":study_hours,
    "stu_name":stu_name
    }
print(dict1)
df = pd.DataFrame(dict1)
print(df)

