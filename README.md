# lastfm_Get_Session_Key

A small Python utility to generate a **Last.fm session key** using the official web authentication flow.

This script is intended as a **one-time setup helper** for applications or scripts that interact with the Last.fm API and require authenticated user actions (such as loving tracks).

## Description

This script walks you through the Last.fm authentication process and retrieves a **session key** tied to your Last.fm account.

It uses the `pylast` library to:
- Create a temporary authentication request
- Generate a browser authorization URL
- Wait for you to approve the application on Last.fm
- Retrieve and print your personal **session key**

The session key can then be copied and reused in other scripts without repeating the authentication process.

Others scripts for mine that use the session key are:
- [Navidrome_Scrobbles_to_LastFM](https://github.com/TheMemoman/Navidrome_scrobbles_to_Lastfm)
- [Navidrome_love_to_LastFM](https://github.com/TheMemoman/Navidrome_love_to_Lastfm)

## How It Works

1. **Create an Unauthenticated Network**  
   The script initializes a `LastFMNetwork` using only your API key and API secret (no session key yet).

2. **Generate Authorization URL**  
   A web authentication URL is generated and printed to the terminal. This URL must be opened in your browser so you can authorize the application on Last.fm.

3. **User Authorization**  
   You log into Last.fm (if needed) and approve the app’s access to your account.

4. **Retrieve Session Key**  
   After authorization, the script retrieves your session key and prints it to the console.  
   This key can be reused indefinitely unless revoked.

## Configure the following variables

| Name         | Description                          | Suggested Value    |
|--------------|--------------------------------------|--------------------|
| `API_KEY`    | Your Last.fm API key                 | `xxxxxxxxxxxxxxxx` |
| `API_SECRET` | Your Last.fm API secret              | `xxxxxxxxxxxxxxxx` |

You can obtain an API key and secret from the  
[Last.fm API authentication page](https://www.last.fm/api/authentication)

## Execute the script

### 1. Create a virtual environment and install `pylast`

```bash
python3 -m venv ~/lastfm_auth_venv
source ~/lastfm_auth_venv/bin/activate
pip install --upgrade pip
pip install pylast/activate
```

### 2. Run the script

```bash
python get_session_key.py
```

### 3. Follow the prompts

1. Open the printed URL in your browser
2. Authorize the application on Last.fm
3. Return to the terminal and press Enter
4. The script will then print your SESSION KEY.

Output Example
```
Open this URL in your browser and authorize the app:
https://www.last.fm/api/auth/?api_key=...

After you've authorized, press Enter here...

Your Last.fm SESSION KEY is:

xxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Keep it secret! You can now paste it into your script.
```

### 4. Notes & Security

🔐 Keep your session key private — it grants access to your Last.fm account

✅ This script only needs to be run once

❌ If you revoke access on Last.fm, you’ll need to generate a new session key

### 5. Alternative way via console commands of getting your session key

You can find a console command tutorial on [this reddit comment](https://www.reddit.com/r/navidrome/comments/1qdarg6/comment/o2f626i/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button).
