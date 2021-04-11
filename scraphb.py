from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path = r"C:\\webdrivers\\chromedriver.exe")

# This is url to scrap
url = "https://hamrobazaar.com/c112-real-estate"

# run url
driver.get(url)

# get categories table element
categories_sidebar = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table[5]/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/font/a")

# select category row 
row=driver.find_elements_by_xpath("/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table[5]/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/table/tbody/tr")

def getAllLink(row):
    '''This methon taes row element of table that contains categories
    input : row element
    output : list of all link present inside that row
    '''
    links = []
    for r in row[1:]:
        lis =r.find_elements_by_tag_name("a")
        for l in lis:
            links.append(l.get_attribute('href'))
    
    return links


# sabai categories ko links haru aayo ani links vanne list ma basyo
categories_links = getAllLink(row)






driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://www.google.com/imghp?hl=EN")

driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[2])
driver.get("https://asterdio.com/career/")


allTab = driver.window_handles
print(allTab)
driver.switch_to.window(driver.window_handles[0])


# driver.quit()   