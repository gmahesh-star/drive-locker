# HTML Version Setup Guide

Super simple setup for the HTML version!

## Step 1: Get Google API Credentials

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable **Google Drive API**
4. Go to "Credentials" → "Create Credentials"

### Create API Key:
1. Click "Create Credentials" → "API Key"
2. Copy the API key

### Create OAuth Client ID:
1. Click "Create Credentials" → "OAuth client ID"
2. Configure consent screen if needed
3. Application type: **Web application**
4. Add authorized JavaScript origins:
   - `http://localhost`
   - `http://localhost:8000`
   - `http://127.0.0.1`
   - `http://127.0.0.1:8000`
5. Copy the Client ID

## Step 2: Configure the HTML File

Open `drive-locker.html` and replace:

```javascript
const CLIENT_ID = 'YOUR_CLIENT_ID_HERE.apps.googleusercontent.com';
const API_KEY = 'YOUR_API_KEY_HERE';
```

With your actual credentials:

```javascript
const CLIENT_ID = '123456789-abcdefg.apps.googleusercontent.com';
const API_KEY = 'AIzaSyAbc123def456ghi789jkl';
```

## Step 3: Run the HTML File

You MUST run it through a local server (not just double-click):

### Option 1: Python (Easiest)
```bash
# Python 3
python -m http.server 8000

# Then open: http://localhost:8000/drive-locker.html
```

### Option 2: Node.js
```bash
npx http-server -p 8000

# Then open: http://localhost:8000/drive-locker.html
```

### Option 3: VS Code
1. Install "Live Server" extension
2. Right-click `drive-locker.html`
3. Click "Open with Live Server"

## Step 4: Use It!

1. Click "🔑 Connect Google Drive"
2. Sign in and allow permissions
3. Click "🔒 Lock ALL Files" or choose other options
4. Watch the terminal-style console!

## Features

✅ **Lock ALL files** - One click to lock everything  
✅ **Lock specific folder** - Enter folder ID  
✅ **Unlock files** - Reverse the operation  
✅ **Statistics** - See how many files are locked  
✅ **Terminal style** - Cool green-on-black console  
✅ **Progress tracking** - Real-time updates  
✅ **No backend needed** - Pure HTML + JavaScript  

## Troubleshooting

### "Origin not allowed" error
- Make sure you added `http://localhost:8000` to authorized origins
- Must run through a server, not file://

### "API key not valid"
- Check you copied the full API key
- Make sure Drive API is enabled

### Files not locking
- You need edit/owner access to files
- Some file types can't be locked
- Check console for specific errors

## That's It!

No Python, no Node.js server, no database - just one HTML file! 🎉
