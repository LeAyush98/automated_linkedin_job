from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from automate import Automate
from dotenv import load_dotenv
import os

# Loading my credentials from secure .env file
load_dotenv(".env")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

gomez = webdriver.Chrome() # download chrome webdriver and pass its PATH here or add it in your environment variables

gomez.get(url="https://www.linkedin.com/")
gomez.maximize_window()

bot = Automate(email = EMAIL, password = PASSWORD) # Please add your username and password, it is safer to keep them as environment variables
bot.wait_long()

def get_objects_phase_one():

    email_input = gomez.find_element(By.ID, f"{bot.USERNAME_ID}")
    password_input = gomez.find_element(By.ID, f"{bot.PASSWORD_ID}")
    post_objects_phase_one(email_input, password_input)

def post_objects_phase_one(email_input, password_input):

    email_input.send_keys(f"{bot.email}")
    password_input.send_keys(f"{bot.password}")

get_objects_phase_one()

submit_key = gomez.find_element(By.CSS_SELECTOR, f"button.{bot.SIGN_IN_ID_CLASS}")
submit_key.click()

gomez.maximize_window()

bot.wait_long()
search_bar = gomez.find_element(By.CSS_SELECTOR, f"input.{bot.SEARCH_CLASS}")
search_bar.send_keys("Python Developer")
search_bar.send_keys(Keys.ENTER)

bot.wait_long()
expand_jobs = gomez.find_element(By.XPATH, f"{bot.EXPAND_JOBS_XPATH}")
expand_jobs.click()

bot.wait_long()
easy_job = gomez.find_element(By.XPATH, f"{bot.EASY_APPLY_XPATH}")
easy_job.click()

bot.wait_long()
job_title_list = gomez.find_elements(By.CSS_SELECTOR, f"div.{bot.JOBS_LIST_CLASS}")

def scroll_to_submit():
    for _ in range(8):
        easy_apply.send_keys(Keys.ARROW_DOWN)

def apply_logic():
    already_done = False
    first_next = gomez.find_element(By.XPATH, f"{bot.NEXT_BUTTON_XPATH}") 
    
    try:
        alter_submit = gomez.find_element(By.XPATH, f"{bot.ALTER_SUBMIT_APP_XPATH}")
    except NoSuchElementException:
        pass   
    if first_next.find_element(By.TAG_NAME, "span").text == "Next":
        first_next.click()   
    
    
    elif alter_submit.find_element(By.TAG_NAME, "span").text == "Submit application":
            scroll_to_submit()
            bot.wait_short()
            alter_submit.click()
            already_done = True
    
    if not already_done:
        bot.wait_short()
        choose = gomez.find_element(By.XPATH, f"{bot.CHOOSE_BUTTON_XPATH}")
        choose.click()
        bot.wait_short()

        second_next = gomez.find_element(By.XPATH, f"{bot.NEXT_AGAIN_XPATH}")
        if second_next.find_element(By.TAG_NAME, "span").text == "Next":
            second_next.click()     
        
        bot.wait_short()
        pain = gomez.find_element(By.XPATH, f"{bot.PAIN}")
        if pain.is_displayed():
            close = gomez.find_element(By.XPATH, f"{bot.CLOSE_BUTTON_XPATH}")
            close.click()
            bot.wait_short()
            discard = gomez.find_element(By.XPATH, f"{bot.DISCARD_BUTTON_XPATH}")
            discard.click()

        else:
            if second_next.find_element(By.TAG_NAME, "span").text == "Review":
                second_next.click()
                scroll_to_submit()
                bot.wait_short()
                submit = gomez.find_element(By.XPATH, f"{bot.SUBMIT_APPLICATION_XPATH}")
                submit.click()
        

for job in job_title_list:
    bot.wait_long()
    job.click()
    bot.wait_short()
    easy_apply = gomez.find_element(By.CSS_SELECTOR, f"div.{bot.FINAL_EASY_APPLY_CLASS}")
    easy_apply.click()
    bot.wait_long()
    apply_logic()

while True:
    pass