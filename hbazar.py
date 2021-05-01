from selenium import webdriver


driver = webdriver.Chrome(executable_path = r"C:\\webdrivers\\chromedriver.exe")

url = "https://hamrobazaar.com/c112-real-estate"

driver.get(url)

categories_sidebar = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table[5]/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/font/a")
# categories_sidebar.click()
print(categories_sidebar)

# this copy href value in variable
# link = driver.find_element_by_xpath("//*[@id='tab_cat1']/table/tbody/tr[2]/td/font/a").get_attribute('href')
# driver.get(link)


row=driver.find_elements_by_xpath("/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table[5]/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/table/tbody/tr")
print(row)

row_count = len(row)
print("row count",row_count)

for r in row[1:]:
    lis =r.find_elements_by_tag_name("a")
    for l in lis:
        print(l.get_attribute('href'))
    # print(td.find_element_by_tag_name('a').get_attribute('href'))


link = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table[5]/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/table/tbody/tr[12]/td/font/a").get_attribute('href')
print(link)

print(type(row_count))

for i in range(row_count):
    j=i+1
    print(j)
    # xpath = "//*[@id='tab_cat1']/table/tbody/tr["+str(j)+"]/td/font/a"
    xpath = "//*[@id='tab_cat1']/table/tbody/tr[{j}]/td/font/a".format(j=j)
        # //*[@id="tab_cat1"]/table/tbody/tr[2]/td/font/a
        # //*[@id="tab_cat1"]/table/tbody/tr[3]/td/font/a
        # //*[@id="tab_cat1"]/table/tbody/tr[13]/td/font/a
    print(xpath)
        
    link = driver.find_element_by_xpath("//*[@id='tab_cat1']/table/tbody/tr[2]/td/font/a").get_attribute('href')
    print("This is link 1",link)
    link2 = driver.find_element_by_xpath(xpath).get_attribute('href')
    print("This is link 2",link2)
        # link = driver.find_element_by_xpath(xpath).get_attribute('href')
        # print("this is link of row {row} => {link}".format(row,link))


print(driver.title)
print(driver.current_url)
driver.quit()

