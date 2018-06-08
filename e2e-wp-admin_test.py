from selenium import webdriver

# Initialize Driver
print "# Initialize Driver"
driver = webdriver.Firefox()
driver.get("http://localhost/wp-admin/setup-config.php")

# Select language
print "# Select language"
driver.find_element_by_id("language-continue").click()

# Configure database
print "# Configure database"
driver.find_element_by_css_selector("body > p.step > a").click()
driver.find_element_by_id("uname").clear()
driver.find_element_by_id("uname").send_keys("wordpress")
driver.find_element_by_id("pwd").clear()
driver.find_element_by_id("pwd").send_keys("admin123")
driver.find_element_by_name("submit").click()

# Run Installation
print "# Run Installation"
driver.find_element_by_link_text("Run the installation").click()
driver.find_element_by_id("weblog_title").clear()
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
print "# Login"
driver.find_element_by_link_text("Log In").click()
driver.find_element_by_id("user_login").clear()
driver.find_element_by_id("user_login").send_keys("purestorage")
driver.find_element_by_id("user_pass").clear()
driver.find_element_by_id("user_pass").send_keys("Pure$torage123")
driver.find_element_by_id("wp-submit").click()

# driver.quit()
print "# driver.quit()"
driver.quit()
