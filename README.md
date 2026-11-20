
# AI 网络故障诊断助手

## 一、项目介绍

本项目使用 Python 开发，结合网络检测工具和大语言模型 API，实现自动化网络故障诊断。

程序通过 DNS 解析、Ping 连通性检测和 TCP 端口检测获取网络状态，再将检测结果传递给大语言模型进行分析，生成故障排查建议。

## 二、项目功能

1. DNS 域名解析
2. Ping 网络连通性检测
3. TCP 端口连接检测
4. 网络综合诊断
5. 大模型故障分析
6. Agent 自动化工作流
7. FastAPI 接口服务
8. Pytest 自动化测试
9. 日志记录

## 三、使用技术

- Python 3.12
- Socket
- Subprocess
- OpenAI SDK
- SiliconFlow API
- Qwen3-8B
- FastAPI
- Uvicorn
- Pytest

## 四、项目目录

```text
week08/
├── tests/
│   └── test_network_diagnosis.py
├── logs/
├── screenshots/
├── network_dns.py
├── network_ping.py
├── network_port.py
├── network_diagnosis.py
├── ai_analyzer.py
├── network_agent.py
├── api.py
├── logger_config.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 五、安装依赖

在项目目录下运行：

```bash
pip install -r requirements.txt
```

## 六、配置大模型 API

项目使用 SiliconFlow API。

需要在电脑系统环境变量中配置：

```text
SILICONFLOW_API_KEY
```

不要将真实 API Key 写进 Python 源代码。

不要将 API Key 上传到 GitHub。

## 七、运行终端程序

在项目目录下运行：

```bash
python network_agent.py
```

输入需要检测的域名，即可进行网络诊断。

输入 q 可以退出。

## 八、运行 API 服务

执行：

```bash
python -m uvicorn api:app --reload
```

浏览器打开：

```text
http://127.0.0.1:8000/docs
```

可以查看和测试 API 接口。

## 九、运行自动化测试

执行：

```bash
python -m pytest tests -v
```

## 十、项目限制

1. 部分网站可能限制 ICMP 请求，因此 Ping 失败不一定表示网站无法访问。
2. TCP 端口连接成功不代表网站的所有业务功能都正常。
3. AI 分析结果依赖实际采集到的网络检测数据。
4. 当前 API 主要用于本地学习和测试。

## 十一、后续改进方向

1. 增加更多网络检测功能。
2. 优化异常处理。
3. 增加接口身份验证。
4. 增加接口请求频率限制。
5. 提高自动化测试覆盖率。
6. 开发可视化操作界面。