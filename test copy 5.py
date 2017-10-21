from selenium import webdriver

b=webdriver.Chrome()
b.get('')

for i in range(2,42):
    x.append(b.find_element_by_xpath("//table[@id='myTable']/tbody[1]/tr[%d]/td[4]"%i).text)
    y.append(b.find_element_by_xpath("//table[@id='myTable']/tbody[1]/tr[%d]/td[5]"%i).text)
