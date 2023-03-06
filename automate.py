import time

class Automate:
    USERNAME_ID = "session_key"
    PASSWORD_ID = "session_password"
    SIGN_IN_ID_CLASS = "sign-in-form__submit-btn--full-width"
    SEARCH_CLASS = "search-global-typeahead__input"
    EXPAND_JOBS_XPATH = "/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[1]/div/div[2]"
    EASY_APPLY_XPATH = "/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[8]/div/button"
    JOBS_LIST_CLASS = "artdeco-entity-lockup__title"
    FINAL_EASY_APPLY_CLASS = "jobs-apply-button--top-card"
    NEXT_BUTTON_XPATH = "/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button"
    CHOOSE_BUTTON_XPATH = "/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/div/div[1]/div/div/div/div[2]/button[1]"
    NEXT_AGAIN_XPATH = "/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]"
    PAIN = "/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/h3"
    CLOSE_BUTTON_XPATH = "/html/body/div[3]/div/div/button"
    DISCARD_BUTTON_XPATH = "/html/body/div[3]/div[2]/div/div[3]/button[1]"
    REVIEW_BUTTON_XPATH = "/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]"
    SUBMIT_APPLICATION_XPATH = "/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[3]/button[2]"
    ALTER_SUBMIT_APP_XPATH = "/html/body/div[3]/div/div/div[2]/div/div/form/footer/div[3]/button"

    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password

    @staticmethod
    def wait_long():
        time.sleep(4)

    @staticmethod
    def wait_short():
        time.sleep(2)

    def __str__(self) -> None:
        print(f"Email is {self.email} and password is *********, Will not leak the password lol")