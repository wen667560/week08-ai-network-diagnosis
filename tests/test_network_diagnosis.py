import socket
import subprocess
from network_diagnosis import check_dns,check_ping,check_port


def test_dns_success(monkeypatch):

    def fake_gethostbyname(domain):
        return "93.184.216.34"

    monkeypatch.setattr(
        "network_diagnosis.socket.gethostbyname",
        fake_gethostbyname
    )

    result = check_dns("example.com")

    assert result["success"] is True
    assert result["ip"] == "93.184.216.34"


def test_dns_failure(monkeypatch):

    def fake_gethostbyname(domain):
        raise socket.gaierror("DNS 查询失败")

    monkeypatch.setattr(
        "network_diagnosis.socket.gethostbyname",
        fake_gethostbyname
    )

    result = check_dns("invalid.example")

    assert result["success"] is False
    assert result["ip"] is None







    from network_diagnosis import check_ping


def test_ping_success(monkeypatch):

    class FakeResult:
        returncode = 0
        stdout = "Ping 检测成功"

    def fake_run(*args, **kwargs):
        return FakeResult()

    monkeypatch.setattr(
        "network_diagnosis.subprocess.run",
        fake_run
    )

    result = check_ping("example.com")

    assert result["success"] is True
    assert "成功" in result["output"]


def test_ping_failure(monkeypatch):

    class FakeResult:
        returncode = 1
        stdout = "请求超时"

    def fake_run(*args, **kwargs):
        return FakeResult()

    monkeypatch.setattr(
        "network_diagnosis.subprocess.run",
        fake_run
    )

    result = check_ping("example.com")

    assert result["success"] is False



    from network_diagnosis import check_port


def test_port_success(monkeypatch):

    class FakeConnection:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            return False

    def fake_create_connection(address, timeout):
        return FakeConnection()

    monkeypatch.setattr(
        "network_diagnosis.socket.create_connection",
        fake_create_connection
    )

    result = check_port("example.com", 443)

    assert result["success"] is True


def test_port_failure(monkeypatch):

    def fake_create_connection(address, timeout):
        raise OSError("连接失败")

    monkeypatch.setattr(
        "network_diagnosis.socket.create_connection",
        fake_create_connection
    )

    result = check_port("example.com", 443)

    assert result["success"] is False