from openai import OpenAI
import os
import pandas as pd
from tqdm import tqdm
from dotenv import load_dotenv
from utils.store import semantic_prompt
from utils.store import gen_rule_prompt

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY_parse')
client = OpenAI()

query = ""
def GPT_generate_content(text, prompt=semantic_prompt):
  response = client.chat.completions.create(
  # model="gpt-4",
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": prompt},
    {"role": "user", "content": text}
  ],
  max_tokens = 4096
  )
  print(response.usage.prompt_tokens)
  return response.choices[0].message.content

df = pd.read_csv('./data/data_test.csv')
# df["parse"] = ""
df["parse"] = ""

for index in tqdm(range(104, len(df))):
  res = GPT_generate_content(df["story"][index])
  print(res)
  df.at[index, "parse"] = res
  df.to_csv("./data/data_test_parse.csv", index=False)

# content = """Story: [April] and her son [John] went to the zoo and then out to dinner yesterday. [Carolina] loved to care for her newborn child [Adrian]. [Luella]'s brother [Adrian] and her went to get ice cream. [April] is teaching her niece, [Luella] how to bake a homemade apple pie. [Carolina] is married to Thomas and when she was 24, the couple welcomed [Luella] into the world.
# Query: ('Eric', 'Marlene'),
# Semantic Parse: son("Eric", "Michael"). father("Michael", "Eric"). wife("Michael", "Marlene"). husband("Marlene", "Michael"). son("Eric", "Arthur"). father("Arthur", "Eric"). brother("Arthur", "Michael")."""

# print(GPT_generate_content(content, gen_rule_prompt))


