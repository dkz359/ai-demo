import dotenv
from langchain_community.llms import Tongyi
from langchain_core.prompts import PromptTemplate
# from langchain.chains import LLMChain

dotenv.load_dotenv()    # 加载环境变量

template = """问题：{question}

回答：让我们一步一步地思考。"""

prompt = PromptTemplate(template=template, input_variables=["question"])
llm = Tongyi()
# llm_chain = LLMChain(prompt=prompt, llm=llm)
llm_chain = prompt | llm
question = "贾斯汀·比伯出生的那一年，哪支NFL球队赢得了超级碗？"

res = llm_chain.invoke(question)
print(res)