import os
from openai import OpenAI
def analyze_network(result):
    api_key = os.getenv("SILICONFLOW_API_KEY")
    if not api_key:
        print("没有检测到 SILICONFLOW_API_KEY")
        return None

    client = OpenAI(
        api_key=api_key,
        base_url="https://api.siliconflow.cn/v1"
    )
    prompt = f"""
你是一名网络故障分析助手。
下面是程序检测到的网络信息：
{result}
请完成以下任务：
1. 总结网络检测结果。
2. 分析可能存在的问题。
3. 区分确定的检测结果和推测。
4. 给出具体排查建议。
5. 不要编造检测数据。
请使用中文回答。
"""
    response = client.chat.completions.create(
        model="Qwen/Qwen3-8B",
        messages=[
            {
                "role": "system",
                "content": "你是一名专业的网络故障诊断助手。"
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )
    answer = response.choices[0].message.content
    print("\n========== AI 故障分析 ==========")
    print(answer)
    return answer

if __name__ == "__main__":
    test_result = {
        "domain": "www.example.com",
        "dns": "成功",
        "ping": "失败",
        "port_443": "成功"
    }
    analyze_network(test_result)