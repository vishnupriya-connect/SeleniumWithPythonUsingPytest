import logging
import time
import pytest

from base_test import setup_class
from base_test import setup_method

EXPECTED_TITLE = 'Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in'


@pytest.mark.usefixtures("setup_class")
class TestAmazonTitle:
    def test_amazon_title(self, setup_method):
        try:
            # Test method to navigate to Amazon and check the title
            self.driver.get("https://www.amazon.in")
            time.sleep(2)
            logging.info("Actual Title of amazon.in : %s", self.driver.title)
            logging.info("Expected Title of amazon.in : %s", EXPECTED_TITLE)
            logging.info("test_amazon_title %s", str(self.driver.title in EXPECTED_TITLE))
            assert self.driver.title == EXPECTED_TITLE
        except AssertionError as ae:
            logging.info("Exception: %s", ae.__str__())
            raise ae  # Re-raise the AssertionError to mark the test as failed
        except Exception as e:
            raise AssertionError(f"Test failed due to exception: {e}")

    @pytest.mark.skip(reason="Skipping test_amazon_title_com test as it is duplicate")
    def test_amazon_title_com(self, setup_method):
        try:
            # logging.info("Skipped: %s", pytest.mark.skip.reason)
            # Test method to navigate to Amazon and check the title
            self.driver.get("https://www.amazon.in")
            logging.info("Actual Title of amazon.in : %s", self.driver.title)
            logging.info("Expected Title of amazon.in : %s", EXPECTED_TITLE)
            logging.info("test_amazon_title %s", str(self.driver.title in EXPECTED_TITLE))
            assert self.driver.title + "..." == EXPECTED_TITLE
        except AssertionError as ae:
            logging.info("Exception: %s", ae.__str__())
            raise ae  # Re-raise the AssertionError to mark the test as failed
        except Exception as e:
            raise AssertionError(f"Test failed due to exception: {e}")
