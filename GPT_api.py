from openai import OpenAI
import os
import pandas as pd
from tqdm import tqdm
from dotenv import load_dotenv
from utils.store import semantic_prompt
from utils.store import gen_rule_prompt

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
client = OpenAI()

query = ""
def GPT_generate_content(text, prompt=semantic_prompt):
  response = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": prompt},
    {"role": "user", "content": text}
  ],
  max_tokens = 4096
  )
  print(response.usage.prompt_tokens)
  return response.choices[0].message.content

# df = pd.read_csv('2.2,2.3 test.csv')
# df["parse"] = ""

# for index in tqdm(range(0, len(df))):
#   res = GPT_generate_content(df["story"][index])
#   print(res)
#   df.at[index, "parse"] = res
# df.to_csv("2.2,2.3 test_ans.csv", index=False)

content = """Story: [Eric] asked his son, [Michael], to go grocery shopping for him. [Michael] was busy and sent his wife, [Marlene], instead. [Eric]'s son [Arthur] is in the hospital. [Arthur]'s brother [Michael] accidentally hit him with a hammer.
Query: ('Eric', 'Marlene'),
Semantic Parse: son("Eric", "Michael"). father("Michael", "Eric"). wife("Michael", "Marlene"). husband("Marlene", "Michael"). son("Eric", "Arthur"). father("Arthur", "Eric"). brother("Arthur", "Michael")."""

print(GPT_generate_content(content, gen_rule_prompt))


