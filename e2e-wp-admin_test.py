from selenium import webdriver
 
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get("http://localhost:9090/wp-admin/setup-config.php")
# print driver.title

# Select language
driver.find_element_by_id("language-continue").click()


# Configure database
driver.find_elements_by_link_text("Let's go!")[0].click()
driver.find_element_by_id("uname").clear()
driver.find_element_by_id("uname").send_keys("wordpress")
driver.find_element_by_id("pwd").clear()
driver.find_element_by_id("pwd").send_keys("admin123")
driver.find_element_by_name("submit").click()

# Run Installation
driver.find_elements_by_link_text("Run the installation")[0].click()
# driver.find_element_by_id("weblog_title").clear()
driver.find_element_by_id("weblog_title").send_keys("Data-Storage")
driver.find_element_by_id("user_login").clear()
driver.find_element_by_id("user_login").send_keys("purestorage")
driver.find_element_by_id("pass1-text").clear()
driver.find_element_by_id("pass1-text").send_keys("Pure$torage123")
driver.find_element_by_name("pw_weak").click()
driver.find_element_by_id("admin_email").clear()
driver.find_element_by_id("admin_email").send_keys("admin@email.com")
driver.find_element_by_id("submit").click()

# Login
driver.find_elements_by_link_text("Log In")[0].click()
driver.find_element_by_id("user_login").clear()
driver.find_element_by_id("user_login").send_keys("purestorage")
driver.find_element_by_id("user_pass").clear()
driver.find_element_by_id("user_pass").send_keys("Pure$torage123")
driver.find_element_by_id("wp-submit").click()

# driver.quit()
driver.quit()
