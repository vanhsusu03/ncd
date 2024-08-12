import pandas as pd
df = pd.read_csv("data/2.2,2.3_train_5k_ans.csv")
count = 0
countNotAns = 0
for index in range(0, len(df)):
    if pd.isnull(df["ans"][index]):
        countNotAns += 1
    else:
        ans = df["ans"][index].replace("[", "").replace("]", "").replace("'", "").replace(",", "").split(" ")
        for txt in ans:
            print(txt)
            if txt == df["target"][index]:
                count += 1
                break

print(countNotAns)
print(count)
print(len(df) - countNotAns - count)
print(len(df))
print(count/len(df))