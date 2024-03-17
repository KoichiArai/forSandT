from selenium import webdriver
from selenium.webdriver.common.by import By
from dicPrefectures import prefectures as pref
from dicPrefectures2 import prefectures as pref2
import csv

browser = webdriver.Chrome()
with open("./outputTest.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)

    # リジョブ
    for prefCnt in range(1,len(pref)+1):
        browser.get("https://relax-job.com/search?business_type=biyoshi&employment=regular-member&feature=new-graduate.student&occupation=assistant_position&pref={}&sort=new".format(prefCnt))
        elems = browser.find_elements(By.CLASS_NAME, 'sc-kBqmDu')
        for jobCnt in range(len(elems)):
            if jobCnt == 6:
                break
            print(jobCnt)

            elemThumbnail = elems[jobCnt].find_element(By.CLASS_NAME, 'image-outer-pc').find_element(By.TAG_NAME, 'img').get_attribute('data-original')
            print(elemThumbnail)
            writer.writerow([elemThumbnail])

            elemShopName = elems[jobCnt].find_element(By.CLASS_NAME, 'sc-bwcZwS')
            print(elemShopName.text)
            writer.writerow([elemShopName.text])

            elemCatchCopy = elems[jobCnt].find_element(By.CLASS_NAME, 'header-text')
            print(elemCatchCopy.text)
            writer.writerow([elemCatchCopy.text])

            elemSalary = elems[jobCnt].find_element(By.TAG_NAME, 'dd')
            if not elems[jobCnt].find_elements(By.CLASS_NAME, 'main-table-list'):
                elemAccess = elems[jobCnt].find_element(By.CLASS_NAME, 'sc-hUhoqY')
                print(elemAccess.text)
                writer.writerow([elemAccess.text])

            else:
                elemsAccess = elems[jobCnt].find_elements(By.CLASS_NAME, 'main-table-list')
                for elemAccess in elemsAccess:
                    print(elemAccess.text)
                    writer.writerow([elemAccess.text])

            elemLinktoApply = elems[jobCnt].find_element(By.CLASS_NAME, 'sc-havuDZ').find_element(By.CLASS_NAME, 'apply-button').get_attribute('href')
            print(elemLinktoApply)
            writer.writerow([elemLinktoApply])

        # ホットペッパービューティーワークス
    # for prefCnt in range(1,len(pref)+1):
        if 1 <= prefCnt <= 9:
            browser.get("https://work.beauty.hotpepper.jp/search/?prefecture=0{}&occupation=OC01&salary_amount=&employment_pattern=EP1&kodawari_condition=KO02&kodawari_condition=".format(prefCnt))
        else:
            browser.get("https://work.beauty.hotpepper.jp/search/?prefecture={}&occupation=OC01&salary_amount=&employment_pattern=EP1&kodawari_condition=KO02&kodawari_condition=".format(prefCnt))
        elems = browser.find_elements(By.CLASS_NAME, 'l-card')
        
        for jobCnt in range(len(elems)):
            if jobCnt == 6:
                break
            print(jobCnt)

            elemThumbnail = elems[jobCnt].find_element(By.CLASS_NAME, 'job-posting__carousel').find_element(By.TAG_NAME, 'img').get_attribute('data-src')
            print(elemThumbnail)
            writer.writerow([elemThumbnail])

            elemShopName = elems[jobCnt].find_element(By.CLASS_NAME, 'job-posting__brand-name')
            print(elemShopName.text.replace('\u3000',' '))
            writer.writerow([elemShopName.text.replace('\u3000',' ')])

            elemCatchCopy = elems[jobCnt].find_element(By.CLASS_NAME, 'job-posting__job-catch')
            print(elemCatchCopy.text)
            writer.writerow([elemCatchCopy.text])

            elemSalary = elems[0].find_element(By.CLASS_NAME, 'job-description-summary__item')
            print(elemSalary.text)
            writer.writerow([elemSalary.text])

            if len(elems[jobCnt].find_elements(By.CLASS_NAME, 'job-posting__recruitment-store-link')) == 1:
                elemAccess = elems[jobCnt].find_element(By.CLASS_NAME, 'job-posting__recruitment-store-link')
                elemAccessLink = elemAccess.get_attribute('href')
                print(elemAccessLink)
                writer.writerow([elemAccessLink])
                elemAccessShopName = elemAccess.find_element(By.CLASS_NAME, 'job-posting__recruitment-store-name')
                print(elemAccessShopName.text)
                writer.writerow([elemAccessShopName.text])
                elemAccessRoute = elemAccess.find_element(By.CLASS_NAME, 'job-posting__recruitment-store-access')
                print(elemAccessRoute.text)
                writer.writerow([elemAccessRoute.text])
            else:
                elemsAccess = elems[jobCnt].find_elements(By.CLASS_NAME, 'job-posting__recruitment-store-link')
                for elemAccess in elemsAccess:
                    elemAccessLink = elemAccess.get_attribute('href')
                    print(elemAccessLink)
                    writer.writerow([elemAccessLink])
                    elemAccessShopName = elemAccess.find_element(By.CLASS_NAME, 'job-posting__recruitment-store-name')
                    print(elemAccessShopName.text)
                    writer.writerow([elemAccessShopName.text])
                    elemAccessRoute = elemAccess.find_element(By.CLASS_NAME, 'job-posting__recruitment-store-access')
                    print(elemAccessRoute.text)
                    writer.writerow([elemAccessRoute.text])
            
            elemLinktoApply = elems[jobCnt].find_element(By.CLASS_NAME, 'c-button').get_attribute('href')
            print(elemLinktoApply)
            writer.writerow([elemLinktoApply])

        # リクエストQJ
    # for prefCnt in range(1, len(pref)+1):
        browser.get('https://www.qjnavi.jp/search?pref='+ pref[prefCnt] +'&technical_rank=biyoshi-assistant')
        elems =  browser.find_elements(By.CLASS_NAME, 'history__card-item')
        jobCnt = 0
        incriment = 0
        while jobCnt < 6:
            if len(elems) - 1 < incriment:
                break
            print('jobCnt: ', jobCnt)
            print('incriment: ', incriment)
            elemSalary = elems[incriment].find_element(By.CLASS_NAME, 'history__card-content').find_element(By.CLASS_NAME, 'history__card-definition').find_element(By.CLASS_NAME, 'history__card-definition-desc')
            if elemSalary.text != '-':
                elemThumbnail = elems[incriment].find_element(By.TAG_NAME, 'img').get_attribute('src')
                print(elemThumbnail)
                writer.writerow([elemThumbnail])
                
                elemShopName = elems[incriment].find_element(By.CLASS_NAME, 'history__card-content').find_element(By.CLASS_NAME, 'history__card-subtitle')
                print(elemShopName.text)
                writer.writerow([elemShopName.text])

                elemCatchCopy = elems[incriment].find_element(By.CLASS_NAME, 'history__card-title')
                print(elemCatchCopy.text)
                writer.writerow([elemCatchCopy.text])

                print(elemSalary.text)
                writer.writerow([elemSalary.text])

                elemAccess = elems[incriment].find_element(By.CLASS_NAME, 'history__card-content').find_element(By.CLASS_NAME, 'history__card-address')
                print(elemAccess.text)
                writer.writerow([elemShopName.text])

                elemLinktoApply = elems[incriment].find_element(By.CLASS_NAME, 'history__card-content').find_element(By.CLASS_NAME, 'button').get_attribute('href')
                print(elemLinktoApply)
                writer.writerow([elemLinktoApply])

                jobCnt += 1
                incriment += 1
            else:
                incriment += 1
                continue

            