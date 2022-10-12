print("集成Fofa,Shodan,Hunter,Censys,零零信安")
print("键入数字进行转换:")
print("1 网页title")
print("2 网页body")
print("3 所在国家")
print("4 ip或ip段")
print("5 端口")
print("6 域名domain")
print("7 Header头")
number = input("请输入:")
if int(number) == 1:
    #title
    Title = input("请输入标题:")
    print(f"Fofa: title=\"{Title}\"\nShodan: title:{Title}\nHunter web.title=\"{Title}\" \n Censys: services.http.response.html_title:{Title} \n 0.zone: title==\"{Title}\"")
if int(number) == 2:
    #body
    Body = input("请输入主体:")
    print(f"Fofa: body=\"{Body}\" \nShodan: http.html:\"{Body}\" \n Hunter: web.body=\"{Body}\"\n Censys: services.http.response.body:{Body} \n 0.zone: html_banner=={Body}")
if int(number) == 3:
    #Country
    Country = input("请输入国家(英文):")
    print(f"Fofa: country=\"{Country}\"\n Shodan: country:{Country}\nHunter: ip.country=\"{Country}\"\n Censys: location.country_code:{Country}\n0.zone: country=={Country}")
if int(number) == 4:
    #ip
    ip = input("请输入ip:")
    print(f"Fofa: ip=\"{ip}\"\nShodan: net:{ip}\nHunter: ip=\"{ip}\" \nCensys: ip: {ip}\n0.zeon: ip=={ip} ")
if int(number) == 5:
    #port
    port = input("请输入端口")
    print(f"Fofa: port=\"{port}\" \nShodan: port:{port} \nHunter: ip.port=\"{port}\" \nCensys: services.port:{port}  \n0.zeon: port=={port}")
if int(number) == 6 :
    #domain
    domain = input("请输入域")
    print(f"Fofa: domain=\"{domain}\" \nShodan: hostname:{domain} \nHunter: domain=\"{domain}\" \nCensys: 俺不会 \n0.zeon: is_ip_domain=={domain}")
if int(number) == 7:
    #port
    HeaderSearch = input("请输入Header")
    print(f"Fofa: header=\"{HeaderSearch}\" \nShodan: 不会 \nHunter: header=\"{HeaderSearch}\" \nCensys: 俺不会 \n0.zeon: 不提供此功能")
# 框架
# if int(number) == 数字:
#     #port
#     port = input("请输入")
#     print(f"Fofa: \nShodan: \nHunter: \nCensys: \n0.zeon:")