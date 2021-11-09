import requests
# from requests.cookies import RequestsCookieJar
import re
import json


# Set User Info
userName = ''
userPasswd = ''

loginUrl = 'https://www.heavens-above.com/login.aspx?lat=0&lng=0&loc=Unspecified&alt=0&tz=UCT'

# Gen session
mySession = requests.Session()
page = mySession.get(url=loginUrl)

# Get values for login from session.get page
pageViewstate = re.findall(r'id="__VIEWSTATE" value="(.*)" />', page.text)
pageViewstategenerator = re.findall(r'id="__VIEWSTATEGENERATOR" value="(.*)" />', page.text)

# Gen login payload
loginPayload = {
    '__LASTFOCUS':'',
    '__EVENTTARGET':'',
    '__EVENTARGUMENT':'',
    '__VIEWSTATE': pageViewstate[0],
    '__VIEWSTATEGENERATOR': pageViewstategenerator[0],
    'utcOffset':0,
    'ctl00$ddlCulture':'zh',
    'ctl00$cph1$Login1$UserName': userName,
    'ctl00$cph1$Login1$Password': userPasswd,
    'ctl00$cph1$Login1$RememberMe':'on',
    'ctl00$cph1$Login1$LoginButton': '登录',
}

# # Session login and check 
loginPage = mySession.post(url=loginUrl, data=json.dumps(loginPayload))
if loginPage.status_code != 200:
    print(f'[Warn]: Login failed. Please check. HTTP Code: {loginPage.status_code}')
else:
    print('[INFO]: Send user login request succeed.')

# Save Cookies in json format
# with open('cookies', 'w+') as cookiesFile:
#     cookiesFile.write(json.dumps(mySession.cookies.get_dict()))

# Load Cookies to dict
# dictCookies = {}
# with open('cookies', 'r') as cookiesFile:
#     dictCookies = json.loads(cookiesFile.read())
