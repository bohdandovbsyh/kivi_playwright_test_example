from playwright.sync_api import expect

from page_objects.main_page import MainPage


def test_search_flight_and_checkout(open_page):
    """
    # Test steps:
        1. Open the website www.kiwi.com.
            1.1 Select a flight from New York to Barcelona.
            1.2 Set the departure date as 1st of July 2023
            1.3 Set the return date as 15th of July 2023
            1.4 Set the number of passengers as 2.
        2. Click on the search button and wait for the search results to load.
        3. Select the filter option to only display flights with 1 stop and excludes United Kingdom
        4. Select any flight from the displayed list of search results.
        5. Verify that the selected flight has 1 stop.
        6. Click on the “Select” button to proceed to the check-out form page
        7. Select continue as guest
            7.1 Complete the required fields on the check-out form page:
            7.2 Enter email address.
            7.3 Enter phone number.
            7.4 Enter Name and Surname
            7.5 Select a nationality from the provided options.
            7.6 Select gender.
            7.7 Enter Date of birth.
            7.8 Enter Passport number.
        8. Click on Remove traveler
        9. Click Continue button
    """
    # Define variables for flight details
    departure_date = "2023-07-01"
    return_date = "2023-07-15"
    country_to_exclude = "United Kingdom"

    # Launch the browser and open the website
    page = open_page
    main_page = MainPage(page)

    # Search for a flight
    main_page.click_accept_cookies().click_booking_checkbox().remove_default_destination()
    main_page.select_departure_city(city='New York', country='United States')
    main_page.select_arrival_city(city='Barcelona', country='Spain')
    main_page.select_departure_and_return_dates(departure_date, return_date)
    flights_page = main_page.click_search_btn()

    # Filter the search results
    flights_page.select_one_stop_flights().exclude_country(country_to_exclude)

    # Select a flight from the search results
    flights_page.select_first_flight()

    # Verify that the selected flight has 1 stop
    expect(page.locator('//li[@data-test="ItineraryLayoverInfoItem"]')).to_have_count(2)

    # Proceed to the check-out form page
    checkout_page = flights_page.open_checkout_form()

    # Fill out the check-out form
    checkout_page.set_passenger_data(email="test@test.com", phone_number="095454545",
                                     first_name="John", last_name="Doe",
                                     nationality="United Kingdom", gender="Male",
                                     birth_day='05', birth_month='January',
                                     birth_year='1995', id_number="ABC123", )
    # Click continue
    checkout_page.click_continue_btn()
