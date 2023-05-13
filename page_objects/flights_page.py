from contextlib import suppress

from page_objects.checkout_page import CheckoutPage


class FlightsPage:
    def __init__(self, page):
        self.__page = page

    __one_stop_check_box = "//span[text()='Up to 1 stop']"
    __exclude_country_btn = "//div[text()='Exclude countries']"
    __search_country_btn = "//div[text()='Search countries']"
    __flights_cards = "[class^='ResultCardstyled__ResultCardMain']"
    __price_btn = "//div[text()='Share']//ancestor::div[contains(@class, 'ResultDetailstyled__Footer-')]" \
                  "/div[contains(@class, 'BookingWrapper')]"

    def select_one_stop_flights(self):
        self.__page.click(self.__one_stop_check_box)
        return self

    def exclude_country(self, country):
        self.__page.click(self.__exclude_country_btn)
        self.__page.click(self.__search_country_btn)
        self.__page.fill("//input[@placeholder='Search countries']", country)
        self.__page.click(f"//span[text()='{country}']")
        return self

    def select_first_flight(self):
        elements = self.__page.locator(self.__flights_cards)
        elements.first.click()
        return self

    def open_checkout_form(self):
        self.__page.click('//div[@data-test="DetailBookingButton"]')
        if self.__page.is_visible(self.__price_btn):
            self.__page.click(self.__price_btn)
        self.__page.click('//a[@data-test="MagicLogin-GuestTextLink"]')
        self.__page.wait_for_load_state()
        return CheckoutPage(self.__page)
