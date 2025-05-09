import pandas as pd
# df = pd.read_csv("data/2.2,2.3_train_cannot_answer_50_turn_last.csv")
df = pd.read_csv("data/2.2,2.3_train_cannot_answer_70_turn_last_edit.csv")
count = 0
countNotAns = 0
remain = []
for index in range(0, len(df)):
    if pd.isnull(df["ans"][index]):
        countNotAns += 1
        remain.append(df.iloc[index])
    elif df["ans"][index] == "[]":
        countNotAns += 1
        remain.append(df.iloc[index])
    else:
        ans = df["ans"][index].replace("[", "").replace("]", "").replace("'", "").replace(",", "").split(" ")
        for txt in ans:
            # print(txt)
            if txt == df["target"][index]:
                count += 1
                break

print("Không trả lời được:", countNotAns)
print("Số câu đúng: ", count)
print("Số câu không đúng: ", len(df) - countNotAns - count)
print("Total: ", len(df))
print("Accuracy: ", count/ len(df))

print("Remain length: ", len(remain))
remain = pd.DataFrame(remain)
remain_df = remain.drop(columns=["ans"])
remain_df.to_csv('./data/2.2,2.3_train_cannot_answer_70_after_last_edit.csv', index = False)