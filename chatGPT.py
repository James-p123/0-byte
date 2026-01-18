import openai
import os
from dotenv import load_dotenv
load_dotenv()
 
openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = "你的问题"
response = openai.Completion.create(
        engine="text-davinci-003", # 慢，模型大、能力强
        # engine="text-curie-001", # 较快
        # engine="text-babbage-001",
        # engine="text-ada-001", # 最快
        prompt=prompt,
        max_tokens=1024, # 编码长度
        n=1, # 候选答案数量
        temperature=1,
    )
for answer in response["choices"]:
    print(answer["text"])