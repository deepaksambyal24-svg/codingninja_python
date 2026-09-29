import pandas as pd

data = {
    "user_id": [1, 2, 3, 4, 5],
    "mail": [
        "john.doe@codingninjas.com",
        "_jane_doe@codingninjas.com",
        "valid.email@codingninjas.com",
        "invalid-email@otherdomain.com",
        "123start@codingninjas.com"
    ]
}

users = pd.DataFrame(data)
domain= '@codingninjas.com'
# Write your code from here
# for user_id,email in users.iterrows():
        # if email[0].isalpha() and email[email.index('@'):]==domain:
        #     print(user_id,email)
for index, row in users.iterrows():zw
    print(row['user_id'], row['mail'])
