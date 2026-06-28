import playwright
from playwright.sync_api import Playwright
ordersPayLoad = {"orders": [{"country": "India", "productOrderedId": "6960eac0c941646b7a8b3e68"}]}

class APIUtils:
    def getToken(self, playwright: Playwright):
        api_request_createorder = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_createorder.post("/api/ecom/auth/login",data={"userEmail": "abdulsamad453@outlook.com", "userPassword": "!Jun26@honWRV"})
        assert response.ok
        print(response.json())
        login_token = response.json()
        return login_token["token"]



    def createorder(self, playwright: Playwright):
        token = self.getToken(playwright)
        api_request_createorder = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_createorder.post("/api/ecom/order/create-order",data=ordersPayLoad, headers={"Authorization": token})
        print(response.json())
        response_body = response.json()
        order_ID=response_body["orders"][0]
        return order_ID
        
    

