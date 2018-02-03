import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def exam_results_checker_chrome():
    chromedriver_path=r'C:\Users\Advait Joshi\Documents\Python\automation\chromedriver.exe'
    website_path=r'https://cx.usiu.ac.ke/ICS/'
    username=r'uname@usiu.ac.ke' #enter your username here
    password=r'*********' #enter your passsword here

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

    #scroll down on grades page
    html_elem=driver.find_element_by_tag_name('html')
    html_elem.send_keys(Keys.PAGE_DOWN)

    time.sleep(5)
    driver.quit()

if __name__ == '__main__':
    exam_results_checker_chrome()
