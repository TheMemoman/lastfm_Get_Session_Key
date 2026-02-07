import time
import pylast

API_KEY = "XXXXXXXXXXXXXXX"
API_SECRET = "XXXXXXXXXXXX"
# Create a network object without a session key
network = pylast.LastFMNetwork(
    api_key=API_KEY,
    api_secret=API_SECRET
)

# Create the generator
skg = pylast.SessionKeyGenerator(network)

# 1) Get the URL for the user to visit
url = skg.get_web_auth_url()

print("Open this URL in your browser and authorize the app:")
print(url)

# Give the user some time
input("After you've authorized, press Enter here...")

# 2) Try to get the session key
session_key = skg.get_web_auth_session_key(url)

print("\nYour Last.fm SESSION KEY is:\n")
print(session_key)
print("\nKeep it secret! You can now paste it into your script.")
