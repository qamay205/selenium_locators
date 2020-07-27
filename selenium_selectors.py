# 1. Submit filled test form
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

input_data = {
    'full_name': 'Elon Musk',
    'Email': 'working_trampoline@gmail.com',
    'Current_address': 'Trampoline',
    'Permanent_adress': 'SpaceX'
}

driver = webdriver.Chrome(executable_path="C:/Selenium/chromedriver.exe")
driver.get("https://demoqa.com/text-box")
driver.find_element_by_css_selector('[id="userName"]').send_keys(input_data['full_name'])
driver.find_element_by_css_selector('[id="userEmail"]').send_keys(input_data['Email'])
driver.find_element_by_css_selector('[id="currentAddress"]').send_keys(input_data['Current_address'])
driver.find_element_by_css_selector('[id="permanentAddress"]').send_keys(input_data['Permanent_adress'])

element = driver.find_element_by_css_selector('[id="submit"]')
move_element = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[6]/span/div/div[1]')
actions = ActionChains(driver)
actions.move_to_element(move_element).click(element).perform()

el_user = driver.find_element_by_css_selector('[id="name"]')
assert driver.find_element_by_css_selector('[id="name"]').text == 'Name:' + input_data['full_name']
el_email = driver.find_element_by_css_selector('[id="email"]')
assert driver.find_element_by_css_selector('[id="email"]').text == 'Email:' + input_data['Email']
el_curr_address = driver.find_element_by_xpath('//*[@id="currentAddress"]')
print(el_curr_address.text)
assert driver.find_element_by_xpath('//*[@id="currentAddress"]').text == 'Current Address :Trampoline'
el_perm_address = driver.find_element_by_css_selector('[id="permanentAddress"]')
assert driver.find_element_by_css_selector('[id="permanentAddress"]').text == 'Permananet Address :' + input_data['Permanent_adress']
print(el_curr_address.text)

# 2. Click on [Code in it] button after selecting new Category
# https://testpages.herokuapp.com/styled/basic-ajax-test.html

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:/Selenium/chromedriver.exe")
driver.get("https://testpages.herokuapp.com/styled/basic-ajax-test.html")
driver.implicitly_wait(10)

sel = Select(driver.find_element_by_css_selector('[id="combo1"]'))
sel.select_by_visible_text('Server')
sel2 = Select(driver.find_element_by_css_selector('[name="language_id"]'))
sel2.select_by_visible_text('Flash')
driver.find_element_by_css_selector('[name="submitbutton"]').click()

# 3. Print all text in Lorem/Ipsum/Dolor columns
https://the-internet.herokuapp.com/challenging_dom#delete """
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:/Selenium/chromedriver.exe")

driver.get("https://the-internet.herokuapp.com/challenging_dom")
elems = driver.find_elements_by_css_selector('tbody tr')

for i in elems:
    print(i.find_element_by_css_selector('tbody tr td:nth-child(1)').text)
    print(i.find_element_by_css_selector('tbody tr td:nth-child(2)').text)
    print(i.find_element_by_css_selector('tbody tr td:nth-child(3)').text)
    print(i.find_element_by_css_selector('tbody tr td:nth-child(4)').text)
    print(i.find_element_by_css_selector('tbody tr td:nth-child(5)').text)
    print(i.find_element_by_css_selector('tbody tr td:nth-child(6)').text)

