class Json:

    import requests
    import json
    from bs4 import BeautifulSoup

    def isAbleJson(self, shop_api_name, app_key): 
        for k in range(129944, 129945):
            requestData = Json.requests.get(f"https://{shop_api_name}.cafe24api.com/api/v2/products/{k}?shop_no=1&cafe24_app_key={app_key}")
            if requestData.status_code == 200:
                Json.jsonParsing(requestData)
   
    def jsonParsing(requestData):         
        
        jsonData = requestData.json()
        print(jsonData)

        json_html_list = ['description']
        print('=' * 170)
        for i in jsonData['product'].keys():
            if i in json_html_list:
                k = jsonData['product'].get(i)
                #print(k)

                header = {'User-Agent': 'Chrome/66.0.3359.181'}
                response = Json.requests.get('https://66girls.co.kr//product/detail.html?product_no=129944', headers=header)
                soup = Json.BeautifulSoup(response.text, 'html.parser')
                # 필수 정보 추출 (이미지, 상품명, 가격, 사이즈)
                frame = soup.select_one('html body .xans-element-.xans-product.xans-product-detail')
                # 사이트내 여러 선택사항
                #print(frame)

                select_list=[]
                
                for sel in frame.find_all('select'):
                    select_list.append(sel)

                # 사이트 선택사항 갯수
                max = len(select_list)
                option_list = []
                
                # 선택사항마다의 옵션 추출
                for v in range(0, max):                
                    for op in select_list[v].find_all('option'):
                        option_list.append([op.text])
                
                print(str(option_list))            

p = Json()
p.isAbleJson("mall66", "f7kOrfNK8UAn2Z93owrB4C")