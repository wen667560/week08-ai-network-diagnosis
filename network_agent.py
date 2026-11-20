from network_diagnosis import diagnose
from ai_analyzer import analyze_network

def run_agent():
    print("=" * 55)
    print("AI 网络故障诊断助手")
    print("=" * 55)

    while True:
        domain = input(
            "\n请输入需要诊断的域名（输入 q 退出）："
        ).strip()

        if domain.lower() == "q":
            print("诊断助手已退出")
            break

        if not domain:
            print("域名不能为空")
            continue

        print("\n第一步：执行网络检测")

        result = diagnose(domain)

        if not result:
            print("DNS 解析失败，暂时无法继续后续检测")
            continue

        print("\n第二步：调用 AI 分析")

        analyze_network(result)

        print("\n本次诊断结束")


if __name__ == "__main__":
    run_agent()