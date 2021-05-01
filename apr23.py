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

def get_detail_link():
    '''get all hyperlink from selected categories'''
    # number of tables inside link
    parent_td = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table[5]/tbody/tr/td[2]")

    child_table = parent_td.find_elements_by_tag_name('table')


    # yo chi category mandya aauta category kholda aaune links haru 
    detail_link = []
    for table in child_table[3:-1]:
        lis_a = table.find_elements_by_tag_name("a")
        if(len(lis_a)>0):
            print("This is new link to detail_link",lis_a[0].get_attribute('href'))
            detail_link.append(lis_a[0].get_attribute('href'))
    
    return detail_link[1:]

def get_all_table_in_detail_link():
    '''This gets all table in details page'''
    # yo chi detail ko wrapper element
    parent_td = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/table[4]/tbody/tr/td/table/tbody/tr/td/table[2]/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr")
    # yesla chi tyo wrapper vitra sabai table lai tancha
    child_table = parent_td.find_elements_by_tag_name('table')
    # aba vira ko sabai data tanne
    for table in child_table:
        # number of rows
        rows = len(driver.find_elements_by_xpath("//*[@id='lblue']/tbody/tr"))
        # number of columns
        columns = len(driver.find_elements_by_xpath("//*[@id='white']"))
        # for idx, table in enumerate(child_table):
        


def click_Next_Page():
    '''This clicks next button of pagination '''

def get_details_from_dlink():
    '''This scrap all data from given link'''
    # yo chi detail ko wrapper element
    parent_td = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/table[4]/tbody/tr/td/table/tbody/tr/td/table[2]/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr")
    # yesla chi tyo wrapper vitra sabai table lai tancha
    child_table = parent_td.find_elements_by_tag_name('table')
    # aba vira ko sabai data tanne
    General_details = []
    seller_details = []
    description = []
    pricing = []
    property_details = []

    all_detail_list = []

    for index,table in enumerate(child_table):
        print("index =>",index)
        selected_list = [0,2,4,7,9]
        if index in selected_list:
            row_elements = table.find_elements_by_tag_name("tr")
            rows = len(row_elements)
            for i in range(rows):
                if i >1:
                    if index == 0:
                        print(row_elements[i].text)
                        General_details.append(row_elements[i].text)
                    elif index == 2:
                        print(row_elements[i].text)
                        seller_details.append(row_elements[i].text)
                    elif index == 7:
                        print(row_elements[i].text)
                        pricing.append(row_elements[i].text)
                    elif index == 9:
                        print(row_elements[i].text)
                        property_details.append(row_elements[i].text)
                if i == 1:
                    print(row_elements[i].text)
                    description.append(row_elements[i].text)

    all_detail_list.append(General_details)
    all_detail_list.append(seller_details)
    all_detail_list.append(description)
    all_detail_list.append(pricing)
    all_detail_list.append(property_details)

    return all_detail_list


# sabai categories ko links haru aayo ani links vanne list ma basyo
categories_links = getAllLink(row)

# create new tab and switch
driver.execute_script("window.open('');")
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])

all_data = {}
data_details = {'general_details':[],'seller_details':[],'description':[],'pricing':[],'property_details':[]}

for index,clink in enumerate(categories_links, start=1):
    print("opening this link",clink)
    driver.get(clink)
    detail_links = get_detail_link()
    all_data[index] = detail_links
    print("this is all data object",all_data)
    driver.switch_to.window(driver.window_handles[2])
    for dlink in detail_links:
        driver.get(dlink)
        product_details = get_details_from_dlink()
        data_details['general_details'].append(product_details[0])
        data_details['seller_details'].append(product_details[1])
        data_details['description'].append(product_details[2])
        data_details['pricing'].append(product_details[3])
        data_details['property_details'].append(product_details[4])
    # loop through pagination
    driver.switch_to.window(driver.window_handles[1])
    next_btn = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table[5]/tbody/tr/td[2]/table[25]/tbody/tr/td/a")
    print("This is returning",next_btn)
    if(next_btn):
        print("Click Btn")
        next_btn.click()
    else:
        pass


    print("This is data details of catgory",data_details)
        

def getAllData(link):
    table_wrapper = driver.find_elements_by_xpath("/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table[5]/tbody/tr/td[2]")

        
        


# driver.quit()
