from selenium import webdriver
import time
path = input("Plece input playlist link : ")
num_of_videos = int(input("Number of videos ?? :"))
driver_path = input('Enter Webdriver Path')
driver=webdriver.Chrome(executable_path=driver_path)

urls = []
driver.get(path)
for _ in driver.find_elements_by_xpath('//*[@id="contents"]/ytd-item-section-renderer'):
    driver.find_element_by_xpath('.//*[@id="video-title"]').click()
    urls.append(driver.current_url)
time.sleep(10)
for i in range(num_of_videos):
    for _ in driver.find_elements_by_xpath('//*[@id="items"]'):
        temp = '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[2]/div/ytd-playlist-panel-renderer/div/div[2]/ytd-playlist-panel-video-renderer['+str(i+1)+']/a/div/div[3]/h4/span'
    driver.find_element_by_xpath(temp).click()
    urls.append(driver.current_url)
    print(driver.current_url)
    time.sleep(5)
print(urls)