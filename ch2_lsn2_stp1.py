import time


try:
    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome('D:/chromedriver/chromedriver.exe')
    browser.get(link)

    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector("option:nth-child(2)").click()
    browser.find_element_by_css_selector("[value='1']").click()
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value("1")     

finally:
    time.sleep(7)
    browser.close()
    browser.quit()
