from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.drizzle-hit.com/#/login")

driver.implicitly_wait(5)
driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div[2]/div[2]/div[2]/form/div[1]/div/div[1]/input").send_keys("superadmin")
driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div[2]/div[2]/div[2]/form/div[2]/div/div[1]/input").send_keys("cqyhzl_Admin@2019")
driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div[2]/div[2]/div[2]/form/div[3]/div/div/div[1]/div/input").send_keys("1111")
driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div[2]/div[2]/div[2]/form/div[5]/div/button").click()
driver.quit()