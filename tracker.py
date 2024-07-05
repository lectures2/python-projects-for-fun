import phonenumbers
from phonenumbers import timezone
from geopy.geocoders import Nominatim

def get_time_zone(phone_number):
    try:
        # Parse phone number
        parsed_number = phonenumbers.parse(phone_number)

        # Get time zone associated with the phone number
        time_zone = timezone.time_zones_for_number(parsed_number)

        return time_zone[0] if time_zone else None

    except phonenumbers.phonenumberutil.NumberParseException:
        print("Invalid phone number")

def get_city_info(address):
    try:
        # Create geocoder object
        geolocator = Nominatim(user_agent="geoapiExercises")

        # Geocode the address
        location = geolocator.geocode(address)

        # Get city information
        city = location.raw['address']['city']
        country = location.raw['address']['country']

        return city, country

    except (KeyError, AttributeError):
        print("Address information not available")

# Example usage
phone_number = "+14155552671"
time_zone = get_time_zone(phone_number)
print("Time zone:", time_zone)

address = "1600 Amphitheatre Parkway, Mountain View, CA"
city, country = get_city_info(address)
print("City:", city)
print("Country:", country)