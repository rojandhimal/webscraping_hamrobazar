from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path=r"C:\\webdrivers\\chromedriver.exe")

# This is url to scrap
url = "https://hamrobazaar.com/c112-real-estate"

# run url
driver.get(url)

# get categories table element
categories_sidebar = driver.find_element_by_xpath(
    "/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table[5]/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/font/a")

# select category row
row = driver.find_elements_by_xpath(
    "/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table[5]/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/table/tbody/tr")


def getAllLink(row):
    '''This methon takes row element of table that contains categories
    input : row element
    output : list of all link present inside that row
    '''
    links = []
    for r in row[1:]:
        lis = r.find_elements_by_tag_name("a")
        for l in lis:
            links.append(l.get_attribute('href'))

    return links


# sabai categories ko links haru aayo ani links vanne list ma basyo
categories_links = getAllLink(row)





allTab = driver.window_handles
print(allTab)
driver.switch_to.window(driver.window_handles[0])

print("Opening link ",categories_links[0])



driver.get(categories_links[0])
# harek category ma palai palo jane
# for clink in categories_links:
#     driver.get(categories_links[clink])

# number of bables inside link
parent_td = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table[5]/tbody/tr/td[2]")

child_table = parent_td.find_elements_by_tag_name('table')


# yo chi category mandya aauta category kholda aaune links haru 
detail_link = []
for table in child_table[3:-1]:
    lis_a = table.find_elements_by_tag_name("a")
    if(len(lis_a)>0):
        print("This is new link to detail_link",lis_a[0].get_attribute('href'))
        detail_link.append(lis_a[0].get_attribute('href'))
        
# this is all link
# print("detail link",detail_link)


# create new tab and switch
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])

# for each link loop and get data
for dlink in detail_link:
    # open one of the link in new tab
    driver.get(detail_link[dlink])





def getAllData(link):
    table_wrapper = driver.find_elements_by_xpath("/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table[5]/tbody/tr/td[2]")

        
        


# driver.quit()
