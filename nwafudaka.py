import os
import time
from datetime import datetime
from selenium import webdriver
from apscheduler.schedulers.blocking import BlockingScheduler
from selenium.webdriver.chrome.options import Options
account=input("请输入账号：")
password=input("请输入密码：")
userhour,userminute=input("请输入每日需要定时打卡的时间，以空格分隔；如早上9：28则输入[9 28]：").split(' ')

def daka():
    chrome_options=Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(r"https://app.nwafu.edu.cn/ncov/wap/default/index")
    driver.find_element_by_xpath("//*[@id='app']/div[2]/div[1]/input").send_keys(account)  # 输入账号
    driver.find_element_by_xpath("//*[@id='app']/div[2]/div[2]/input").send_keys(password)  # 输入密码
    driver.find_element_by_class_name("btn").click()  # 点击登陆
    print('正在登陆...')
    time.sleep( 5 )
    driver.find_element_by_xpath("/html/body/div[1]/div/div/section/div[4]/ul/li[6]/div/input").click()  # 获取地理位置
    print('正在获取地理位置')
    time.sleep( 5 )
    driver.find_element_by_xpath("/html/body/div[1]/div/div/section/div[5]/div/a").click()
    driver.find_element_by_xpath("//*[@id="wapcf"]/div/div[2]/div[2]").click() # 提交信息
    time.sleep( 5 )
    driver.close()
    print("打卡完成！按Y重新打卡,关闭窗口即可退出 ")

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(daka, 'cron', hour=(userhour),minute=(userminute))
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
