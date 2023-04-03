import requests

# requests.get()
# requests.post()
#####################################
# response = requests.get("https://httpbin.org/get")
# print(response.status_code)
######################################""
# response = requests.get("https://httpbin.org/get")
# print(response.text)
######################################
# params = {
#     "name" : "Mike",
#     "age": 25
# }
# response = requests.get("https://httpbin.org/get", params=params)
# res_json = response.json()
# del res_json['origin']          # to hide my IP address
# print(res_json)
#######################################
# payload = {
#     "name" : "Mike",
#     "age": 25
# }
# response = requests.post("https://httpbin.org/post", data=payload)
# res_json = response.json()
# del res_json['origin']          # to hide my IP address
# print(res_json)
#######################################
# response = requests.get("https://httpbin.org/status/404")
# print(response.status_code)
# #######################################
# response = requests.get("https://httpbin.org/status/404")
# if response.status_code == requests.codes.not_found:
#     print("Not found")
# else:
#     print(response.status_code)
#######################################
# response = requests.get("https://httpbin.org/user-agent")  #user_ agent: an identification that tells the webservice which software yu are using
# print(response.text)
########################################
# problem: websites will block us if they see we are using python requests or will serve us differently
# solution: specify a different user_agent manually while sending the request 
# headers = {
#     "User-Agent": "HelloWorld/1.1"             # or any other user agent
# }
# response = requests.get("https://httpbin.org/user-agent", headers=headers)
# print(response.text)
#########################################
# headers = {
#     "User-Agent": "HelloWorld/1.1"             # or any other user agent
#     "Accept": "image/jpeg"
# }
# response = requests.get("https://httpbin.org/image", headers=headers)
# print(response.text)
###############################
# If response doesnt come or it is late then we may specify a delay of 5 seconds
# response = requests.get("https://httpbin.org/delay/5", timeout=3)   # if reponse is late more than 3 sec then raise a exception and break
# res_json = response.json()
# del res_json['origin']          # to hide my IP address
# print(res_json)
##############################
# proxies = {
#     "http": "139.99.237.62:80",
#     "https": "139.99.237.62:80"
# }
# response = requests.get("https://httpbin.org/get", proxies=proxies) 

# print(response.text)