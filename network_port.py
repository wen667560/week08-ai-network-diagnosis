import socket


def check_port(host, port, timeout=3):
    print("=" * 50)
    print("TCP 端口检测")
    print("=" * 50)

    print(f"目标地址：{host}")
    print(f"目标端口：{port}")

    try:
        with socket.create_connection(
            (host, port),
            timeout=timeout
        ):
            print("TCP 连接成功")

            return {
                "host": host,
                "port": port,
                "success": True,
                "error": None
            }

    except socket.timeout:
        print("连接超时")

        return {
            "host": host,
            "port": port,
            "success": False,
            "error": "连接超时"
        }

    except OSError as error:
        print(f"连接失败：{error}")

        return {
            "host": host,
            "port": port,
            "success": False,
            "error": str(error)
        }


if __name__ == "__main__":
    host = input("请输入目标域名：").strip()

    if not host:
        print("域名不能为空！")
    else:
        check_port(host, 443)
        check_port(host, 3306)