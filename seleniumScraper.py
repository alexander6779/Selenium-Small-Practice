from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# data for xlsx
data = {}

# scraping data from website
try:
    driver = webdriver.Chrome()

    # Ir a la página
    driver.get("https://www.tutiempo.net/las-palmas-de-gran-canaria.html")

    # Esperar hasta que el botón de consentimiento aparezca y hacer clic en él
    consent_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='fc-button fc-cta-consent fc-primary-button']")))
    consent_button.click()
    
    days = [day.text for day in driver.find_elements(By.CLASS_NAME, "day")]
    min_temp = [temp.text for temp in driver.find_elements(By.XPATH, "//span[@class='t min']")]
    max_temp = [temp.text for temp in driver.find_elements(By.XPATH, "//span[@class='t max']")]

    # Hacer clic en el enlace del día siguiente
    next_day_link = driver.find_element(By.XPATH, "//a[contains(@href, 'tutiempo.net/las-palmas-de-gran-canaria.html?dia=8')]")
    next_day_link.click()
        
    # Obtener los elementos de los días y temperaturas mínimas y máximas del día siguiente
    days += [day.text for day in driver.find_elements(By.CLASS_NAME, "day")]
    min_temp += [temp.text for temp in driver.find_elements(By.XPATH, "//span[@class='t min']")]
    max_temp += [temp.text for temp in driver.find_elements(By.XPATH, "//span[@class='t max']")]
    
    data = { 'día' : days,
            'min_temperaturas' : min_temp,
            'max_temperaturas': max_temp}

    assert "No results found." not in driver.page_source

finally:
    driver.close()
    
# filling a dataframe and exporting to xlsx
dt = pd.DataFrame(data)
dt.to_excel('tiempo.xlsx', index=False)