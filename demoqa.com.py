import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.webdriver import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/automation-practice-form")

#First step: Getting all the Fields

#Name (First and Last)
first_name = driver.find_element('xpath', '//input[@id="firstName"]')
last_name = driver.find_element('xpath', '//input[@id="lastName"]')
first_name.send_keys("Shadowheart")
last_name.send_keys("Astarion")

#Email
email = driver.find_element('xpath', '//input[@id="userEmail"]')
email.send_keys("emailchecking@gmail.com")

#Gender radio buttons
gender_button = driver.find_element('xpath', '//label[@for="gender-radio-1"]')
gender_button.click()

#Mobile Telephone Number
phone_number = driver.find_element('xpath', '//input[@id="userNumber"]')
phone_number.send_keys("6087777888")

#Date of Birth
month_year = "January 2019"
day = "1"

birth = driver.find_element('xpath', '//input[@id="dateOfBirthInput"]')
birth.click()

while True:
    current_year = driver.find_element('xpath',
                                       '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[5]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[1]').text
    print(current_year)
    if current_year == month_year:
        break

    button_year_back = driver.find_element('xpath','/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[5]/div[2]/div[2]/div[2]/div/div/button[1]')
    button_year_back.click()

date_wanted = driver.find_element('xpath', '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[5]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[5]')
date_wanted.click()
phone_number.click()

#Subjects
subjects = driver.find_element('xpath', '//input[@id="subjectsInput"]')
subjects.click()
subjects.send_keys("C")
time.sleep(2)
choice_one = driver.find_element('xpath', '//div[@id="react-select-2-option-2"]')
choice_one.click()

#Hobbies radio buttons
hobbies = driver.find_elements('xpath', '//div[@id="hobbiesWrapper"]//label[@class="custom-control-label"]')

# Click each checkbox
for hobby in hobbies:
    # Perform the click
    driver.execute_script("arguments[0].click();", hobby)
    #time.sleep(2)

#Picture selection
picture_upload = driver.find_element('xpath', '//input[@id="uploadPicture"]')
picture_upload.send_keys("C:/Users/user/Desktop/auto.jpg")

#Current Address
address = driver.find_element('xpath', '//textarea[@id="currentAddress"]')
address.send_keys("Czech Republic, Prague, 10000")

#State and City Dropdown menu (2 of them)
state = driver.find_element('xpath', '//div[@id="state"]')
city = driver.find_element('xpath', '//div[@id="city"]')

state.click()
driver.find_element('xpath', '//div[@id="react-select-3-option-2"]').click()

city.click()
driver.find_element('xpath', '//div[@id="react-select-4-option-1"]').click()

time.sleep(3)

#Submission button
submit_button = driver.find_element('xpath', '//button[@id="submit"]')
submit_button.click()
time.sleep(3)