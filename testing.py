from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Navigate to the URL
    driver.get("https://kvdqp.net/ap/home/indexqra?id=CfDJ8OgHroCaKu9LoX5dcKGTneeBLvXEE1rez__-OmRm_1slgC4gdA-y6r5odAYQrZHzKlnsq4vewpZonZfW_VWT2i31XwcVRG6DlGmekMpOy9j_4Znhh9NekF4p3mczFbyvXcc9dbvjNFcFOeuPmcWfB3aG58W5Q3cGgtBAcsNzchR9&culture=en-MY")

    # Wait for the page to load completely
    time.sleep(5)  

    
    Name = driver.find_element(By.ID, "NewAppointmentForm")



    name_input = driver.find_element(By.ID, "name") 
    name_input.send_keys("John Doe")
        
    email_input = driver.find_element(By.ID, "email") 
    email_input.send_keys("john.doe@example.com")

    phone_input = driver.find_element(By.ID, "mobileNumber")  
    phone_input.send_keys("1234567890")

    confirm_button = driver.find_element(By.ID, "SaveAppointment")  
    confirm_button.click()

    


finally:
    # Close the browser after the test is complete
    driver.quit()
    print("Done")
