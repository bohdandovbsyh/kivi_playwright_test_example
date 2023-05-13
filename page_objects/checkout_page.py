class CheckoutPage:
    def __init__(self, page):
        self.__page = page

    def set_passenger_data(self, email, phone_number, first_name, last_name, nationality, gender, birth_day,
                           birth_month, birth_year, id_number, is_id_has_expiration=False):
        self.__page.fill("[type='email']", email)
        self.__page.fill("[name='phone']", phone_number)
        self.__page.fill('[name="firstname"]', first_name)
        self.__page.fill('[name="lastname"]', last_name)
        self.__page.select_option('[data-test="ReservationPassenger-nationality"]', label=nationality)
        self.__page.select_option('[class^="PassengerForm__Gender"] select', label=gender)
        self.__page.fill('[name="birthDay"]', birth_day)
        self.__page.select_option('[name="birthMonth"]', label=birth_month)
        self.__page.fill('[name="birthYear"]', birth_year)
        self.__page.fill('[name="idNumber"]', id_number)
        if not is_id_has_expiration:
            self.__page.click("//span[text()='No expiration']")
        else:
            # TODO implement setting id expiration data
            pass
        return self

    def click_continue_btn(self):
        self.__page.click('[data-test="StepControls-passengers-next"]')
        # TODO implement next page
        return self
