# -*- coding: utf-8 -*-

import chromedriver_binary 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
from bs4 import BeautifulSoup
import json

options = Options()
options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

driver = webdriver.Chrome(chrome_options=options)
driver.get('https://login.microsoftonline.com/53a8b0d9-d900-48cc-9d7e-5935dc8d5b17/oauth2/authorize?client_id=00000003-0000-0ff1-ce00-000000000000&response_mode=form_post&protectedtoken=true&response_type=code%20id_token&resource=00000003-0000-0ff1-ce00-000000000000&scope=openid&nonce=1EFE23B0D93938227B5C6E9DFC78DEF70176B9D1A4EAAC5E-0BCDC9D2D78FA20A7B35EA0E4919B17B6A7416E8A4AC3407BB70EFC378F44538&redirect_uri=https%3A%2F%2Fofficerakuten.sharepoint.com%2F_forms%2Fdefault.aspx&claims=%7B%22id_token%22%3A%7B%22xms_cc%22%3A%7B%22values%22%3A%5B%22CP1%22%5D%7D%7D%7D&wsucxt=1&cobrandid=11bd8083-87e0-41b5-bb78-0bc43c8a8e8a&client-request-id=4dfc7c9f-b017-a000-9dc3-8a882566a48f')

# ID/PASSを入力
id = driver.find_element_by_id("i0116")
id.send_keys("ar-taisei.kato@rakuten.com")
#password = driver.find_element_by_id("パスワード入力フィールドの要素")
#password.send_keys("実際のPASS")

time.sleep(1)

# ログインボタンをクリック
login_button = driver.find_element_by_id("idSIButton9")
login_button.click()

time.sleep(1)

# サイト内で他の画面に遷移させたければ
driver.get('https://rakuten.okta.com/login/default?fromURI=%2Fapp%2Foffice365%2FexkdvyeypYsVHUsZq356%2Fsso%2Fwsfed%2Fpassive%3Fcbcxt%3D%26client-request-id%3D4dfc7c9f-b017-a000-9dc3-8a882566a48f%26lc%3D%26mkt%3D%26wctx%3DLoginOptions%253D3%2526estsredirect%253D2%2526estsrequest%253DrQIIAZ2RP2gTURzH83LJmcSWhiIoTkVSBOWS9-69l_fegeL9xaW2CKK4lPvbXGNz6d0Fqzg5FQftrqKIUyZxkk5CB7GDZM7oVJzEQRwcvCBCx-J3-PKF33f48vldklAbaS34V1iZuQKjCCl-OEvHlC42mq8e_V45-670-uXBk93l6O2zMeC9PB9mWqeTRFHsh6nbH-XhoJ313DQcJvEgb_vJVmc9StKtrBOEkTu6l7fdbLjzAYAJAEcAjMvbyHZsFRvQElhgrqrMoGbXFpZjMm7ZDoOIdQ1hIZ3Yum5SW4GGaZnCUi3GHV2FOjMwtXVoE4GEgZjR1RlBXZvrRDcxgcwwGLQdExd1Qijm0_LCqj7Ke-rMkjR-GP4o12cb14dJlo-lEwF5L7UodrkHA6EEojgS7vuKCFioUIFp4POAeogdSnIyDAdx8FU676ZK7sZZGLf7bp5c-0erQDSpgG-VOVjVarVGc-GcvFT6VQFvqgXz55_9n18uTu0Xy1c_PSUHpcNqx995gLfZLeN6P9hcoZfvkzX3xuaGg8VNusrw7Tsbqd1NVCMxLP0K1dCeDPZkeV-u16Rm6YJkrqEjGXyXwe6p0n79vx84bZxRoVogEYpKlqCqEaoRdndyGkznUKPuJ17qDoI4WGwh5AUccqxwFhaUkEcVz2NcgZ5PsM9dHnL38fyJah_nS38A0%26wa%3Dwsignin1.0%26username%3Dar-taisei.kato%2540rakuten.com%26wtrealm%3Durn%253Afederation%253AMicrosoftOnline&redirectFromAdsso=true')

# ID/PASSを入力
id = driver.find_element_by_id("okta-signin-username")
id.send_keys("ar-taisei.kato@rakuten.com")

time.sleep(1)

password = driver.find_element_by_id("okta-signin-password")
password.send_keys("Tkapple0827a")

time.sleep(1)

# ログインボタンをクリック
login_button = driver.find_element_by_id("okta-signin-submit")
login_button.click()

time.sleep(2)

# サイト内で他の画面に遷移させたければ
driver.get('https://login.microsoftonline.com/login.srf')

time.sleep(3)

# ログインボタンをクリック
login_button = driver.find_element_by_id("idSIButton9")
login_button.click()

time.sleep(1)

# サイト内で他の画面に遷移させたければ
driver.get('https://www.office.com/?auth=2')

time.sleep(1)

driver.get('https://officerakuten.sharepoint.com/sites/GlobalPortal/SitePages/top.aspx?wa=wsignin1.0')

#time.sleep(2)

#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# クリック
#in_button = driver.find_element_by_id("O365_MainLink_NavMenu")
#login_button.click()

#time.sleep(2)

# クリック
#login_button = driver.find_element_by_id("allAppsLink")
#login_button.click()

#time.sleep(2)

# クリック
#login_button = driver.find_element_by_id("O365_AppTile_f5c98d6d-d486-4cf5-b1d6-e08447651a90")
#login_button.click()


url = driver.current_url
#カレントページのURLを表示
print(url)

#session = requests.session()

#セッションの受け渡し
#for cookie in driver.get_cookies():
#    session.cookies.set(cookie["name"], cookie["value"])

#result = session.post(url)
#data1 = json.loads(result.text)

headers = {
"User-Agent":
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko)  Safari/605.1.15  Chrome/79.0.3945.117 "
}
session = requests.session()
session.headers.update(headers)

for cookie in driver.get_cookies():
       c = {cookie['name']: cookie['value']}
       session.cookies.update(c)

result = session.post(url)
result.raise_for_status()

if 'json' in result.headers.get('content-type'):
    data1 = json.loads(result.text)
else:
    data1 = BeautifulSoup(result.text, 'html.parser')

#print(data1)

#Beautifulでやる方法
#driver.get(url)
#data1 = json.loads(BeautifulSoup(driver.page_source,"lxml").find("body").text)

# listを作成
l = [] #コロナ
l2 = [] #
l3 = [] #
l4 = [] #
l5 = [] #

# OSDN magazineのURLを変数に確認
#URL = url

# requests.get()でHTMLを取得
#result = requests.get(URL)

# BeautifulSoupの機能、html.parserでHTMLやXMLをパースできる。
#data1 = BeautifulSoup(result.text, 'html.parser')

# find_allでclassを指定し、見出しを取得
data2 = data1.find_all("a", class_="cbs-Line1Link ms-noWrap ms-displayBlock")

# 配列に格納された値をfor文とprint文で出力

for item in data2:
    print('{} ({})'.format(item.getText(), item.get('href')))

# タイトルの中に検索したい単語があった場合、そのジャンルのリストに追加
for item in data2:    
    if item.getText().upper().find("COVID") != -1 or item.getText().find("コロナ") != -1:
        print('{} ({})'.format(item.getText(), item.get('href')))
        l.append('{} ({})'.format(item.getText(), item.get('href')))
    elif item.getText().upper().find("RAKUTEN") != -1:
        l2.append('{} ({})'.format(item.getText(), item.get('href')))
    elif item.getText().upper().find("IOS") != -1:
        l3.append('{} ({})'.format(item.getText(), item.get('href')))
    elif item.getText().upper().find("ORACLE") != -1:
        l4.append('{} ({})'.format(item.getText(), item.get('href')))
    elif item.getText().upper().find("GIT") != -1:
        l5.append('{} ({})'.format(item.getText(), item.get('href')))
    else:
        pass

print(' ')       
print('コロナに関する記事')
[print(i) for i in l]
print(' ')

print('Aに関する記事')
[print(i) for i in l2]
print(' ')

print('Bに関する記事')
[print(i) for i in l3]
print(' ')

print('Cに関する記事')
[print(i) for i in l4]
print(' ')

print('Dに関する記事')
[print(i) for i in l5]
print(' ')











