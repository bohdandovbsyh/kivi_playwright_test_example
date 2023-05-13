from page_objects.flights_page import FlightsPage


class MainPage:
    def __init__(self, page):
        self.__page = page

    __accept_cookies_btn = "#cookies_accept"
    __booking_checkbox = '[class^="BookingcomSwitchstyled__S"]'
    __default_destination_re_btn = '//*[@data-test="PlacePickerInputPlace-close"]'
    __search_btn = '//div[text()="Search"]'

    def click_accept_cookies(self):
        if self.__page.is_visible(self.__accept_cookies_btn, timeout=2000):
            self.__page.click(self.__accept_cookies_btn)
        return self

    def click_booking_checkbox(self):
        if self.__page.is_visible(self.__booking_checkbox, timeout=2000):
            self.__page.click(self.__booking_checkbox)
        return self

    def remove_default_destination(self):
        self.__page.click(self.__default_destination_re_btn)

    def select_departure_city(self, city, country):
        self.__page.fill('//*[@data-test="SearchPlaceField-origin"]//*[@data-test="SearchField-input"]', city)
        self.__page.click(f'//div[text()="{city}, {country}"]')
        return self

    def select_arrival_city(self, city, country):
        self.__page.fill('//*[@data-test="SearchPlaceField-destination"]//*[@data-test="SearchField-input"]', city)
        self.__page.click(f"//div[text()='{city}, {country}']")
        return self

    def select_departure_and_return_dates(self, departure_date, return_date):
        self.__page.click('//div[text()="Departure"]')
        # can be implemented in proper way to search directly month you want
        self.__page.click('//*[@data-test="CalendarMoveNextButton"]')
        self.__page.click('//*[@data-test="CalendarMoveNextButton"]')
        self.__page.click(f'//div[@data-value="{departure_date}"]')
        self.__page.click(f'//div[@data-value="{return_date}"]')
        self.__page.click('//button[@data-test="SearchFormDoneButton"]')
        return self

    def click_search_btn(self):
        self.__page.click(self.__search_btn)
        self.__page.wait_for_load_state()
        return FlightsPage(self.__page)
