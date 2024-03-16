from selenium import webdriver
from selenium.webdriver.common.by import By
from dicPrefectures import prefectures as pref
import csv

browser = webdriver.Chrome()
with open("./outputTest.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)

    # # リジョブ
    # for i in range(1,len(pref)+1):
    #     browser.get("https://relax-job.com/search?business_type=biyoshi&employment=regular-member&feature=new-graduate.student&occupation=assistant_position&pref={}&sort=new".format(i))
    #     elems = browser.find_elements(By.CLASS_NAME, 'sc-kBqmDu')
    #     for i in range(len(elems)):
    #         if i == 6:
    #             break
    #         print(i)
    #         elemShopName = elems[i].find_element(By.CLASS_NAME, 'sc-bwcZwS')
    #         print(elemShopName.text)
    #         writer.writerow([elemShopName.text])

    #         elemCatchCopy = elems[i].find_element(By.CLASS_NAME, 'header-text')
    #         print(elemCatchCopy.text)
    #         writer.writerow([elemCatchCopy.text])

    #         elemSalary = elems[i].find_element(By.TAG_NAME, 'dd')
    #         if not elems[i].find_elements(By.CLASS_NAME, 'main-table-list'):
    #             elemAccess = elems[i].find_element(By.CLASS_NAME, 'sc-hUhoqY')
    #             print(elemAccess.text)
    #             writer.writerow([elemAccess.text])

    #         else:
    #             elemsAccess = elems[i].find_elements(By.CLASS_NAME, 'main-table-list')
    #             for elemAccess in elemsAccess:
    #                 print(elemAccess.text)
    #                 writer.writerow([elemAccess.text])

    #         elemThumbnail = elems[i].find_element(By.CLASS_NAME, 'image-outer-pc').find_element(By.TAG_NAME, 'img').get_attribute('data-original')
    #         print(elemThumbnail)
    #         writer.writerow([elemThumbnail])

    #         elemLinktoApply = elems[i].find_element(By.CLASS_NAME, 'sc-havuDZ').find_element(By.CLASS_NAME, 'apply-button').get_attribute('href')
    #         print(elemLinktoApply)
    #         writer.writerow([elemLinktoApply])

    # # ホットペッパービューティーワークス
    # for i in range(1,len(pref)+1):
    #     if 1 <= i <= 9:
    #         browser.get("https://work.beauty.hotpepper.jp/search/?prefecture=0{}&occupation=OC01&salary_amount=&employment_pattern=EP1&kodawari_condition=KO02&kodawari_condition=".format(i))
    #     else:
    #         browser.get("https://work.beauty.hotpepper.jp/search/?prefecture={}&occupation=OC01&salary_amount=&employment_pattern=EP1&kodawari_condition=KO02&kodawari_condition=".format(i))
    #     elems = browser.find_elements(By.CLASS_NAME, 'l-card')
        
    #     for i in range(len(elems)):
    #         if i == 6:
    #             break
    #         print(i)
    #         elemThumbnail = elems[i].find_element(By.CLASS_NAME, 'job-posting__carousel').find_element(By.TAG_NAME, 'img').get_attribute('data-src')
    #         print(elemThumbnail)
    #         writer.writerow([elemThumbnail])

    #         elemShopName = elems[i].find_element(By.CLASS_NAME, 'job-posting__brand-name')
    #         print(elemShopName.text.replace('\u3000',' '))
    #         writer.writerow([elemShopName.text.replace('\u3000',' ')])

    #         elemCatchCopy = elems[i].find_element(By.CLASS_NAME, 'job-posting__job-catch')
    #         print(elemCatchCopy.text)
    #         writer.writerow([elemCatchCopy.text])

    #         elemSalary = elems[0].find_element(By.CLASS_NAME, 'job-description-summary__item')
    #         print(elemSalary.text)
    #         writer.writerow([elemSalary.text])

    #         if len(elems[i].find_elements(By.CLASS_NAME, 'job-posting__recruitment-store-link')) == 1:
    #             elemAccess = elems[i].find_element(By.CLASS_NAME, 'job-posting__recruitment-store-link')
    #             elemAccessLink = elemAccess.get_attribute('href')
    #             print(elemAccessLink)
    #             writer.writerow([elemAccessLink])
    #             elemAccessShopName = elemAccess.find_element(By.CLASS_NAME, 'job-posting__recruitment-store-name')
    #             print(elemAccessShopName.text)
    #             writer.writerow([elemAccessShopName.text])
    #             elemAccessRoute = elemAccess.find_element(By.CLASS_NAME, 'job-posting__recruitment-store-access')
    #             print(elemAccessRoute.text)
    #             writer.writerow([elemAccessRoute.text])
    #         else:
    #             elemsAccess = elems[i].find_elements(By.CLASS_NAME, 'job-posting__recruitment-store-link')
    #             for elemAccess in elemsAccess:
    #                 elemAccessLink = elemAccess.get_attribute('href')
    #                 print(elemAccessLink)
    #                 writer.writerow([elemAccessLink])
    #                 elemAccessShopName = elemAccess.find_element(By.CLASS_NAME, 'job-posting__recruitment-store-name')
    #                 print(elemAccessShopName.text)
    #                 writer.writerow([elemAccessShopName.text])
    #                 elemAccessRoute = elemAccess.find_element(By.CLASS_NAME, 'job-posting__recruitment-store-access')
    #                 print(elemAccessRoute.text)
    #                 writer.writerow([elemAccessRoute.text])
            
    #         elemLinktoApply = elems[i].find_element(By.CLASS_NAME, 'c-button').get_attribute('href')
    #         print(elemLinktoApply)
    #         writer.writerow([elemLinktoApply])

    # リクエストQJ
    for i in range(1, len(pref)+1):
        browser.get('https://www.qjnavi.jp/search?pref='+ pref[i] +'&technical_rank=biyoshi-assistant')
        elems =  browser.find_elements(By.CLASS_NAME, 'history__card-item')
        cnt = 0
        incriment = 0
        while cnt < 6:
            if len(elems) - 1 < incriment:
                break
            print('cnt: ', cnt)
            print('incriment: ', incriment)
            elemSalary = elems[incriment].find_element(By.CLASS_NAME, 'history__card-content').find_element(By.CLASS_NAME, 'history__card-definition').find_element(By.CLASS_NAME, 'history__card-definition-desc')
            if elemSalary.text != '-':
                elemThumbnail = elems[incriment].find_element(By.TAG_NAME, 'img').get_attribute('src')
                print(elemThumbnail)
                writer.writerow([elemThumbnail])

                elemCatchCopy = elems[incriment].find_element(By.CLASS_NAME, 'history__card-title')
                print(elemCatchCopy.text)
                writer.writerow([elemCatchCopy.text])

                elemShopName = elems[incriment].find_element(By.CLASS_NAME, 'history__card-content').find_element(By.CLASS_NAME, 'history__card-subtitle')
                print(elemShopName.text)
                writer.writerow([elemShopName.text])

                elemAccess = elems[incriment].find_element(By.CLASS_NAME, 'history__card-content').find_element(By.CLASS_NAME, 'history__card-address')
                print(elemAccess.text)
                writer.writerow([elemShopName.text])

                print(elemSalary.text)
                writer.writerow([elemSalary.text])

                elemLinktoApply = elems[incriment].find_element(By.CLASS_NAME, 'history__card-content').find_element(By.CLASS_NAME, 'button').get_attribute('href')
                print(elemLinktoApply)
                writer.writerow([elemLinktoApply])

                cnt += 1
                incriment += 1
            else:
                incriment += 1
                continue

            