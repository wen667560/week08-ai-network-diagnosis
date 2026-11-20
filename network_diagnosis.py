from logger_config import logger
import socket
import subprocess
def check_dns(domain):
    try:
        ip = socket.gethostbyname(domain)
        return {
            "success": True,
            "ip": ip,
            "error": None
        }
    except socket.gaierror as error:
        return {
            "success": False,
            "ip": None,
            "error": str(error)
        }


def check_ping(domain):
    try:
        result = subprocess.run(
            ["ping", "-n", "4", "-w", "2000", domain],
            capture_output=True,
            text=True,
            encoding="gbk",
            errors="replace",
            timeout=12
        )
        return {
            "success": result.returncode == 0,
            "output": result.stdout
        }
    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "output": "Ping 检测超时"
        }


def check_port(host, port):
    try:
        with socket.create_connection(
            (host, port),
            timeout=3
        ):
            return {
                "success": True,
                "error": None
            }
    except OSError as error:
        return {
            "success": False,
            "error": str(error)
        }


def diagnose(domain):
    logger.info(f"开始检测域名：{domain}")
    print("\n开始网络综合诊断")
    dns_result = check_dns(domain)
    print("\n1. DNS 检测")
    if not dns_result["success"]:
        print("DNS 解析失败")
        logger.error(f"DNS解析失败:{domain}")
        return
    ip = dns_result["ip"]
    print(f"DNS 解析成功：{ip}")
    logger.info(f"DNS解析成功:{ip}")
    print("\n2. Ping 检测")
    ping_result = check_ping(domain)
    if ping_result["success"]:
        print("Ping 检测成功")
    else:
        print("Ping 未收到成功响应")
    logger.info(f"域名检测结束:{domain}")
    print("\n3. TCP 端口检测")
    port_result = check_port(domain, 443)
    if port_result["success"]:
        print("443 端口连接成功")
    else:
        print(f"443 端口连接失败：{port_result['error']}")

    return {
        "domain": domain,
        "ip": ip,
        "dns": dns_result,
        "ping": ping_result,
        "port_443": port_result
    }


if __name__ == "__main__":
    website = input("请输入需要诊断的网站：").strip()
    if website:
        result = diagnose(website)
        print("\n综合诊断结束")