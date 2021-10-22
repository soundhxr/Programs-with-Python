from selenium import webdriver
from time import sleep
driver = webdriver.Chrome(executable_path="D:/Python Programs/chromedriver.exe")
driver.get("https://www.youtube.com/watch?v=sgkNV0TW7no&t=613s&ab_channel=SimplyWaste")
sleep(5)
for i in range(10):
    driver.find_element_by_xpath('''/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[1]/ytd-comments-header-renderer/div[5]/ytd-comment-simplebox-renderer/div[1]/yt-formatted-string''').send_keys("Kabilan bro: *demands 100K comments.* \nMe: Ok bro, done! \nComment no: ",i)
    driver.find_element_by_xpath('''/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[1]/ytd-comments-header-renderer/div[5]/ytd-comment-simplebox-renderer/div[3]/ytd-comment-dialog-renderer/ytd-commentbox/div/div[4]/div[5]/ytd-button-renderer[2]/a/tp-yt-paper-button''').click()