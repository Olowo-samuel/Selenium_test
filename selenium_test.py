from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.geeksforgeeks.org/python/find_element_by_link_text-driver-method-selenium-python/")

#This will wait for 5 seconds, until a table has been found
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//table/tbody")) 
)

#To obtain the number of rows in the table
#Since each table will have an header, i am going to be adding 1
#to account for the table, makes sense right

#I think I kinda fiured something out
#You can just right click on the elements attribute and copy the full XPATH
rows = 1 + len(driver.find_elements(By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/div/div[1]/article/div[3]/table/tbody/tr"))

#To obtain the number of columns in the table
#We can just count the nuumber of coloumns in the first row or in any other row
cols = len(driver.find_elements(By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div/div/div[1]/article/div[3]/table/tbody/tr[1]/td"))

print(rows)
print(cols)