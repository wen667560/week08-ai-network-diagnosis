# AI Network Diagnosis Assistant

基于 Python 和大语言模型的网络故障诊断助手。

## 项目简介

本项目通过 Python 实现基础网络检测，
并调用大语言模型分析网络检测结果。

## 技术栈

- Python 3.12
- Socket
- Subprocess
- OpenAI SDK
- SiliconFlow API
- Qwen3-8B

## 功能

1. DNS 域名解析
2. Ping 网络连通性检测
3. TCP 端口连接检测
4. 综合网络诊断
5. AI 故障分析
6. 多工具工作流

## 安装

```bash
pip install -r requirements.txt
```

## API 配置

配置环境变量：

SILICONFLOW_API_KEY

不要将 API Key 上传到 GitHub。

## 运行

```bash
python network_agent.py
```

## 项目说明

这是一个学习型网络诊断项目，
用于了解 Python 网络编程和 AI 工具调用流程。