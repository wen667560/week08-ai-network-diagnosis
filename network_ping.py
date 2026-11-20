import subprocess
def check_ping(domain):
    print("=" * 50)
    print("网络 Ping 连通性检测")
    print("=" * 50)
    print(f"正在检测：{domain}")
    try:
        result = subprocess.run(    ##subprocess.run()调用系统命令
            ["ping", "-n", "4", "-w", "2000", domain],  #ping -n 4:发送4次ping请求，-w 2000:每次等待响应最多2000毫秒
            capture_output=True, #获取命令输出
            text=True,
            encoding="gbk",
            errors="replace",
            timeout=12
        )
        output = result.stdout
        print(output)
        success = result.returncode == 0     ##returncode:查看命令执行状态
        if success:
            print("Ping 检测成功")
        else:
            print("Ping 检测失败或没有收到响应")

        return {
            "domain": domain,
            "success": success,
            "output": output
        }

    except subprocess.TimeoutExpired:
        print("检测超时")

        return {
            "domain": domain,
            "success": False,
            "output": "Ping 检测超时"
        }

    except Exception as error:
        print(f"发生错误：{error}")

        return {
            "domain": domain,
            "success": False,
            "output": str(error)
        }


if __name__ == "__main__":
    website = input("请输入检测域名：").strip()

    if website:
        check_ping(website)