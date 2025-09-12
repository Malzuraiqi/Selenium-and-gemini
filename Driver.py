from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.by import By

class DriverActions:
    def scroll_to_bottom(self, driver):
        frame_to_scroll_to = driver.find_element(By.ID, "spvFeedHeader")
        previous = 0

        while True:
            titles = driver.find_elements(By.CLASS_NAME, "product-title-text")
            number_of_items = len(titles)

            if number_of_items > previous:
                previous = number_of_items
                ActionChains(driver).scroll_to_element(frame_to_scroll_to).perform()
                time.sleep(3)
            else:
                break

        return titles