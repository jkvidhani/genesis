import pandas as pd
data = pd.read_csv("train.csv")
df = pd.DataFrame(data)

#1
srv_rate_gen = df.groupby("Sex")["Survived"].mean()    # print(srv_rate_gen)

#2
avg_fare_pclass = df.groupby("Pclass")["Fare"].mean()  # print(avg_fare_pclass)

#3
# high_srv_rate = df.groupby("Pclass")["Survived"].mean()
#OR
high_srv_rate = df.groupby("Pclass")["Survived"].mean().idxmax()
# print(high_srv_rate.max())

#4
avg_age_srv = df.groupby("Survived")["Age"].mean()     # print(avg_age_srv)

#5
pass_emb = df["Embarked"].value_counts()               # print(pass_emb)

#6
exp_tickets = df.sort_values("Fare", ascending=False)  # print(exp_tickets)

#7
pct = df.groupby("Sex")["Survived"].mean() * 100       # print(pct)