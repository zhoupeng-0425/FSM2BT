#导入 Python 的内置 os 模块
#os 模块提供了与操作系统交互的功能。在这里，我们主要使用它的 os.getenv() 函数来获取环境变量的值
import os
#从一个名为 python-dotenv 的第三方库中导入 load_dotenv 函数
#它会查找一个名为 .env 的文件，并将文件中定义的键值对加载到当前运行环境的环境变量中
from dotenv import load_dotenv
#执行加载操作
load_dotenv(override=True)

ZHIPU_API_KEY="f2a511e97e9f4d8eb61e2fc1c29e0b2a.XsEL9AYu3NEzTEdk"
ZHIPU_BASE_URL="https://open.bigmodel.cn/api/paas/v4"
ChatGPT_API_KEY=""

# ZHIPU_API_KEY = os.getenv('ZHIPU_API_KEY')
# QWEN_API_KEY = os.getenv('QWEN_API_KEY')
# DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')
#
#
# ZHIPU_BASE_URL = os.getenv('ZHIPU_BASE_URL')
# QWEN_BASE_URL = os.getenv('QWEN_BASE_URL')
# DEEPSEEK_BASE_URL = os.getenv('DEEPSEEK_BASE_URL')
