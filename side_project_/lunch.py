from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import logging
import time

# 設定日誌
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class LunchOrderBot:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')

    def init_driver(self):
        try:
            driver = webdriver.Chrome(options=self.options)
            driver.maximize_window()
            return driver
        except Exception as e:
            logging.error(f"初始化驅動失敗: {str(e)}")
            return None

    def wait_and_find_element(self, driver, by, value, timeout=10):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except TimeoutException:
            print(f"等待元素超時: {value}")
            raise

    def switch_to_new_window(self, driver, original_window):
        print("等待新視窗開啟...")
        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)

        # 切換到新視窗
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                print("已切換到新視窗")
                return True
        return False

    def login(self, driver):
        try:
            original_window = driver.current_window_handle
            print("等待登入表單載入...")

            username_field = self.wait_and_find_element(driver, By.NAME, "username")
            password_field = self.wait_and_find_element(driver, By.NAME, "password")

            print("輸入帳號密碼...")
            username_field.clear()
            username_field.send_keys(self.username)
            time.sleep(0.5)

            password_field.clear()
            password_field.send_keys(self.password)
            time.sleep(0.5)

            print("點擊登入按鈕...")
            login_button = self.wait_and_find_element(driver, By.NAME, "imageField")
            login_button.click()

            # 切換到新視窗
            if not self.switch_to_new_window(driver, original_window):
                print("無法找到新開啟的視窗")
                return False

            # 確認選單已載入
            self.wait_and_find_element(driver, By.ID, "submenu_tbl")
            print("登入成功！")
            return True

        except Exception as e:
            print(f"登入發生錯誤: {str(e)}")
            return False

    def navigate_to_lunch_order(self, driver):
        try:
            time.sleep(1)

            print("移動到「公共事務區」...")
            public_affairs = self.wait_and_find_element(driver, By.ID, "T_PM000200")
            actions = ActionChains(driver)
            actions.move_to_element(public_affairs).perform()
            time.sleep(1)

            print("尋找並移動到「資源申請」...")
            resource_xpath = "//td[contains(text(), '資源申請')]"
            resource_request = self.wait_and_find_element(driver, By.XPATH, resource_xpath)
            actions.move_to_element(resource_request).perform()
            time.sleep(1)

            print("點擊「便當訂購」...")
            lunch_xpath = "//td[contains(text(), '便當訂購')]"
            lunch_order = self.wait_and_find_element(driver, By.XPATH, lunch_xpath)
            actions.move_to_element(lunch_order).click().perform()

            print("等待頁面載入...")
            time.sleep(2)
            return True

        except Exception as e:
            print(f"導航過程發生錯誤: {str(e)}")
            return False

    def select_lunch(self, driver):
        """選擇便當"""
        try:
            print("等待頁面載入...")
            time.sleep(2)  # 等待頁面完全載入

            # 切換到 mainFrame iframe
            print("切換到訂餐框架...")
            iframe = self.wait_and_find_element(driver, By.NAME, "mainFrame")
            driver.switch_to.frame(iframe)

            # 使用精確的 ID 找到 checkbox
            print("尋找便當選項...")
            checkbox = self.wait_and_find_element(driver, By.ID, "chk_6891")

            print("點擊便當選項...")
            checkbox.click()
            time.sleep(1)  # 等待點擊後的反應

            # 確認是否已選中
            if checkbox.is_selected():
                print("已成功選擇便當")
            else:
                print("便當選擇可能未成功，嘗試再次點擊...")
                checkbox.click()
                time.sleep(1)

            # 切回主框架
            driver.switch_to.default_content()
            return True

        except Exception as e:
            print(f"選擇便當時發生錯誤: {str(e)}")
            import traceback
            print(traceback.format_exc())
            # 確保切回主框架
            try:
                driver.switch_to.default_content()
            except:
                pass
            return False

    def run_order_process(self):
        print("開始訂購流程...")
        driver = self.init_driver()

        if not driver:
            return

        try:
            print(f"開啟網頁: {self.url}")
            driver.get(self.url)

            if self.login(driver):
                if self.navigate_to_lunch_order(driver):
                    print("準備選擇便當...")
                    if self.select_lunch(driver):
                        print("便當選擇完成")
                    else:
                        print("便當選擇失敗")
                else:
                    print("無法進入訂購頁面")
            else:
                print("登入失敗")

            input("按 Enter 關閉瀏覽器...")

        except Exception as e:
            print(f"執行過程發生錯誤: {str(e)}")
            import traceback
            print(traceback.format_exc())
        finally:
            driver.quit()
            print("已關閉瀏覽器")


def main():
    # 在這裡填入實際的網址和帳號密碼
    bot = LunchOrderBot(
        url="http://192.168.2.105/ehrportal/LoginFOrginal.asp",
        username="H210372",
        password="B123209852"
    )

    bot.run_order_process()


if __name__ == "__main__":
    main()