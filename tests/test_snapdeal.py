import logging
import pytest

from base_test import setup_class
from base_test import setup_method

EXPECTED_TITLE = 'Shop Online for Men, Women & Kids Clothing, Shoes, Home Decor Items'


@pytest.mark.usefixtures("setup_class")
class TestSnapDealTitle:
    def test_snap_deal_title(self, setup_method):
        try:
            # Test method to navigate to Snapdeal and check the title
            self.driver.get("https://www.snapdeal.com")
            logging.info("Actual Title of snapdeal.com : %s", self.driver.title)
            logging.info("Expected Title of snapdeal.com : %s", EXPECTED_TITLE)
            logging.info("test_snap_deal_title %s", str(self.driver.title + "..." in EXPECTED_TITLE))
            assert self.driver.title + "..." == EXPECTED_TITLE
        except AssertionError as ae:
            logging.info("Exception: %s", ae.__str__())
            raise ae  # Re-raise the AssertionError to mark the test as failed
        except Exception as e:
            raise AssertionError(f"Test failed due to exception: {e}")

    @pytest.mark.skip(reason="Skipping this test as it is duplicate")
    def test_snap_deal_title_2(self, setup_method):
        try:
            # Test method to navigate to Snapdeal and check the title
            self.driver.get("https://www.snapdeal.com")
            logging.info("Actual Title of snapdeal.com : %s", self.driver.title)
            logging.info("Expected Title of snapdeal.com : %s", EXPECTED_TITLE)
            logging.info("test_snap_deal_title_2 %s", str(self.driver.title + "..." in EXPECTED_TITLE))
            assert self.driver.title + "..." == EXPECTED_TITLE
        except AssertionError as ae:
            logging.info("Exception: %s", ae.__str__())
            raise ae  # Re-raise the AssertionError to mark the test as failed
        except Exception as e:
            raise AssertionError(f"Test failed due to exception: {e}")