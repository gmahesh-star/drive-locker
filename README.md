# Google Drive File Locker 🔒

**Live Web App:** https://drive-locker.vercel.app

A beautiful, easy-to-use web application to lock your Google Drive files and prevent viewers from downloading, copying, or printing them. No installation required - just open the link and start protecting your files!

## ✨ Features

- 🌐 **Web-Based** - No installation, works in any browser
- 📱 **Mobile Responsive** - Works perfectly on phones, tablets, and desktops
- 🗂️ **Visual Folder Browser** - Navigate through folders like Windows Explorer
- 🔒 **Lock & Share** - Lock files and share with specific people in one click
- 📧 **Email Notifications** - Recipients get notified when folders are shared
- 💝 **Personalized** - Made with love for Purnendu by Mahesh
- ⚡ **Fast & Secure** - Direct connection to Google Drive API

## 🚀 Quick Start (Web App)

1. **Open:** https://drive-locker.vercel.app
2. **Click:** "Connect Google Drive"
3. **Sign in** with your Google account
4. **Browse** your folders and lock files!

That's it! No installation, no setup, no configuration needed.

---

## 🎯 How to Use

### Step 1: Connect to Google Drive

1. Open https://drive-locker.vercel.app
2. Wait for the personalized splash screen ("From Mahesh TO: PURNENDU ♥")
3. Click **"[+] Connect Google Drive"**
4. Sign in and grant permissions
5. You'll see **"[OK] CONNECTED - Ready to lock files"**

### Step 2: Browse Your Folders

1. Click **"[BROWSE] Browse Folders & Lock Files"**
2. You'll see all your folders in "My Drive"
3. Click on any folder to open it
4. Navigate through subfolders by clicking on them
5. See the breadcrumb trail: `My Drive > College Notes > Semester 1`

### Step 3: Lock Files

**Option A: Lock Without Sharing**
1. Navigate to the folder you want to lock
2. Click **"[LOCK] Lock Files Here"**
3. Choose if you want to include subfolders
4. Confirm and watch the progress!

**Option B: Lock & Share with People**
1. Navigate to the folder
2. Click **"[LOCK & SHARE] Lock & Share with People"**
3. Enter email addresses (one per line):
   ```
   friend1@gmail.com
   friend2@gmail.com
   teacher@school.com
   ```
4. OR check "Anyone with the link" for public sharing
5. Click **"[LOCK & SHARE] This Folder Only"** or **"Include Subfolders"**
6. Done! Recipients get ONE email with folder access

### Step 4: View Progress

Watch the console output in real-time:
```
[START] Locking folder: College Notes
[STEP 1] Locking all files...
[1/25] [LOCK] COA-Mod-1.pdf
[1/25] [OK] Locked
[2/25] [LOCK] Data Structures.pdf
[2/25] [OK] Locked
...
[STEP 2] Sharing folder with recipients...
[SHARE] Sent email to: friend@gmail.com
[SHARE] Folder shared successfully!
[COMPLETE] Locked: 25 | Failed: 0
```

---

## 📱 Mobile Features

The app is fully optimized for mobile devices:

- ✅ **Touch-friendly buttons** (48px minimum height)
- ✅ **Responsive layout** adapts to screen size
- ✅ **No horizontal scrolling** - everything fits perfectly
- ✅ **Large text** for easy reading
- ✅ **Tap feedback** - buttons respond to touch
- ✅ **Mobile keyboard** optimized for email input

Works great on:
- 📱 iPhone & Android phones
- 📱 iPads & Android tablets
- 💻 Laptops & Desktops
- 🖥️ Large monitors

---

## 🎨 What Makes It Special

### Personalized Experience
- Beautiful splash screen: "From Mahesh TO: PURNENDU ♥"
- Custom loading messages: "Mahesh's tool is working hard for Purnendu"
- Made specifically for Purnendu by his childhood friend Mahesh

### Smart Folder Browser
- Navigate folders like Windows Explorer
- See file counts in each folder
- Breadcrumb navigation to go back easily
- Shows both folders and files clearly

### Lock & Share Feature
- Lock files AND share them in one operation
- Share with specific people via email
- OR share as "Anyone with the link"
- Recipients get ONE email (not one per file!)
- Automatic viewer permissions (can't download)

---

## 🔐 Security & Privacy

- ✅ **Direct connection** to Google Drive API (no middleman)
- ✅ **No data stored** on our servers
- ✅ **OAuth 2.0** authentication (industry standard)
- ✅ **HTTPS only** (secure connection)
- ✅ **Open source** - you can review the code

### What Gets Locked?

✅ **Prevents:**
- Downloading files via Drive UI
- Printing documents
- Copying/pasting content
- Downloading from Drive mobile app

❌ **Cannot Prevent:**
- Screenshots or photos of screen
- Owner/editor downloads (they always can)
- Files already downloaded before locking

---

## 📊 Statistics

Click **"[STATS] Show Statistics"** to see:
- Total files in your Drive
- How many are locked
- How many are unlocked
- Lock percentage

---

## 🐍 Python Script (Alternative)

Prefer command line? We also have a Python script version.

### Quick Setup (5 minutes)

### Step 1: Install Python

Make sure you have Python 3.7+ installed:
```bash
python --version
```

If not installed, download from [python.org](https://www.python.org/downloads/)

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Get Google Credentials

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or select existing)
3. Enable **Google Drive API**:
   - Go to "APIs & Services" → "Library"
   - Search "Google Drive API"
   - Click "Enable"
4. Create credentials:
   - Go to "APIs & Services" → "Credentials"
   - Click "Create Credentials" → "OAuth client ID"
   - Choose "Desktop app"
   - Download the JSON file
5. Rename downloaded file to `credentials.json`
6. Place it in the same folder as this script

### Step 4: Run the Script

```bash
python lock_drive_files.py
```

First time you run it:
- A browser window will open
- Sign in with your Google account
- Click "Allow" to grant permissions
- The script will save your login (you won't need to do this again)

## Usage

When you run the script, you'll see a menu:

```
🔒 Google Drive File Locker
============================================================

What would you like to do?
1. Lock ALL my Drive files (disable download for viewers)
2. Lock files in a specific folder
3. Unlock ALL my Drive files (enable download for viewers)
4. Show statistics (how many files are locked)
5. Exit
```

### Option 1: Lock All Files

Locks every file in your entire Drive. Perfect if you want to protect everything.

```
Enter choice (1-5): 1
⚠️  This will lock ALL files in your Drive. Continue? (yes/no): yes

📂 Scanning your Drive for files...
   Found 150 files so far...

✅ Found 150 files

🔒 Starting to lock 150 files...

[1/150] 🔐 Locking: Document1.pdf
[2/150] ✓ Already locked: Spreadsheet.xlsx
[3/150] 🔐 Locking: Presentation.pptx
...

📊 SUMMARY
============================================================
✅ Successfully locked: 120
⏭️  Already locked: 25
❌ Failed: 5
📁 Total files: 150
```

### Option 2: Lock Specific Folder

Lock only files in a specific folder (and optionally subfolders).

```
Enter choice (1-5): 2
Enter folder ID (from Drive URL): 1a2b3c4d5e6f7g8h9i0j
Include subfolders? (yes/no): yes
```

**How to get folder ID:**
1. Open the folder in Google Drive
2. Look at the URL: `https://drive.google.com/drive/folders/1a2b3c4d5e6f7g8h9i0j`
3. Copy the ID: `1a2b3c4d5e6f7g8h9i0j`

### Option 3: Unlock All Files

Reverses the lock operation (enables download for viewers).

### Option 4: Show Statistics

Shows how many files are locked vs unlocked without making any changes.

```
📊 STATISTICS
============================================================
📁 Total files: 150
🔒 Locked files: 120
🔓 Unlocked files: 30
📈 Locked percentage: 80.0%
```

## Important Notes

### What This Protects

✅ Prevents easy download via Drive UI  
✅ Disables print option for viewers  
✅ Blocks copy/paste in Drive editors  

### What This CANNOT Prevent

❌ Screenshots or photos of screen  
❌ Owner/editor downloads (they always can)  
❌ Files already downloaded before locking  

### Permissions

- You need **edit or owner** access to lock a file
- Files you only have "view" access to will be skipped
- Shared Drive files require **Manager** role

### Rate Limits

- Google Drive API has quotas (1,000 requests per 100 seconds)
- The script automatically pauses to avoid hitting limits
- For very large Drives (1000+ files), it may take several minutes

## Troubleshooting

### "credentials.json not found"

You need to download OAuth credentials from Google Cloud Console. See Step 3 above.

### "Insufficient permissions" errors

Some files will be skipped if:
- You don't own them
- You only have "view" access
- They're in a Shared Drive where you're not a Manager

This is normal and expected. The script will continue with other files.

### "Rate limit exceeded"

If you see this, the script will automatically wait and retry. Just let it run.

### Script is slow

For large Drives (1000+ files), the script needs to:
1. Scan all files (takes time)
2. Update each file individually
3. Pause to avoid rate limits

This is normal. You can leave it running in the background.

## Advanced Usage

### Run Without Interaction

You can modify the script to run automatically without the menu. Edit the `main()` function:

```python
def main():
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)
    
    # Automatically lock all files
    files = get_all_files(service)
    locked, skipped, failed = lock_all_files(service, files)
    
    print(f"Done! Locked {locked} files, skipped {skipped}, failed {failed}")
```

### Schedule Regular Runs

**Windows (Task Scheduler):**
1. Open Task Scheduler
2. Create Basic Task
3. Set trigger (e.g., daily at 2 AM)
4. Action: Start a program
5. Program: `python`
6. Arguments: `C:\path\to\lock_drive_files.py`

**Linux/Mac (Cron):**
```bash
# Run daily at 2 AM
0 2 * * * cd /path/to/script && python3 lock_drive_files.py
```

### Lock Only Specific File Types

Modify the `get_all_files()` function to filter by MIME type:

```python
# Only lock PDFs
if file['mimeType'] == 'application/pdf':
    all_files.append(file)
```

## Security

- Your credentials are stored locally in `token.pickle`
- The script only requests Drive access (no other Google services)
- You can revoke access anytime at [myaccount.google.com/permissions](https://myaccount.google.com/permissions)

## Files Created

- `token.pickle` - Your saved login (don't share this!)
- `credentials.json` - OAuth credentials (don't commit to git!)

## Need Help?

Common issues:
1. Make sure `credentials.json` is in the same folder
2. Make sure you have Python 3.7+
3. Make sure dependencies are installed (`pip install -r requirements.txt`)
4. Try deleting `token.pickle` and logging in again

---

## 🌟 About This Project

**Made by:** Mahesh  
**Made for:** Purnendu (childhood friend)  
**Purpose:** To help Purnendu easily lock and share his college notes  
**Tech Stack:** HTML, CSS, JavaScript, Google Drive API v3  
**Hosting:** Vercel (free tier)  
**Time saved:** Hours of manual clicking!  

### Why This Was Built

Purnendu needed an easy way to:
1. Lock his college notes to prevent unauthorized downloads
2. Share them with classmates securely
3. Do it all from his mobile phone
4. Not worry about technical setup

So Mahesh built this beautiful web app as a gift! ♥

---

## 🔗 Links

- **Live App:** https://drive-locker.vercel.app
- **GitHub:** https://github.com/gmahesh-star/drive-locker
- **Issues:** Report bugs or request features on GitHub

---

## 📝 License

MIT License - Use freely, modify as needed, share with friends!

---

## 💖 Special Thanks

To Purnendu - for being an amazing friend and inspiring this project!

**"Made with care for my childhood friend" - Mahesh**
