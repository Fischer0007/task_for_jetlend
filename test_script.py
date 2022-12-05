import random
import time
import pyautogui

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from configuration import *


def test_new_application(driver):
    driver.get(URL)
    time.sleep(4)
    driver.find_element(By.CLASS_NAME, "onboardingNavigation_container__right__2e5Sh").click()
    time.sleep(4)


    driver.find_element(By.CSS_SELECTOR, "#root > div.layout_container__3UOP4 > div.mainContainer_container__2tFuH > "
                                         "div > div:nth-child(1) > div.block_footer__1SzBe.block_footer--no-border__M9z4Z "
                                         "> div > div.dashboard_buttons-container__main__1NKdH > span:nth-child(1) > button").click()
    time.sleep(4)

    driver.find_element(By.CSS_SELECTOR, ".modal_footer__1zeVm > span:nth-child(2) > button:nth-child(1)").click()

    time.sleep(4)

    #slider
    move = ActionChains(driver)
    slider = driver.find_element(By.CSS_SELECTOR, "#root > div.layout_container__3UOP4 > div.mainContainer_container__2tFuH >"
                                                  " div > div > div.wizard_wizard__screen__2NV8p > "
                                                  "div.stepProfileDetailsInput_form-container__3g_5G > div.grid-row.h-mt-20 > "
                                                  "div > div.range_knobs-container__NvCj8 > div")

    move.click_and_hold(slider).move_by_offset(random.randint(1,200), 0).release().perform()
    time.sleep(3)

    driver.find_element(By.CSS_SELECTOR, "#root > div.layout_container__3UOP4 > div.mainContainer_container__2tFuH > "
                                         "div > div > div.wizard_wizard__screen__2NV8p > div.wizard_wizard__footer__1I5Xb "
                                         "> div:nth-child(1) > span > button").click()
    time.sleep(4)

    if "Отказ" in driver.page_source:
        driver.save_screenshot('screenshots/отказ в одобрении.png')
    else:
        driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div/div[2]/div[5]/div[1]/button').click()

        time.sleep(5)

        driver.find_element(By.XPATH, "/html/body/div[12]/div/div/form/section/div/div/div[2]/div[1]/label").click()
        time.sleep(1)
        pyautogui.write(r'G:\passport-main-page-demo-01.5a795789.jpg')
        pyautogui.press('enter')
        time.sleep(5)
        driver.find_element(By.XPATH, "/html/body/div[12]/div/div/form/section/div/div/div[2]/div[2]/label").click()
        time.sleep(1)
        pyautogui.write(r'G:\passport-main-page-demo-01.5a795789.jpg')
        pyautogui.press('enter')

        time.sleep(10)
        driver.find_element(By.XPATH, "/html/body/div[12]/div/div/form/section/footer/span[2]/button").click()

        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div/div[2]/div[6]/div/span/button').click()
        time.sleep(4)

        driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div/div[2]/div[6]/div[2]/div[3]/div/button').click()
        time.sleep(15)

        driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div/div[2]/div[12]/div/span/button').click()
        time.sleep(15)
        driver.save_screenshot('screenshots/Возобновляемая кредитная линия предварительно одобрена.png')

