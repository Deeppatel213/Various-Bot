from selenium import webdriver
import csv
from time import sleep

#strting enrollment
initial = int(input("Enter First enrollment : "))
final = int(input("Enter Last enrollment : "))
total_sem = int(input('Enter Total Sem : '))
print("Please Enter each sem total subject space seperated : ")
sem_sub = [int(x) for x in input().split()]
path = input("Enter path where you save result : ")
file_name = input('Enter File name : ')
################################################test

#define driver path
driver = webdriver.Chrome(executable_path=r'C:\Users\RAKESH\Desktop\chromedriver.exe')

driver.get('https://www.students.gtu.ac.in/')

for i in range(initial,final):
#enrollment information
    driver.find_element_by_xpath('//*[@id="txtEnrollNo"]').clear()
    driver.find_element_by_xpath('//*[@id="txtEnrollNo"]').send_keys(i)
    driver.find_element_by_xpath('//*[@id="CodeNumberTextBox"]').click()
    sleep(10)
    try:
#basic information
        driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
        driver.find_element_by_xpath('//*[@id="CodeNumberTextBox"]').click()
        name = driver.find_element_by_xpath('//*[@id="lblName"]').text
        enrollment = driver.find_element_by_xpath('//*[@id="lblMapNumber"]').text

# cpi spi information
        for j in driver.find_elements_by_xpath('//*[@id="div2"]'):
            cpi = driver.find_element_by_xpath('.//*[@id="grdv2"]/tbody/tr[2]/td[2]').text
            cgpa = driver.find_element_by_xpath('.//*[@id="grdv2"]/tbody/tr[2]/td[3]').text
            spi = driver.find_element_by_xpath('.//*[@id="grdvLastExm"]/tbody/tr[2]/td[5]').text
            total_back = driver.find_element_by_xpath('.//*[@id="grdv2"]/tbody/tr[2]/td[4]').text
            current_back = driver.find_element_by_xpath('.//*[@id="grdvLastExm"]/tbody/tr[2]/td[4]').text
# result
        for j in driver.find_elements_by_xpath('//*[@id="div3"]'):
            sub_code = []
            sub_grade = []
            for k in range(total_sem):
                temp_str = './/*[@id="rptmarksheetHistoryOuter_rptmarksheetHistoryOuterInner_'+str(k)
                temp_grade_str = './/*[@id="rptmarksheetHistoryOuter_rptmarksheetHistoryOuterInner_'+str(k)
                for m in range(sem_sub[k]):
                    temp_sub_code_sem = temp_str+'_rptmarksheetHistoryInnerNew_0_TextBox3_'+str(m)+'"]'
                    temp_grade_sem = temp_grade_str+'_rptmarksheetHistoryInnerNew_0_Label1_'+str(m)+'"]'
                    s_code = driver.find_element_by_xpath(temp_sub_code_sem).text
                    sub_code.append(s_code)
                    s_grade = driver.find_element_by_xpath(temp_grade_sem).text
                    sub_grade.append(s_grade)
        final_header = ['Name','Enrollment']+sub_code+['CPI','SPI','CGPA','Current Backlock','Total Backlock']
        final_grade_obtain = [name,enrollment]+sub_grade+[cpi,spi,cgpa,current_back,total_back]
        final_answer = dict(zip(final_header,final_grade_obtain))
################ File Save #####################
        temp_file_name = path+'/'+file_name+'.csv'
        if i==initial:
            with open(temp_file_name, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=final_header)
                writer.writeheader()
        with open(temp_file_name, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=final_header)
            writer.writerow(final_answer)
        print(enrollment)
    except:
        print('..........Failed.......')