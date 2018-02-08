import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import smtplib

#function declarations begin
def open_grades_page_chrome():
    """Open the grades page on CX portal.

    Don't forget to quit the driver when you call this function.This function
    has been separated from check_exam_results_chrome for modularity
    """
    chromedriver_path=r'C:\Users\Advait Joshi\Documents\Python\automation\chromedriver.exe'#enter path to chromedriver.exe
    website_path=r'https://cx.usiu.ac.ke/ICS/'#enter website URL
    username=r'uname@usiu.ac.ke' #enter your username here
    password=r'******' #enter your passsword here

    driver=webdriver.Chrome(chromedriver_path)#open chromedriver
    driver.get(website_path)#open website

    #enter username and password and submit the form
    #log into website
    username_elem=driver.find_element_by_name('userName')
    username_elem.send_keys(username)
    password_elem=driver.find_element_by_name('password')
    password_elem.send_keys(password)
    submit_elem=driver.find_element_by_name('btnLogin')
    submit_elem.click()

    #go to student page
    student_elem=driver.find_element_by_link_text('STUDENT')
    student_elem.click()

    #go to grades page
    check_grades_elem=driver.find_element_by_link_text('Check Your Grades')
    check_grades_elem.click()

    #go to actual results/grades page
    view_report_elem=driver.find_element_by_link_text('View Final Grade Report')
    view_report_elem.click()

    #scroll down on grades page
    html_elem=driver.find_element_by_tag_name('html')
    html_elem.send_keys(Keys.PAGE_DOWN)

    return driver#allows quitting the driver from a different function

def check_exam_results_chrome():
    """Open web browser to exam results"""
    driver=open_grades_page_chrome()

    time.sleep(5)#give user time to view grades
    driver.quit()#close driver

def take_grades_screenshot():
    """Take screenshot of grades"""
    driver=open_grades_page_chrome()

    driver.save_screenshot("grades.png")#take screenshot
    os.startfile('grades.png')#open screenshot

    driver.quit()#close driver

def send_screenshot_to_email():
    "Take screenshot and send it to email"
    driver=open_grades_page_chrome()

    driver.save_screenshot("grades.png")

def main():
    """Main function"""
    print("What would you like to do?")
    print("1. Open webbrowser to grades page")
    print("2. Open screenshot of grades page")
    print("3. Send yourself a screenshot of your grades page")

    choice=int(input("Make a choice (Please use an integer): "))

    if choice==1:
        check_exam_results_chrome()
    elif choice==2:
        take_grades_screenshot()
    else:
        pass


if __name__ == '__main__':
    main()
