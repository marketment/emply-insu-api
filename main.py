from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get("/insurance")
def get_insurance_data(
    opaBoheomFg: str = Query(..., description="1: 산재, 2: 고용"),
    v_saeopjaDrno: str = Query(None, description="사업자등록번호")
):
    base_url = "https://apis.data.go.kr/B490001/gySjbPstateInfoService/getGySjBoheomBsshItem"
    service_key = "iKOpfM3zIpKL5tQ/SHLRwuSj4Odbz2JaoWdkLiNdNSKr6jD3wo/sUJ/3+jdWEmvDLbNUZs8kY6QNzdhZs+eE/w=="

    params = {
        "serviceKey": service_key,
        "opaBoheomFg": opaBoheomFg,
        "numOfRows": 3,
        "pageNo": 1
    }

    if v_saeopjaDrno:
        params["v_saeopjaDrno"] = v_saeopjaDrno

    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        return response.text  # XML 그대로 반환 (첫 연결 확인 목적)
    except Exception as e:
        return {"error": str(e), "message": "공공데이터포털 요청 중 문제가 발생했습니다."}
