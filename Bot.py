#!/usr/bin/python3
# -- coding: utf-8 --
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy,ProxyType
from time import sleep
import random


def proxyip():
    a=str(random.randint(1,254))
    b=str(random.randint(1,254))
    c=str(random.randint(1,254))
    d=str(random.randint(1,254))
    e="."
    f=a+e+b+e+c+e+d
    return f

giris=int(input("İzlenme Sayısı: "))
say=0
while True:
    say+=1
    httpProxy="http://{}".format(proxyip())+":80"
    httpsProxy = "https://{}".format(proxyip())+":443"
    ftpProxy = "ftp://{}".format(proxyip())+":21"

    proxy=Proxy({
        'ProxyType':ProxyType.MANUAL,
        'http':httpProxy,
        'https':httpsProxy,
        'ftp':ftpProxy,
        'noProxy':''
    })
    path=("C:\Users\Akıncı\Desktop\bot\geckodriver")
    driver = webdriver.Firefox(proxy=proxy,executable_path=path)
    print("Ne kadar görüntülendi: ",say)
    print("İp Adresleri >>>>>> HTTP = ",httpProxy," HTTPS = ",httpsProxy," FTP = ",ftpProxy)
    driver.get("BOT ATILCAK LİNK")
    sleep(10)
    driver.find_element_by_xpath("//body/ytd-app[1]/div[1]/ytd-page-manager[1]/ytd-watch-flexy[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ytd-player[1]/div[1]/div[1]/div[28]/div[2]/div[1]/button[1]").click()
    driver.find_element_by_xpath("//body/ytd-app[1]/div[1]/ytd-page-manager[1]/ytd-watch-flexy[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ytd-player[1]/div[1]/div[1]/div[28]/div[2]/div[1]/span[1]/button[1]").click()
    sayi=random.randint(2950,3000)
    sleep(sayi)
    driver.close()
    if giris==say:
        print("Görüntülenme Tamamlandı")
        break
