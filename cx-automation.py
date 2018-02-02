import time
from selenium import webdriver

chromedriver_path=r'C:\Users\Advait Joshi\Documents\Python\automation\chromedriver.exe'
website_path=r'https://cx.usiu.ac.ke/ICS/'
username=r'ajoshi@usiu.ac.ke'
password=r'646270.ab'

driver=webdriver.Chrome(chromedriver_path)
driver.get(website_path)

#login page
username_elem=driver.find_element_by_name('userName')
username_elem.send_keys(username)
password_elem=driver.find_element_by_name('password')
password_elem.send_keys(password)
submit_elem=driver.find_element_by_name('btnLogin')
submit_elem.click()

#home page
student_elem=driver.find_element_by_link_text('STUDENT')
student_elem.click()

#student page
check_grades_elem=driver.find_element_by_link_text('Check Your Grades')
check_grades_elem.click()

#check grades page
view_report_elem=driver.find_element_by_link_text('View Final Grade Report')
view_report_elem.click()

time.sleep(5)
driver.quit()
