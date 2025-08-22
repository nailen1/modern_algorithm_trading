# HEADER

content-type: application/json; charset=utf-8
authorization: Bearer {access_token}
appkey: {발급받은 앱키}
appsecret: {발급받은 앱시크릿}
tr_id: TTTS3012R (실전투자) or VTTS3012R (모의투자)

# QUERY PARAMETER

CANO: 계좌번호 앞 8자리
ACNT_PRDT_CD: 계좌상품코드 뒤 2자리
OVRS_EXCG_CD: 거래소코드(예: NASD, NYSE, AMEX, SEHK 등)
TR_CRCY_CD: 거래통화코드(예: USD, HKD, CNY, JPY, VND)
CTX_AREA_FK200: 연속조회검색조건(최초 조회시 공백)
CTX_AREA_NK200: 연속조회키(최초 조회시 공백)

# API GUIDE URL

https://apiportal.koreainvestment.com/apiservice/apiservice-oversea-stock-order#L_0482dfb1-154c-476c-8a3b-6fc1da498dbf
