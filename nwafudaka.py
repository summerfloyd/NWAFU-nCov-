import os
import time
import msvcrt
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
account=input("请输入账号：")
password=input("请输入密码：")

def daka():
    chrome_options=Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(r"https://app.nwafu.edu.cn/ncov/wap/default/index")
    driver.find_element_by_xpath("//*[@id='app']/div[2]/div[1]/input").send_keys(account)  # 输入账号
    driver.find_element_by_xpath("//*[@id='app']/div[2]/div[2]/input").send_keys(password)  # 输入密码
    driver.find_element_by_class_name("btn").click()  # 点击登陆
    time.sleep( 5 )
    driver.find_element_by_xpath("/html/body/div[1]/div/div/section/div[4]/ul/li[6]/div/input").click()  # 获取地理位置
    driver.find_element_by_xpath("/html/body/div[1]/div/div/section/div[5]/div/a").click()  # 提交信息
    time.sleep( 5 )
    driver.close()
    print("打卡完成！按Y重新打卡,关闭窗口即可退出 ")

def repeat():
    key = input('press key') 
    if key == 'y' or 'Y':
        daka()
        repeat()
    else:
            os._exit()

daka()
repeat()

if __name__ == "__main__":
    nwafudaka()
    os.system("pause")
