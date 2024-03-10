from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
browser = webdriver.Chrome()
browser.get("https://relax-job.com/search?business_type=biyoshi&employment=regular-member&feature=new-graduate.student&occupation=assistant_position&pref=1&sort=new")

wait = WebDriverWait(browser, 10)

elems = browser.find_elements(By.CLASS_NAME, 'sc-kBqmDu')
with open("./outputTest.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for i in range(len(elems)):
        if i == 6:
            break
        print(i)
        elemShopName = elems[i].find_element(By.CLASS_NAME, 'sc-bwcZwS')
        print(elemShopName.text)
        writer.writerow([elemShopName.text])
        elemCatchCopy = elems[i].find_element(By.CLASS_NAME, 'header-text')
        print(elemCatchCopy.text)
        writer.writerow([elemCatchCopy.text])
        elemSalary = elems[i].find_element(By.TAG_NAME, 'dd')
        if not elems[i].find_elements(By.CLASS_NAME, 'main-table-list'):
            elemAccess = elems[i].find_element(By.CLASS_NAME, 'sc-hUhoqY')
            print(elemAccess.text)
            writer.writerow([elemAccess.text])
        else:
            elemsAccess = elems[i].find_elements(By.CLASS_NAME, 'main-table-list')
            for elemAccess in elemsAccess:
                print(elemAccess.text)
                writer.writerow([elemAccess.text])
        elemThumbnail = elems[i].find_element(By.CLASS_NAME, 'image-outer-pc').find_element(By.TAG_NAME, 'img').get_attribute('data-original')
        print(elemThumbnail)
        writer.writerow([elemThumbnail])
        elemLinktoApply = elems[i].find_element(By.CLASS_NAME, 'sc-havuDZ').find_element(By.CLASS_NAME, 'apply-button').get_attribute('href')
        print(elemLinktoApply)
        writer.writerow([elemLinktoApply])