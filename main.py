from model_factory import get_chatgpt_lmm  # 我们用多模态模型来演示
from prompt_config import PromptConfig
import time

def main():
    """主执行函数"""
   

    # 1. 从配置中获取提示词
    system_prompt = PromptConfig.BT_to_FSM_PROMPT
    print("提示词已加载。")

    # 2. 从模型工厂获取模型实例
    # 注意：这里我们使用 get_chatgpt_lmm() 
    llm1 = get_chatgpt_lmm()
    print("LLM已初始化。")

    # 3. 准备用户输入
    user_message_content = "要求：直接输出结果。"

    # 4. 构建消息列表
    messages = [
        ("system", system_prompt),
        ("user", user_message_content)
    ]
    start_time = time.time()
    # 5. 调用模型
    print("正在调用模型进行分析...")
    try:
        response = llm1.invoke(messages)

        end_time = time.time()
        total_time = round(end_time - start_time, 3)

        print(f"服务器处理耗时：{total_time}秒")
        # 6. 处理模型输出
        print("\n--- 模型原始输出 ---")
        
        print(response.content)
        #result_data = json.loads(response.content)
        #sentiment = result_data.get("imgs_aspect_sentiment", "未能分析")

        #print("\n--- 分析结果 ---")

    except Exception as e:
        print(f"执行过程中发生错误: {e}")

    print("\n--- 任务执行完毕 ---")


if __name__ == "__main__":
    # 当这个脚本被直接运行时，才执行 main() 函数
    # 这使得该文件既可以被直接运行，也可以被其他脚本导入而不执行代码
    main()
