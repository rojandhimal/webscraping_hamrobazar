from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path=r"C:\\webdrivers\\chromedriver.exe")

# This is url to scrap
url = "https://hamrobazaar.com/i2614958-house-on-sale.html"

# run url
driver.get(url)

# yo chi detail ko wrapper element
parent_td = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/table[4]/tbody/tr/td/table/tbody/tr/td/table[2]/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr")
# yesla chi tyo wrapper vitra sabai table lai tancha
child_table = parent_td.find_elements_by_tag_name('table')
# aba vira ko sabai data tanne
data_details = {'general_details':[],'seller_details':[],'description':[],'pricing':[],'property_details':[]}
labels = []
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
            if i == 1:
                labels.append(row_elements[i].text)
            elif i >1:
                if index == 0:
                    print(row_elements[i].text)
                    General_details.append(row_elements[i].text)
                elif index == 2:
                    print(row_elements[i].text)
                    seller_details.append(row_elements[i].text)
                elif index == 3:
                    print(row_elements[i].text)
                    description.append(row_elements[i].text)
                elif index == 7:
                    print(row_elements[i].text)
                    pricing.append(row_elements[i].text)
                elif index == 9:
                    print(row_elements[i].text)
                    property_details.append(row_elements[i].text)

all_detail_list.append(General_details)
all_detail_list.append(seller_details)
all_detail_list.append(description)
all_detail_list.append(pricing)
all_detail_list.append(property_details)

print("This is all details",all_detail_list)

data_details['general_details'].append(General_details)
data_details['seller_details'].append(seller_details)
data_details['description'].append(description)
data_details['pricing'].append(pricing)
data_details['property_details'].append(property_details)

print("data_details", data_details)
        
    

print("loop ends here")