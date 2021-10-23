from selenium import webdriver
import time

contry_code = int(input('Enter contry code without "+" : '))
number = int(input('Enter Number'))
number_of_message = int(input('How many messege you want to send : '))
messege = input('Enter messege : ')
driver=webdriver.Chrome(executable_path=r"C:\Users\RAKESH\Desktop\chromedriver.exe")
link = 'https://api.whatsapp.com/send/?phone='+str(contry_code)+str(number)+'&text&app_absent=0'
driver.get(link)

driver.find_element_by_xpath('//*[@id="action-button"]').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="fallback_block"]/div/div/a').click()
print('Please scan QR code')
time.sleep(10)

for i in range(number_of_message):
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]').send_keys(messege)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[2]').click()