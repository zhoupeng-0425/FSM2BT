# 负责 “提供LLM工具”（模型）
from langchain_openai import ChatOpenAI

from env_utils import ZHIPU_API_KEY, ZHIPU_BASE_URL, ChatGPT_API_KEY
# def get_zhipu_llm():
#     #创建并返回一个用于文本的智谱AI模型实例 (glm-4.5)
#     return ChatOpenAI(
#     model='glm-4.6',
#     api_key=ZHIPU_API_KEY,
#     base_url=ZHIPU_BASE_URL,
#     temperature=0,
#     max_retries=3,
#     request_timeout=180,
#
# )
# def get_zhipu_lmm():
#     #创建并返回一个用于多模态的智谱AI模型实例 (glm-4.5v)
#     return ChatOpenAI(
#     model='glm-4.5v',
#     api_key=ZHIPU_API_KEY,
#     base_url=ZHIPU_BASE_URL,
#     temperature=0,
#     max_retries=3,
#     request_timeout=180,
# )

def get_zhipu_lmm():
    return  ChatOpenAI(
        model='glm-4.6',
        api_key=ZHIPU_API_KEY,
        base_url=ZHIPU_BASE_URL,
        temperature=0,
        max_retries=3,
        request_timeout=180,
    )

def get_chatgpt_lmm():
    return ChatOpenAI(
        model="gpt-4o",               # 或 "gpt-4o-mini"（更便宜、更快）
        api_key=ChatGPT_API_KEY,
        base_url=None,                # 使用默认 OpenAI 端点；如用代理可设为自定义 URL
        temperature=0,
        max_retries=3,              #重试次数
        request_timeout=180,        #请求超时时间（描述）
        top_p=0.95,
    )
##想要稳定输出（比如问答、生成固定格式内容）：temperature=0.1 + top_p=0.9

# llm = ChatOpenAI(
#     model='deepseek-reasoner',
#     api_key=DEEPSEEK_API_KEY,
#     base_url=DEEPSEEK_BASE_URL,
#     temperature=0.1,
#     max_retries=3,
#     request_timeout=180,
# )



