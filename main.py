# -*- coding: utf-8 -*-
from fastapi import FastAPI
import requests
import xmltodict
import urllib3

# SSL 경고 비활성화 (테스트 환경 한정)
urllib3.disable_warnings()

app = FastAPI()

@app.get("/insurance")
def get_insurance_data(
    opaBoheomFg: str = "2",  # 1: 산재보험, 2: 고용보험
    pageNo: int = 1,
    numOfRows: int = 3,
    v_saeopjaDrno: str = None
):
    serviceKey = "iKOpfM3zIpKL5tQ/SHLRwuSj4Odbz2JaoWdkLiNdNSKr6jD3wo/sUJ/3+jdWEmvDLbNUZs8kY6QNzdhZs+eE/w=="
    base_url = "http://apis.data.go.kr/B490001/gySjbPstateInfoService/getGySjBoheomBsshItem"  # HTTPS → HTTP

    params = {
        "serviceKey": serviceKey,
        "opaBoheomFg": opaBoheomFg,
        "pageNo": pageNo,
        "numOfRows": numOfRows
    }

    if v_saeopjaDrno:
        params["v_saeopjaDrno"] = v_saeopjaDrno

    try:
        response = requests.get(base_url, params=params, verify=False)  # SSL 검증 비활성화
        response.raise_for_status()
        data = xmltodict.parse(response.content)
        return data
    except Exception as e:
        return {
            "error": str(e),
            "message": "공공데이터포털 요청 중 문제가 발생했습니다."
        }