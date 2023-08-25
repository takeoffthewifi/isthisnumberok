# Made by github.com/takeoffthewifi & This program use the API : https://api-ninjas.com/api/validatephone
import requests

number = '+12065550100'
api_url = 'https://api.api-ninjas.com/v1/validatephone?number={}'.format(number)
response = requests.get(api_url, headers={'X-Api-Key': 'YOUR-API-KEY'})

# ASCII art
ascii_art = r"""
  _____  _______ _     _     _   _                 _                ____  _  _____  
 |_   _||__   __| |   (_)   | \ | |               | |              / __ \| |/ /__ \ 
   | |  ___| |  | |__  _ ___|  \| |_   _ _ __ ___ | |__   ___ _ __| |  | | ' /   ) |
   | | / __| |  | '_ \| / __| . ` | | | | '_ ` _ \| '_ \ / _ \ '__| |  | |  <   / / 
  _| |_\__ \ |  | | | | \__ \ |\  | |_| | | | | | | |_) |  __/ |  | |__| | . \ |_|  
 |_____|___/_|  |_| |_|_|___/_| \_|\__,_|_| |_| |_|_.__/ \___|_|   \____/|_|\_\(_)  
                                                                                    
"""
print(ascii_art)

print()
print("A simple Python program that checks the validity of a phone number. github.com/takeoffthewifi. & https://api-ninjas.com/ ")
print()

numberphone = input("Enter the phone number to check: ")

if response.status_code == requests.codes.ok:
    api_response = response.json()  # Parse the JSON response

    # Extract information from the API response
    is_valid = api_response["is_valid"]
    is_formatted_properly = api_response["is_formatted_properly"]
    country = api_response["country"]
    location = api_response["location"]
    timezones = ", ".join(api_response["timezones"])
    format_national = api_response["format_national"]
    format_international = api_response["format_international"]
    format_e164 = api_response["format_e164"]
    country_code = api_response["country_code"]

    # Create a list of all number phone information 
    info_list = [
        f"✅ Valid Number: {is_valid}",
        f"📞 Formatted Properly: {is_formatted_properly}",
        f"🌎 Country: {country}",
        f"📍 Location: {location}",
        f"🕒 Timezones: {timezones}",
        f"📞 National Format: {format_national}",
        f"🌐 International Format: {format_international}",
        f"📞 E164 Format: {format_e164}",
        f"🌍 Country Code: {country_code}"
    ]

    # Print the formatted information
    print("\n".join(info_list))
else:
    print("Error:", response.status_code, response.text)
