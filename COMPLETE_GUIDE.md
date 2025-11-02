# COMPLETE SETUP GUIDE FOR YOUR FRIEND

## What This Tool Does

This tool automatically locks ALL your Google Drive files so that people who view them CANNOT:
- Download the files
- Print the files  
- Copy/paste content from the files

**Important:** Owners and editors can still download. This only affects viewers and commenters.

---

## STEP 1: Get Google Cloud Credentials (10 minutes)

### 1.1 Create Google Cloud Project

1. Open browser and go to: **https://console.cloud.google.com/**
2. Sign in with your Google account
3. Click the dropdown at the top (says "Select a project")
4. Click **"NEW PROJECT"** button
5. Enter project name: `DriveLocker` (or any name)
6. Click **"CREATE"**
7. Wait 10 seconds for project to be created

### 1.2 Enable Google Drive API

1. In the left menu, click **"APIs & Services"** → **"Library"**
2. In the search box, type: `Google Drive API`
3. Click on **"Google Drive API"** from results
4. Click the blue **"ENABLE"** button
5. Wait for it to enable (takes 5 seconds)

### 1.3 Create API Key

1. In the left menu, click **"APIs & Services"** → **"Credentials"**
2. Click **"+ CREATE CREDENTIALS"** at the top
3. Select **"API key"**
4. A popup will show your API key
5. **COPY THIS KEY** - paste it somewhere safe (Notepad)
6. Click **"CLOSE"**

### 1.4 Configure OAuth Consent Screen

1. In the left menu, click **"OAuth consent screen"**
2. Select **"External"** (unless you have Google Workspace, then choose Internal)
3. Click **"CREATE"**
4. Fill in required fields:
   - **App name:** DriveLocker
   - **User support email:** Your email
   - **Developer contact:** Your email
5. Click **"SAVE AND CONTINUE"**
6. On "Scopes" page, click **"SAVE AND CONTINUE"** (don't add anything)
7. On "Test users" page:
   - Click **"+ ADD USERS"**
   - Enter your email address
   - Click **"ADD"**
8. Click **"SAVE AND CONTINUE"**
9. Click **"BACK TO DASHBOARD"**

### 1.5 Create OAuth Client ID

1. In the left menu, click **"Credentials"** again
2. Click **"+ CREATE CREDENTIALS"** → **"OAuth client ID"**
3. Application type: Select **"Web application"**
4. Name: `DriveLocker Web Client`
5. Under **"Authorized JavaScript origins"**, click **"+ ADD URI"**
   - Add: `http://localhost`
   - Click **"+ ADD URI"** again
   - Add: `http://localhost:8000`
   - Click **"+ ADD URI"** again  
   - Add: `http://127.0.0.1:8000`
6. Click **"CREATE"**
7. A popup shows your credentials
8. **COPY THE CLIENT ID** - paste it somewhere safe (Notepad)
9. Click **"OK"**

**You now have:**
- ✅ API Key (looks like: `AIzaSyAbc123...`)
- ✅ Client ID (looks like: `123456789-abc.apps.googleusercontent.com`)

---

## STEP 2: Setup the HTML File (2 minutes)

### 2.1 Download the File

Make sure you have the file: `drive-locker.html`

### 2.2 Edit the File

1. Right-click `drive-locker.html`
2. Open with **Notepad** or any text editor
3. Find these lines near the top (around line 370):

```javascript
const CLIENT_ID = 'YOUR_CLIENT_ID_HERE.apps.googleusercontent.com';
const API_KEY = 'YOUR_API_KEY_HERE';
```

4. Replace with YOUR credentials:

```javascript
const CLIENT_ID = '123456789-abc.apps.googleusercontent.com';  // Paste your Client ID
const API_KEY = 'AIzaSyAbc123def456ghi789jkl';  // Paste your API Key
```

5. **SAVE THE FILE** (Ctrl+S)

---

## STEP 3: Run the HTML File (1 minute)

**IMPORTANT:** You CANNOT just double-click the HTML file. You MUST run it through a local server.

### Option A: Using Python (Easiest)

1. Open **Command Prompt** (Windows) or **Terminal** (Mac/Linux)
2. Navigate to the folder with the HTML file:
   ```
   cd path\to\simple-drive-locker
   ```
3. Run this command:
   ```
   python -m http.server 8000
   ```
4. You should see: `Serving HTTP on 0.0.0.0 port 8000...`
5. Open your browser and go to: **http://localhost:8000/drive-locker.html**

### Option B: Using VS Code

1. Install VS Code if you don't have it
2. Install the "Live Server" extension
3. Right-click `drive-locker.html`
4. Click **"Open with Live Server"**

### Option C: Using Node.js

1. Open Command Prompt/Terminal
2. Navigate to the folder
3. Run:
   ```
   npx http-server -p 8000
   ```
4. Open browser: **http://localhost:8000/drive-locker.html**

---

## STEP 4: Use the Tool (2 minutes)

### 4.1 Connect to Google Drive

1. You should see the black and white interface
2. Click **"[+] Connect Google Drive"** button
3. A Google sign-in window will open
4. Sign in with your Google account
5. You'll see a warning: "Google hasn't verified this app"
   - Click **"Advanced"**
   - Click **"Go to DriveLocker (unsafe)"**
   - This is YOUR app, it's safe!
6. Review permissions and click **"Allow"**
7. The window will close
8. You should see: **"[OK] CONNECTED - Ready to lock files"**

### 4.2 Lock ALL Your Files

1. Click **"[LOCK] Lock ALL Files"** button
2. A confirmation popup appears: **"[WARNING] This will lock ALL files in your Drive. Continue?"**
3. Click **"OK"**
4. Watch the console output:
   ```
   [SCAN] Scanning Drive for files...
   [SCAN] Found 150 files so far...
   [SCAN] Scan complete! Total files: 150
   [1/150] [LOCK] Locking: Document.pdf
   [1/150] [OK] Locked successfully
   [2/150] [SKIP] Already locked: Spreadsheet.xlsx
   ...
   ```
5. Wait for it to complete (may take several minutes for many files)
6. When done, you'll see:
   ```
   [COMPLETE] Locked: 120 | Skipped: 25 | Failed: 5
   ```

### 4.3 Lock a Specific Folder (Optional)

1. Go to Google Drive in your browser
2. Open the folder you want to lock
3. Look at the URL: `https://drive.google.com/drive/folders/1a2b3c4d5e6f7g8h9i0j`
4. Copy the folder ID: `1a2b3c4d5e6f7g8h9i0j`
5. In the tool, click **"[FOLDER] Lock Folder"**
6. Paste the folder ID
7. Click **"[START] Start Locking Folder"**

### 4.4 View Statistics

1. Click **"[STATS] Show Statistics"**
2. You'll see:
   ```
   [STATS] Total Files: 150
   [STATS] Locked: 120
   [STATS] Unlocked: 30
   [STATS] Locked Percentage: 80%
   ```

### 4.5 Unlock Files (If Needed)

1. Click **"[UNLOCK] Unlock ALL Files"**
2. Confirm the action
3. All files will be unlocked (viewers can download again)

---

## TROUBLESHOOTING

### Problem: "Origin not allowed" error

**Solution:**
- Make sure you added `http://localhost:8000` to "Authorized JavaScript origins" in Google Cloud Console
- Make sure you're running through a server (not opening file directly)

### Problem: "Invalid API key" error

**Solution:**
- Check you copied the FULL API key (starts with `AIzaSy...`)
- Make sure you enabled Google Drive API in Google Cloud Console
- Try creating a new API key

### Problem: "Invalid Client ID" error

**Solution:**
- Check you copied the FULL Client ID (ends with `.apps.googleusercontent.com`)
- Make sure you created OAuth client ID (not just API key)

### Problem: Files not locking

**Reasons:**
- You don't own the file (you need edit/owner access)
- File is in a Shared Drive where you're not a Manager
- Some file types don't support this feature (rare)

**What to do:**
- Check the console output for specific errors
- Files you can't lock will show `[FAIL]` - this is normal
- The tool will continue with other files

### Problem: "Rate limit exceeded"

**Solution:**
- This is normal for large Drives (1000+ files)
- The tool automatically waits and retries
- Just let it run, it will complete eventually

### Problem: Tool is slow

**Explanation:**
- Google Drive API has rate limits
- The tool processes 10 files, then waits 1 second
- For 1000 files, expect 5-10 minutes
- This is normal and prevents errors

---

## WHAT HAPPENS AFTER LOCKING?

### For File Viewers:
- ❌ Cannot download files
- ❌ Cannot print files
- ❌ Cannot copy/paste content
- ✅ Can still view files online

### For File Editors/Owners:
- ✅ Can still do everything (download, print, copy)
- The lock only affects viewers and commenters

### Important Notes:
- **Screenshots:** People can still take screenshots (no way to prevent this)
- **Already Downloaded:** If someone downloaded before locking, they keep that copy
- **Offline Access:** If synced to Google Drive desktop app before locking, they keep offline access
- **Sharing:** You can still share files normally

---

## SECURITY & PRIVACY

### Is This Safe?

**YES!** Here's why:
- You created the app in YOUR Google Cloud account
- Only YOU can use it (you added yourself as test user)
- The code runs in YOUR browser (not on any server)
- No one else has access to your files

### What Permissions Does It Need?

- **Google Drive access:** To read file list and update lock settings
- **That's it!** It doesn't access file contents, Gmail, or anything else

### Can I Revoke Access?

**YES!** Anytime:
1. Go to: **https://myaccount.google.com/permissions**
2. Find "DriveLocker"
3. Click **"Remove Access"**

---

## FREQUENTLY ASKED QUESTIONS

### Q: Do I need to keep the tool open?

**A:** No. Once files are locked, they stay locked. You can close the browser.

### Q: Do I need to run this regularly?

**A:** Only if you add new files. Existing locked files stay locked forever (until you unlock them).

### Q: Can I lock files automatically when I upload them?

**A:** Not with this tool. You'd need to run it manually after uploading new files.

### Q: How do I unlock a single file?

**A:** Go to Google Drive → Right-click file → Share → Advanced → Uncheck "Disable options to download..."

### Q: Will this work on my phone?

**A:** No, this is a desktop-only tool. Use a computer.

### Q: Can I share this tool with friends?

**A:** Yes! They need to:
1. Create their own Google Cloud project
2. Get their own API Key and Client ID
3. Edit the HTML file with their credentials

### Q: Does this cost money?

**A:** No! Google Cloud is free for this usage (under 1 million API calls per day).

### Q: What if I have 10,000+ files?

**A:** It will work, but take 30-60 minutes. The tool handles rate limiting automatically.

---

## QUICK REFERENCE

### How to Get Folder ID:
1. Open folder in Drive
2. Look at URL: `https://drive.google.com/drive/folders/FOLDER_ID_HERE`
3. Copy the ID part

### How to Check if File is Locked:
1. Right-click file in Drive
2. Click "Share"
3. Click "Advanced" (bottom right)
4. Look for: "Disable options to download, print, and copy for commenters and viewers"
5. If checked = Locked ✅

### Console Output Meanings:
- `[OK]` = Success
- `[FAIL]` = Failed (usually permission issue)
- `[SKIP]` = Already in desired state
- `[LOCK]` = Currently locking
- `[UNLOCK]` = Currently unlocking

---

## NEED MORE HELP?

### Check These First:
1. Make sure Python/server is running
2. Make sure you're at `http://localhost:8000/drive-locker.html` (not `file:///...`)
3. Check browser console for errors (F12 → Console tab)
4. Make sure API Key and Client ID are correct

### Still Stuck?
- Re-read the setup steps carefully
- Try creating new credentials in Google Cloud Console
- Make sure Google Drive API is enabled
- Try a different browser (Chrome works best)

---

## SUMMARY CHECKLIST

Before using the tool, make sure you have:

- ✅ Created Google Cloud project
- ✅ Enabled Google Drive API
- ✅ Created API Key
- ✅ Created OAuth Client ID
- ✅ Added authorized JavaScript origins
- ✅ Edited HTML file with your credentials
- ✅ Running through a local server (not double-clicking)
- ✅ Connected to Google Drive in the tool

If all checked, you're ready to lock files!

---

**That's everything your friend needs to know!** 🎉

The tool is simple: Connect → Click Lock → Done!
