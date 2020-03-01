from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome(executable_path="C:\selenium\drivers\chromedriver.exe")
driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')

element=driver.find_element_by_id('RESULT_RadioButton-9')
drp=Select(element)
drp.select_by_visible_text('Morning')
#drp.select_by_index(2)
#drp.select_by_value('Radio-2')

print(len(drp.options))

all_options=drp.options
for option in all_options:
    print(option.text)