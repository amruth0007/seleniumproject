from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\selenium\drivers\chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

driver.switch_to_frame(0)

driver.find_element_by_name("RESULT_FileUpload-10").send_keys("C://Users/amruth/Desktop/Ramesh/Ramesh-Photo.jpg")