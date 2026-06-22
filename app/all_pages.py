class RCNILocators:

    # ----- Navigation -----
    enrollment_menu = "data-testid=Enrollment"
    reconciliation_link = ("role=link[name='Reconciliation Workbench End']")

    # ----- Filters -----
    issuer_dropdown = "data-testid=issuerName"
    month_dropdown = "data-testid=reconciliationMonth"
    year_dropdown = "data-testid=reconciliationYear"
    go_button = "data-testid=reconciliationGoButton"

    # ----- Table headings -----
    heading_file_name = "data-testid=table-heading-0"
    heading_report_name = "data-testid=table-heading-9"
    heading_status = "data-testid=table-heading-2"

    # ----- Rows -----
    first_row = "data-testid=table-row-0-cell-9"

    # ----- Chart buttons -----
    chart_main = ".css-15rufqy"
    chart_second = ".css-h1sary"
    chart_third = "div:nth-child(3) > .css-15rufqy"

    # ----- Status label pattern -----
    # Example: f"{issuer_name} - JUNE - Status"
    status_label = "{} - June - Status"



import os
from playwright.sync_api import Page, expect
from pages.rcni_locators import RCNILocators as L
from dotenv import load_dotenv

load_dotenv()

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto(os.getenv("GA_URL"))
        self.page.get_by_role("textbox", name="Email Address") \
            .wait_for(state="visible", timeout=60000)

    def login(self, email, password):
        self.page.get_by_role("textbox", name="Email Address").fill(email)
        self.page.get_by_role("textbox", name="Password").fill(password)
        self.page.get_by_role("button", name="Login").click()

        # Slow redirect
        # self.page.wait_for_load_state("networkidle", timeout=120000)

        # Login success indicator
        self.page.get_by_test_id("Enrollment") \
            .wait_for(state="visible", timeout=120000)
        expect(self.page.get_by_test_id("Enrollment")).to_be_visible()


class LoginLocators:
    email_input = ("role= textbox[name='Email Address']")
    password_input = ("role= textbox[name='Password']")
    login_button = ("role= button[name='Login']")
    enrollment_menu = "data-testid=Enrollment"
