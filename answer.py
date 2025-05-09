import os
import pickle
import time
import json
import clingo
from clingo.control import Control
from clingo.symbol import parse_term
import pandas as pd
from asp_rules.rules import rules

from tqdm import tqdm
df = pd.read_csv("data/2.2,2.3_train_5k.csv")
# df = pd.read_csv("data/2.2,2.3_train_cannot_answer_70_after_last.csv")

df["ans"] = ""

for index, row in tqdm(df.iterrows()):
    row["query"] = row["query"].replace(" ", "").replace("'", '"')
    row["parse"] = str(row["parse"])
    row["parse"] = row["parse"].replace("),",").")
    row["parse"] = row["parse"].replace("-","_")
    res = rules + row["parse"]
    try:
        ctl = clingo.Control()
        ctl.add("base", [], res)
        ctl.ground([("base", [])])
        for model in ctl.solve(yield_=True):
            model = str(model)
        text = model.split(" ")
        ans = []
        for txt in text:
            if row["query"] in txt:
                tmp = txt.split("(")[0]
                tmp = tmp.replace("_", "-")
                ans.append(tmp)
    except:
        ans = ""
    # add ans to the ans column
    df.at[index, "ans"] = ans

df.to_csv("data/2.2,2.3_train_cannot_answer_70_turn_last_edit.csv", index=False)

