import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dicPrefectures import prefectures as pref
from dicPrefectures2 import prefectures as pref2
from google.oauth2.service_account import Credentials
import gspread
# import csv
options = Options()
# options.add_argument('--headless') 

scopes = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

credentials = Credentials.from_service_account_file(
    config.jsonName,
    scopes=scopes
)

gc = gspread.authorize(credentials)

spreadsheet_url1 = config.spreadSheetUrl1
spreadsheet_url2 = config.spreadSheetUrl2
spreadsheet_url3 = config.spreadSheetUrl3

sheet1 = gc.open_by_url(spreadsheet_url1).worksheet("リクエストQJ")
sheet2 = gc.open_by_url(spreadsheet_url2).worksheet("ビューティーワークス")
sheet3 = gc.open_by_url(spreadsheet_url3).worksheet("ジョブメドレー")


browser = webdriver.Chrome(executable_path=config.chromeDriverExecutablePath, options=options)
# with open("./outputTest.csv", "w", newline='', encoding='shift-jis') as f:
#     writer = csv.writer(f)

hotpepperList = []
requestqjList = []
jobmedleyList = []

for prefCnt in range(1,len(pref)+1):
        # ホットペッパービューティーワークス
    # for prefCnt in range(1,len(pref)+1):
    if 1 <= prefCnt <= 9:
        browser.get(config.hpbwUrl1.format(prefCnt))
    else:
        browser.get(config.hpbwUrl2.format(prefCnt))
    elems = browser.find_elements(By.CLASS_NAME, 'l-card')
    
    for jobCnt in range(len(elems)):
        if jobCnt == 6:
            break
        print(jobCnt)

        elemJobDetail = elems[jobCnt].find_element(By.CLASS_NAME, 'job-description-summary__items').get_attribute('href')

        elemShopName = elems[jobCnt].find_element(By.CLASS_NAME, 'job-posting__brand-name')
        print(elemShopName.text.replace('\u3000',' '))
        hotpepperList.append(["elemShopName", pref2[prefCnt], elemShopName.text.replace('\uff5e', '~').replace('\U0001f538', '◆').replace('\u203c', '!!').replace('\uff0d', '-').replace('\u3000',' ').replace('\u2730', '★').replace('\u273f', '★').replace('\u2116', 'No.').replace('\ufe0e', '').replace('\u2f6c', '目').replace('\u2b50', '★').replace('\u2013', '_').replace('\ufe0f', '').replace('\u2661', '★').replace('\u2160', '1'), elemJobDetail])
        
        # elemThumbnail = elems[jobCnt].find_element(By.CLASS_NAME, 'job-posting__carousel').find_element(By.TAG_NAME, 'img').get_attribute('data-src')
        # print(elemThumbnail)
        # hotpepperList.append(["elemThumbnail", elemThumbnail])

        elemCatchCopy = elems[jobCnt].find_element(By.CLASS_NAME, 'job-posting__job-catch')
        print(elemCatchCopy.text)
        hotpepperList.append(["elemCatchCopy", pref2[prefCnt], elemCatchCopy.text.replace('\uff5e', '~').replace('\U0001f538', '◆').replace('\u203c', '!!').replace('\uff0d', '-').replace('\u3000',' ').replace('\u2730', '★').replace('\u273f', '★').replace('\u2116', 'No.').replace('\ufe0e', '').replace('\u2f6c', '目').replace('\u2b50', '★').replace('\u2013', '_').replace('\ufe0f', '').replace('\u2661', '★').replace('\u2160', '1')])

        elemSalary = elems[0].find_element(By.CLASS_NAME, 'job-description-summary__item')
        print(elemSalary.text)
        hotpepperList.append(["elemSalary", pref2[prefCnt], elemSalary.text.replace('\uff5e', '~').replace('\U0001f538', '◆').replace('\u203c', '!!').replace('\uff0d', '-').replace('\u3000',' ').replace('\u2730', '★').replace('\u273f', '★').replace('\u2116', 'No.').replace('\ufe0e', '').replace('\u2f6c', '目').replace('\u2b50', '★').replace('\u2013', '_').replace('\ufe0f', '').replace('\u2661', '★').replace('\u2160', '1').replace('"', '')])

        if len(elems[jobCnt].find_elements(By.CLASS_NAME, 'job-posting__recruitment-store-link')) == 1:
            elemAccess = elems[jobCnt].find_element(By.CLASS_NAME, 'job-posting__recruitment-store-link')
            elemAccessShopName = elemAccess.find_element(By.CLASS_NAME, 'job-posting__recruitment-store-name')
            elemAccessRoute = elemAccess.find_element(By.CLASS_NAME, 'job-posting__recruitment-store-access')
            print(elemAccessShopName.text)
            hotpepperList.append(["elemAccess", pref2[prefCnt], elemAccessShopName.text.replace('\uff5e', '~').replace('\U0001f538', '◆').replace('\u203c', '!!').replace('\uff0d', '-').replace('\u3000',' ').replace('\u2730', '★').replace('\u273f', '★').replace('\u2116', 'No.').replace('\ufe0e', '').replace('\u2f6c', '目').replace('\u2b50', '★').replace('\u2013', '_').replace('\ufe0f', '').replace('\u2661', '★').replace('\u2160', '1') \
            + "\n" + elemAccessRoute.text.replace('\uff5e', '~').replace('\U0001f538', '◆').replace('\u203c', '!!').replace('\uff0d', '-').replace('\u3000',' ').replace('\u2730', '★').replace('\u273f', '★').replace('\u2116', 'No.').replace('\ufe0e', '').replace('\u2f6c', '目').replace('\u2b50', '★').replace('\u2013', '_').replace('\ufe0f', '').replace('\u2661', '★').replace('\u2160', '1')])
            print(elemAccessRoute.text)
            # elemAccessLink = elemAccess.get_attribute('href')
            # print(elemAccessLink)
            # hotpepperList.append(['この求人にアクセス', elemAccessLink])
        else:
            elemsAccess = elems[jobCnt].find_elements(By.CLASS_NAME, 'job-posting__recruitment-store-link')
            for elemAccess in elemsAccess:
                elemAccessShopName = elemAccess.find_element(By.CLASS_NAME, 'job-posting__recruitment-store-name')
                elemAccessRoute = elemAccess.find_element(By.CLASS_NAME, 'job-posting__recruitment-store-access')
                hotpepperList.append(["elemAccess", pref2[prefCnt], elemAccessShopName.text.replace('\uff5e', '~').replace('\U0001f538', '◆').replace('\u203c', '!!').replace('\uff0d', '-').replace('\u3000',' ').replace('\u2730', '★').replace('\u273f', '★').replace('\u2116', 'No.').replace('\ufe0e', '').replace('\u2f6c', '目').replace('\u2b50', '★').replace('\u2013', '_').replace('\ufe0f', '').replace('\u2661', '★').replace('\u2160', '1') \
                                      + "\n" + elemAccessRoute.text.replace('\uff5e', '~').replace('\U0001f538', '◆').replace('\u203c', '!!').replace('\uff0d', '-').replace('\u3000',' ').replace('\u2730', '★').replace('\u273f', '★').replace('\u2116', 'No.').replace('\ufe0e', '').replace('\u2f6c', '目').replace('\u2b50', '★').replace('\u2013', '_').replace('\ufe0f', '').replace('\u2661', '★').replace('\u2160', '1')])
                print(elemAccessShopName.text)
                print(elemAccessRoute.text)
                # elemAccessLink = elemAccess.get_attribute('href')
                # print(elemAccessLink)
                # hotpepperList.append(['この求人にアクセス', elemAccessLink])
        
        elemLinktoApply = elems[jobCnt].find_element(By.CLASS_NAME, 'c-button').get_attribute('href')
        print(elemLinktoApply)
        hotpepperList.append(["elemLinktoApply", pref2[prefCnt], "この求人にアクセス", elemLinktoApply])

    # リクエストQJ
# for prefCnt in range(1, len(pref)+1):
    browser.get(config.reqjUrl1 + pref[prefCnt] + config.reqjUrl2)
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

            elemShopName = elems[incriment].find_element(By.CLASS_NAME, 'history__card-content').find_element(By.CLASS_NAME, 'history__card-subtitle')
            elemJobDetail = elems[incriment].find_element(By.CLASS_NAME, 'history__card-body').find_element(By.TAG_NAME, 'a').get_attribute('href')
            print(elemShopName.text)
            requestqjList.append(["elemShopName", pref2[prefCnt], elemShopName.text, elemJobDetail])

            # elemThumbnail = elems[incriment].find_element(By.TAG_NAME, 'img').get_attribute('src')
            # print(elemThumbnail)
            # requestqjList.append(["elemThumbnail", elemThumbnail])

            elemCatchCopy = elems[incriment].find_element(By.CLASS_NAME, 'history__card-title')
            print(elemCatchCopy.text)
            requestqjList.append(["elemCatchCopy", pref2[prefCnt], elemCatchCopy.text.replace('\uff5e', '~').replace('\U0001f538', '◆').replace('\u203c', '!!').replace('\uff0d', '-').replace('\u3000',' ').replace('\u2730', '★').replace('\u273f', '★').replace('\u2116', 'No.').replace('\ufe0e', '').replace('\u2f6c', '目').replace('\u2b50', '★').replace('\u2013', '_').replace('\ufe0f', '').replace('\u2661', '★').replace('\u2160', '1')])

            print(elemSalary.text)
            requestqjList.append(["elemSalary", pref2[prefCnt], elemSalary.text.replace('\uff5e', '~').replace('\U0001f538', '◆').replace('\u203c', '!!').replace('\uff0d', '-').replace('\u3000',' ').replace('\u2730', '★').replace('\u273f', '★').replace('\u2116', 'No.').replace('\ufe0e', '').replace('\u2f6c', '目').replace('\u2b50', '★').replace('\u2013', '_').replace('\ufe0f', '').replace('\u2661', '★').replace('\u2160', '1')])

            elemAccess = elems[incriment].find_element(By.CLASS_NAME, 'history__card-content').find_element(By.CLASS_NAME, 'history__card-address')
            print(elemAccess.text)
            requestqjList.append(["elemAccess", pref2[prefCnt], elemAccess.text.replace('\uff5e', '~').replace('\U0001f538', '◆').replace('\u203c', '!!').replace('\uff0d', '-').replace('\u3000',' ').replace('\u2730', '★').replace('\u273f', '★').replace('\u2116', 'No.').replace('\ufe0e', '').replace('\u2f6c', '目').replace('\u2b50', '★').replace('\u2013', '_').replace('\ufe0f', '').replace('\u2661', '★').replace('\u2160', '1')])

            elemLinktoApply = elems[incriment].find_element(By.CLASS_NAME, 'history__card-content').find_element(By.CLASS_NAME, 'button').get_attribute('href')
            print(elemLinktoApply)
            requestqjList.append(["elemLinktoApply", pref2[prefCnt], "この求人にアクセス", elemLinktoApply])

            jobCnt += 1
            incriment += 1
        else:
            incriment += 1
            continue
    
    #ジョブメドレー
    browser.get(config.jmedreyUrl.format(prefCnt))
    elems = browser.find_element(By.CLASS_NAME, "o-wrapper__body").find_element(By.CLASS_NAME, "o-container").\
            find_element(By.CLASS_NAME, "o-container__column").find_element(By.CLASS_NAME, "c-offers-sort-area__contents").find_elements(By.CLASS_NAME, 'o-gutter-row__item')
    imgList = []
    while len(imgList) < 7:
        if elems[len(imgList)].find_elements(By.CLASS_NAME, "c-priority-job-offer-card__heading"):
            elemShopName = elems[len(imgList)].find_element(By.CLASS_NAME, "c-priority-job-offer-card__heading").find_element(By.CLASS_NAME, "c-text-link").text
            elemJobDetail = elems[len(imgList)].find_element(By.CLASS_NAME, "c-priority-job-offer-card__heading").find_element(By.CLASS_NAME, "c-text-link").get_attribute('href')
            jobmedleyList.append(["elemShopName", pref2[prefCnt], elemShopName, elemJobDetail])
            print(elemShopName)
            
            elemCatchCopy = elems[len(imgList)].find_element(By.CLASS_NAME, "c-priority-job-offer-card__detail").text
            jobmedleyList.append(["elemCatchCopy", pref2[prefCnt], elemCatchCopy.replace('\uff5e', '~').replace('\U0001f538', '◆').replace('\u203c', '!!').replace('\uff0d', '-').replace('\u3000',' ').replace('\u2730', '★').replace('\u273f', '★').replace('\u2116', 'No.').replace('\ufe0e', '').replace('\u2f6c', '目').replace('\u2b50', '★').replace('\u2013', '_').replace('\ufe0f', '').replace('\u2661', '★').replace('\u2160', '1')])
            print(elemCatchCopy)

            elemSalary = elems[len(imgList)].find_element(By.CLASS_NAME, "c-priority-job-offer-card__tbody").find_elements(By.TAG_NAME, "tr")[0].find_element(By.TAG_NAME, "td").text
            jobmedleyList.append(["elemSalary", pref2[prefCnt], elemSalary.replace('\uff5e', '~').replace('\U0001f538', '◆').replace('\u203c', '!!').replace('\uff0d', '-').replace('\u3000',' ').replace('\u2730', '★').replace('\u273f', '★').replace('\u2116', 'No.').replace('\ufe0e', '').replace('\u2f6c', '目').replace('\u2b50', '★').replace('\u2013', '_').replace('\ufe0f', '').replace('\u2661', '★').replace('\u2160', '1')])
            print(elemSalary)

            elemAccess = elems[len(imgList)].find_element(By.CLASS_NAME, "c-priority-job-offer-card__tbody").find_elements(By.TAG_NAME, "tr")[1].find_element(By.TAG_NAME, "td").text
            jobmedleyList.append(["elemAccess", pref2[prefCnt], elemAccess.replace('\uff5e', '~').replace('\U0001f538', '◆').replace('\u203c', '!!').replace('\uff0d', '-').replace('\u3000',' ').replace('\u2730', '★').replace('\u273f', '★').replace('\u2116', 'No.').replace('\ufe0e', '').replace('\u2f6c', '目').replace('\u2b50', '★').replace('\u2013', '_').replace('\ufe0f', '').replace('\u2661', '★').replace('\u2160', '1')])
            print(elemAccess)

            elemThumbnail = elems[len(imgList)].find_element(By.CLASS_NAME, "c-priority-job-offer-card__heading").find_element(By.CLASS_NAME, "c-priority-job-offer-card__image-box").find_element(By.TAG_NAME, "img").get_attribute('data-src')
            imgList.append(elemThumbnail)
            infLoopCnt = 0
            while True:
                print("infLoopCnt", infLoopCnt)
                if elems[len(imgList)+1].find_elements(By.CLASS_NAME, "c-priority-job-offer-card__heading"):
                    if infLoopCnt >= 3:
                        break
                    elemAccess = elems[len(imgList)+1].find_element(By.CLASS_NAME, "c-priority-job-offer-card__tbody").find_elements(By.TAG_NAME, "tr")[1].find_element(By.TAG_NAME, "td").text
                    jobmedleyList.append(["elemAccess", pref2[prefCnt], elemAccess.replace('\uff5e', '~').replace('\U0001f538', '◆').replace('\u203c', '!!').replace('\uff0d', '-').replace('\u3000',' ').replace('\u2730', '★').replace('\u273f', '★').replace('\u2116', 'No.').replace('\ufe0e', '').replace('\u2f6c', '目').replace('\u2b50', '★').replace('\u2013', '_').replace('\ufe0f', '').replace('\u2661', '★').replace('\u2160', '1')])
                    print(elemAccess)

                    elemThumbnail = elems[len(imgList)+1].find_element(By.CLASS_NAME, "c-priority-job-offer-card__heading").find_element(By.CLASS_NAME, "c-priority-job-offer-card__image-box").find_element(By.TAG_NAME, "img").get_attribute('data-src')

                    imgList.append(elemThumbnail)
                else:
                    break
                infLoopCnt += 1
        else:
            elemShopName = elems[len(imgList)+1].find_element(By.CLASS_NAME, "c-text-link").text
            elemJobDetail = elems[len(imgList)+1].find_element(By.CLASS_NAME, "c-text-link").get_attribute("href")
            print(elemShopName)
            jobmedleyList.append(["elemShopName", pref2[prefCnt], elemShopName, elemJobDetail])

            elemCatchCopy = elems[len(imgList)+1].find_element(By.CLASS_NAME, "gtm-click-job-offer-card").find_element(By.TAG_NAME, "h3").text
            jobmedleyList.append(["elemCatchCopy", pref2[prefCnt], elemCatchCopy.replace('\uff5e', '~').replace('\U0001f538', '◆').replace('\u203c', '!!').replace('\uff0d', '-').replace('\u3000',' ').replace('\u2730', '★').replace('\u273f', '★').replace('\u2116', 'No.').replace('\ufe0e', '').replace('\u2f6c', '目').replace('\u2b50', '★').replace('\u2013', '_').replace('\ufe0f', '').replace('\u2661', '★').replace('\u2160', '1')])
            print(elemCatchCopy)

            elemSalary = elems[len(imgList)+1].find_element(By.CLASS_NAME, "gtm-click-job-offer-card").find_elements(By.TAG_NAME, "tr")[0].find_element(By.TAG_NAME, "p").text
            jobmedleyList.append(["elemSalary", pref2[prefCnt], elemSalary.replace('\uff5e', '~').replace('\U0001f538', '◆').replace('\u203c', '!!').replace('\uff0d', '-').replace('\u3000',' ').replace('\u2730', '★').replace('\u273f', '★').replace('\u2116', 'No.').replace('\ufe0e', '').replace('\u2f6c', '目').replace('\u2b50', '★').replace('\u2013', '_').replace('\ufe0f', '').replace('\u2661', '★').replace('\u2160', '1')])
            print(elemSalary)

            elemAccess = elems[len(imgList)+1].find_element(By.CLASS_NAME, "gtm-click-job-offer-card").find_elements(By.TAG_NAME, "tr")[3].find_element(By.TAG_NAME, "p").text
            jobmedleyList.append(["elemAccess", pref2[prefCnt], elemAccess.replace('\uff5e', '~').replace('\U0001f538', '◆').replace('\u203c', '!!').replace('\uff0d', '-').replace('\u3000',' ').replace('\u2730', '★').replace('\u273f', '★').replace('\u2116', 'No.').replace('\ufe0e', '').replace('\u2f6c', '目').replace('\u2b50', '★').replace('\u2013', '_').replace('\ufe0f', '').replace('\u2661', '★').replace('\u2160', '1')])
            print(elemAccess)

            elemLinktoApply = elems[len(imgList)+1].find_element(By.CLASS_NAME, "gtm-click-job-offer-card").find_element(By.TAG_NAME, "a").get_attribute("href")
            jobmedleyList.append(["elemLinktoApply", pref2[prefCnt], "この求人にアクセス", elemLinktoApply])
            print(elemLinktoApply)

            elemThumbnail = elems[len(imgList)+1].find_element(By.CLASS_NAME, "gtm-click-job-offer-card").find_element(By.TAG_NAME, "img").get_attribute("data-src")
            imgList.append(elemThumbnail)
            infLoopCnt = 0
            while True:
                if not elems[len(imgList)+1].find_elements(By.CLASS_NAME, "c-priority-job-offer-card__heading"):
                    if infLoopCnt >= 3:
                        break
                    elemAccess = elems[len(imgList)+1].find_element(By.CLASS_NAME, "gtm-click-job-offer-card").find_elements(By.TAG_NAME, "tr")[3].find_element(By.TAG_NAME, "p").text
                    jobmedleyList.append(["elemAccess", pref2[prefCnt], elemAccess.replace('\uff5e', '~').replace('\U0001f538', '◆').replace('\u203c', '!!').replace('\uff0d', '-').replace('\u3000',' ').replace('\u2730', '★').replace('\u273f', '★').replace('\u2116', 'No.').replace('\ufe0e', '').replace('\u2f6c', '目').replace('\u2b50', '★').replace('\u2013', '_').replace('\ufe0f', '').replace('\u2661', '★').replace('\u2160', '1')])
                    print(elemAccess)

                    elemThumbnail = elems[len(imgList)+1].find_element(By.CLASS_NAME, "gtm-click-job-offer-card").find_element(By.TAG_NAME, "img").get_attribute("data-src")

                    imgList.append(elemThumbnail)
                else:
                    break
                infLoopCnt += 1
browser.quit()

sheet1.clear()
sheet2.clear()
sheet3.clear()
sheet1.update('A1', requestqjList)
sheet2.update('A1', hotpepperList)
sheet3.update('A1', jobmedleyList)