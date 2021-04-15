import time
from selenium import webdriver

import datetime
from selenium.common.exceptions import UnexpectedAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.set_page_load_timeout(100)
try:
    driver.get('http://wxcas.bjfu.edu.cn/tpass/login?service=https%3A%2F%2Fs.bjfu.edu.cn%2Ftp_fp%2Fview%3Fm%3Dfp#act=fp/formHome') # 打开网站
except TimeoutException:
    print('time out after 30 seconds when loading page')
    driver.execute_script('window.stop()')
driver.maximize_window()
driver.implicitly_wait(10)  # 控制间隔时间，等待浏览器反应

with open('userinfo.txt','r') as info:
    username = info.readline()
    password = info.readline()
    reason=info.readline()

driver.find_element_by_id('un').click()  # 点击用户名输入框
driver.find_element_by_id('un').clear()  # 清空输入框
driver.find_element_by_id('un').send_keys(username)  # 自动敲入用户名

driver.find_element_by_id('pd').click()  # 点击密码输入框
driver.find_element_by_id('pd').clear()  # 清空输入框
driver.find_element_by_id('pd').send_keys(password)  # 自动敲入密码
try:
    #采用class定位登陆按钮
##driver.find_element_by_class_name('login_box_landing_btn').click() # 点击“登录”按钮
    #driver.implicitly_wait(10)  # 控制间隔时间，等待浏览器反应

    name=driver.find_element_by_xpath('//*[@id="user-btn-01"]/span').text

        ##time.sleep(2)

        #采用xpath定位报平安按钮
    driver.find_element_by_xpath('//*[@id="formHome_serve_content"]/div[2]').click() # 点击“报出校申请”按钮
        #driver.implicitly_wait(10)  # 控制间隔时间，等待浏览器反应
        ##driver.get('https://s.bjfu.edu.cn/tp_fp/view?m=fp#from=hall&serveID=280612cb-5fcf-47f2-850a-d2084ca7e3c6&act=fp/serveapply')


    time.sleep(2)

    driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a').click()

    time.sleep(2)
    driver.switch_to.frame('formIframe')

    driver.find_element_by_class_name('van-checkbox__label').click()
    driver.find_element_by_id('QTSY').click()  # 点击具体事由输入框
    driver.find_element_by_id('QTSY').clear()  # 清空输入框
    driver.find_element_by_id('QTSY').send_keys(reason)  # 自动敲入具体事由

    driver.find_element_by_xpath('//*[@id="body_0"]/div[1]/div[7]/div[2]/div/button/span[1]').click()
    driver.find_element_by_xpath('//*[@id="body_0"]/div[1]/div[7]/div[2]/div/div/ul/li[2]/a').click()
    driver.find_element_by_xpath('//*[@id="body_0"]/div[1]/div[8]/div[2]/div/button/span[1]').click()
    driver.find_element_by_xpath('//*[@id="body_0"]/div[1]/div[8]/div[2]/div/div/ul/li[4]/a').click()
    driver.find_element_by_xpath('//*[@id="body_0"]/div[1]/div[12]/div[2]/div[1]/button/span[1]').click()
    driver.find_element_by_xpath('//*[@id="body_0"]/div[1]/div[12]/div[2]/div[1]/div/ul/li[2]/a').click()
    driver.find_element_by_xpath('//*[@id="body_0"]/div[1]/div[12]/div[2]/div[2]/button/span[1]').click()
    driver.find_element_by_xpath('//*[@id="body_0"]/div[1]/div[12]/div[2]/div[2]/div/ul/li[2]/a').click()
    driver.find_element_by_xpath('//*[@id="body_0"]/div[1]/div[12]/div[2]/div[3]/button/span[1]').click()
    driver.find_element_by_xpath('//*[@id="body_0"]/div[1]/div[12]/div[2]/div[3]/div/ul/li[7]/a').click()

    js = "$('#JHCXSJ').removeAttr('readonly')"  # jQuery，移除属性
    # js = "$('input:eq(0)').attr('readonly',false)"  # jQuery，设置为false
    driver.execute_script(js)

    driver.find_element_by_xpath('//*[@id="JHCXSJ"]').send_keys(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))


    js = "$('#JHFXSJ').removeAttr('readonly')"  # jQuery，移除属性
    # js = "$('input:eq(0)').attr('readonly',false)"  # jQuery，设置为false
    driver.execute_script(js)

    driver.find_element_by_xpath('//*[@id="JHFXSJ"]').send_keys((datetime.datetime.now()+datetime.timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M"))

    driver.switch_to.parent_frame()

    driver.find_element_by_xpath('//*[@id="commit"]').click()

except:
    print('申请失败')

driver.quit()


