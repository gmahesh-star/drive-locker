# Simple Google Drive File Locker

A simple Python script to automatically lock all your Google Drive files to prevent viewers from downloading, copying, or printing them.

## What This Does

This script sets the "Disable options to download, print, and copy for commenters and viewers" setting on all your Drive files automatically, so you don't have to do it manually for each file.

## Quick Setup (5 minutes)

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

**Made for:** Helping your friend automate Drive file locking  
**Time saved:** Hours of manual clicking!  
**License:** MIT - Use freely
