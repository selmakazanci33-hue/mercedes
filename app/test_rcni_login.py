import os
from dotenv import load_dotenv
from pages.login_page import LoginPage
import pytest

from utils.issuer_report_utils import (
    capture_issuer_screenshots,
    extract_report_rows,
    build_issuer_html_report
)

load_dotenv()

ISSUERS = [
    "82824", "83761", "70893", "45334", "49046",
    "83502", "60224", "15105", "86637", "68806",
    "64357", "37301", "37001", "89942", "58081",
    "13535", "43802"
]


@pytest.fixture(autouse=True)
def screenshot_on_failure(request, page):
    yield

    rep = getattr(request.node, "rep_call", None)

    if rep and rep.failed:
        os.makedirs("assets/failures", exist_ok=True)
        shot = f"assets/failures/{request.node.name}.png"
        page.screenshot(path=shot, full_page=True)
        print(f"\n[FINAL TEST FAILURE SCREENSHOT SAVED] → {shot}")


def pytest_runtest_makereport(item, call):
    setattr(item, "rep_" + call.when, call)


def test_rcni_dynamic(page):
    issuer_results = []

    print(os.getenv("GA_URL"))

    login = LoginPage(page)
    login.goto()
    login.login(os.getenv("GA_EMAIL"), os.getenv("GA_PASSWORD"))

    page.get_by_test_id("Enrollment").click()

    rcni_link = page.get_by_role("link", name="Reconciliation Workbench End")
    rcni_link.wait_for(state="visible", timeout=120000)
    rcni_link.click()

    page.wait_for_selector('[data-testid="reconciliationMonth"]', timeout=120000)
    page.wait_for_selector('[data-testid="issuerName"]', timeout=120000)
    page.wait_for_selector('[data-testid="reconciliationYear"]', timeout=120000)

    for issuer in ISSUERS:
        print(f"\n=== Processing Issuer {issuer} ===")

        issuer_dir = f"assets/issuers/{issuer}"
        os.makedirs(issuer_dir, exist_ok=True)

        issuer_result = {
            "issuer": issuer,
            "issuer_name": issuer,
            "screenshots": {},
            "report_rows": [],
            "no_report": False
        }

        try:
            month = page.get_by_test_id("reconciliationMonth")
            month.wait_for(state="visible", timeout=20000)

            try:
                month.select_option("6")
            except Exception:
                month.click()
                page.get_by_role("option", name="June").click()

            page.wait_for_timeout(700)

            issuer_dd = page.get_by_test_id("issuerName")

            try:
                issuer_dd.select_option(issuer)
            except Exception:
                issuer_dd.click()
                page.get_by_role("option", name=issuer).click()

            page.wait_for_timeout(700)

            try:
                issuer_name = issuer_dd.evaluate("""
                    el => el.options
                        ? el.options[el.selectedIndex].textContent.trim()
                        : el.innerText.trim()
                """)
            except Exception:
                issuer_name = issuer

            issuer_result["issuer_name"] = issuer_name

            year = page.get_by_test_id("reconciliationYear")

            try:
                year.select_option("2026")
            except Exception:
                year.click()
                page.get_by_role("option", name="2026").click()

            page.wait_for_timeout(700)

            page.get_by_test_id("reconciliationGoButton").click()

            try:
                page.get_by_text("TOP 5 DISCREPANCIES").wait_for(
                    state="visible",
                    timeout=60000
                )
            except Exception:
                pass

            try:
                page.get_by_text("Issuer Activity").last.wait_for(
                    state="visible",
                    timeout=60000
                )
            except Exception:
                pass

            page.wait_for_timeout(7000)

            issuer_result["report_rows"] = extract_report_rows(page)

            if not issuer_result["report_rows"]:
                issuer_result["no_report"] = True
                print(f"No report rows captured for issuer {issuer}.")
            else:
                print(
                    f"Rows captured for issuer {issuer}: "
                    f"{len(issuer_result['report_rows'])}"
                )

            issuer_result["screenshots"] = capture_issuer_screenshots(
                page,
                issuer_dir
            )

            issuer_results.append(issuer_result)

        except Exception as e:
            fail_shot = f"{issuer_dir}/failure.png"
            page.screenshot(path=fail_shot, full_page=True)

            issuer_result["screenshots"]["Failure Screenshot"] = fail_shot
            issuer_result["report_rows"].append({
                "file_name": "",
                "received_date": "",
                "status": "FAILED",
                "in_file": "",
                "in_hix": "",
                "success": "",
                "discrepancies": "",
                "errors": "",
                "total_discrepancies": "",
                "report_name": str(e),
                "report_date": ""
            })

            issuer_results.append(issuer_result)

            print(f"[ISSUER FAILED] {issuer} → {fail_shot}")
            raise e

        finally:
            _return_to_rcni(page)

    build_issuer_html_report(issuer_results, "IssuerTeam.html")

    print("\n=== ALL ISSUERS COMPLETE ===")
    print("HTML report created: IssuerTeam.html")


def _return_to_rcni(page):
    try:
        page.get_by_test_id("Enrollment").click()

        rcni_link = page.get_by_role("link", name="Reconciliation Workbench End")
        rcni_link.wait_for(state="visible", timeout=120000)
        rcni_link.click()

        page.wait_for_selector('[data-testid="issuerName"]', timeout=120000)

    except Exception:
        pass
