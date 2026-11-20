import socket  #网络通信模板

def check_dns(domain):
    print("=" * 50)
    print("Python DNS 域名解析检测")
    print("=" * 50)

    print(f"正在检测域名：{domain}")

    try:
        ip_address = socket.gethostbyname(domain) #获取域名对应的IPv4地址

        print("DNS 解析成功！")
        print(f"域名：{domain}")
        print(f"IP 地址：{ip_address}")

    except socket.gaierror as error:
        print("DNS 解析失败！")
        print(f"错误信息：{error}")


if __name__ == "__main__":
    website = input("请输入需要检测的网站域名：").strip()

    if website:
        check_dns(website)
    else:
        print("域名不能为空！")