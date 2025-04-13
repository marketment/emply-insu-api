from fastapi import FastAPI, Query
import httpx

app = FastAPI()

@app.get("/insurance")
def get_insurance_data(
    opaBoheomFg: str = Query(..., description="1: 산재, 2: 고용"),
    v_saeopjaDrno: str = Query(None, description="사업자등록번호")
):
    base_url = "https://apis.data.go.kr/B490001/gySjbPstateInfoService/getGySjBoheomBsshItem"
    service_key = "iKOpfM3zIpKL5tQ%2FSHLRwuSj4Odbz2JaoWdkLiNdNSKr6jD3wo%2FsUJ%2F3%2BjdWEmvDLbNUZs8kY6QNzdhZs%2BeE%2Fw%3D%3D"

    params = {
        "serviceKey": service_key,
        "opaBoheomFg": opaBoheomFg,
        "numOfRows": 3,
        "pageNo": 1
    }

    if v_saeopjaDrno:
        params["v_saeopjaDrno"] = v_saeopjaDrno

    try:
        # httpx로 SSL 우회
        with httpx.Client(verify=False, timeout=10.0) as client:
            response = client.get(base_url, params=params)
        response.raise_for_status()
        return response.text
    except Exception as e:
        return {"error": str(e), "message": "공공데이터포털 요청 중 문제가 발생했습니다."}


