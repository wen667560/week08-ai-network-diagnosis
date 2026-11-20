import re

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from network_diagnosis import diagnose
from ai_analyzer import analyze_network


app = FastAPI(
    title="AI 网络故障诊断助手",
    description="使用 Python 网络检测和大模型进行网络故障分析",
    version="1.0.0"
)


class DiagnosisRequest(BaseModel):

    domain: str = Field(
        min_length=3,
        max_length=253,
        description="需要诊断的网站域名"
    )

    use_ai: bool = True


def validate_domain(domain):

    pattern = (
        r"^(?=.{1,253}$)"
        r"(?:[a-zA-Z0-9]"
        r"(?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+"
        r"[a-zA-Z]{2,63}$"
    )

    return re.fullmatch(pattern, domain) is not None


@app.get("/")
def home():

    return {
        "message": "AI 网络故障诊断助手运行正常"
    }


@app.get("/health")
def health():

    return {
        "status": "ok"
    }


@app.post("/diagnose")
def diagnose_api(request: DiagnosisRequest):

    domain = request.domain.strip()

    if not validate_domain(domain):

        raise HTTPException(
            status_code=400,
            detail="请输入有效的网站域名"
        )

    result = diagnose(domain)

    if result is None:

        raise HTTPException(
            status_code=422,
            detail="DNS 解析失败，无法继续诊断"
        )

    answer = None

    if request.use_ai:

        answer = analyze_network(result)

    return {
        "success": True,
        "network_result": result,
        "ai_analysis": answer
    }