#!/usr/bin/env python3
"""
Simple Google Drive File Locker
Automatically locks all your Drive files to prevent download/copy/print for viewers.
"""

import os
import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import time

# Scopes required
SCOPES = ['https://www.googleapis.com/auth/drive']

def authenticate():
    """Authenticate with Google Drive API."""
    creds = None
    
    # Token file stores user's access and refresh tokens
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    # If no valid credentials, let user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists('credentials.json'):
                print("❌ ERROR: credentials.json not found!")
                print("\nPlease follow these steps:")
                print("1. Go to https://console.cloud.google.com/")
                print("2. Create a project and enable Google Drive API")
                print("3. Create OAuth 2.0 credentials (Desktop app)")
                print("4. Download credentials.json and place it in this folder")
                return None
            
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save credentials for next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    return creds

def get_all_files(service, folder_id=None, recursive=True):
    """Get all files from Drive."""
    all_files = []
    page_token = None
    
    print("📂 Scanning your Drive for files...")
    
    try:
        while True:
            # Build query
            if folder_id:
                query = f"'{folder_id}' in parents and trashed=false"
            else:
                query = "trashed=false"
            
            # List files
            results = service.files().list(
                q=query,
                pageSize=100,
                pageToken=page_token,
                fields="nextPageToken, files(id, name, mimeType, copyRequiresWriterPermission, capabilities)"
            ).execute()
            
            files = results.get('files', [])
            
            for file in files:
                # Skip folders if not recursive
                if file['mimeType'] == 'application/vnd.google-apps.folder':
                    if recursive:
                        # Recursively get files from subfolder
                        subfolder_files = get_all_files(service, file['id'], recursive)
                        all_files.extend(subfolder_files)
                else:
                    all_files.append(file)
            
            page_token = results.get('nextPageToken')
            if not page_token:
                break
            
            print(f"   Found {len(all_files)} files so far...")
    
    except HttpError as error:
        print(f"❌ Error scanning files: {error}")
        return []
    
    return all_files

def lock_file(service, file_id, file_name):
    """Lock a single file (disable download/copy/print for viewers)."""
    try:
        service.files().update(
            fileId=file_id,
            body={'copyRequiresWriterPermission': True},
            fields='id, name, copyRequiresWriterPermission'
        ).execute()
        return True
    except HttpError as error:
        if error.resp.status == 403:
            print(f"   ⚠️  Skipped (no permission): {file_name}")
        elif error.resp.status == 429:
            print(f"   ⏸️  Rate limited, waiting 2 seconds...")
            time.sleep(2)
            return lock_file(service, file_id, file_name)  # Retry
        else:
            print(f"   ❌ Error: {file_name} - {error}")
        return False

def lock_all_files(service, files, batch_size=10):
    """Lock all files with progress tracking."""
    total = len(files)
    locked = 0
    skipped = 0
    failed = 0
    
    print(f"\n🔒 Starting to lock {total} files...\n")
    
    for i, file in enumerate(files, 1):
        # Check if already locked
        if file.get('copyRequiresWriterPermission', False):
            print(f"[{i}/{total}] ✓ Already locked: {file['name']}")
            skipped += 1
            continue
        
        # Lock the file
        print(f"[{i}/{total}] 🔐 Locking: {file['name']}")
        if lock_file(service, file['id'], file['name']):
            locked += 1
        else:
            failed += 1
        
        # Rate limiting - pause between batches
        if i % batch_size == 0 and i < total:
            print(f"   💤 Pausing briefly to avoid rate limits...")
            time.sleep(1)
    
    return locked, skipped, failed

def unlock_all_files(service, files, batch_size=10):
    """Unlock all files (reverse operation)."""
    total = len(files)
    unlocked = 0
    skipped = 0
    failed = 0
    
    print(f"\n🔓 Starting to unlock {total} files...\n")
    
    for i, file in enumerate(files, 1):
        # Check if already unlocked
        if not file.get('copyRequiresWriterPermission', False):
            print(f"[{i}/{total}] ✓ Already unlocked: {file['name']}")
            skipped += 1
            continue
        
        # Unlock the file
        print(f"[{i}/{total}] 🔓 Unlocking: {file['name']}")
        try:
            service.files().update(
                fileId=file['id'],
                body={'copyRequiresWriterPermission': False},
                fields='id, name, copyRequiresWriterPermission'
            ).execute()
            unlocked += 1
        except HttpError as error:
            print(f"   ❌ Error: {file['name']} - {error}")
            failed += 1
        
        # Rate limiting
        if i % batch_size == 0 and i < total:
            time.sleep(1)
    
    return unlocked, skipped, failed

def main():
    """Main function."""
    print("=" * 60)
    print("🔒 Google Drive File Locker")
    print("=" * 60)
    print()
    
    # Authenticate
    creds = authenticate()
    if not creds:
        return
    
    service = build('drive', 'v3', credentials=creds)
    
    # Menu
    print("\nWhat would you like to do?")
    print("1. Lock ALL my Drive files (disable download for viewers)")
    print("2. Lock files in a specific folder")
    print("3. Unlock ALL my Drive files (enable download for viewers)")
    print("4. Show statistics (how many files are locked)")
    print("5. Exit")
    
    choice = input("\nEnter choice (1-5): ").strip()
    
    if choice == '1':
        # Lock all files
        confirm = input("\n⚠️  This will lock ALL files in your Drive. Continue? (yes/no): ")
        if confirm.lower() != 'yes':
            print("Cancelled.")
            return
        
        files = get_all_files(service)
        print(f"\n✅ Found {len(files)} files")
        
        if files:
            locked, skipped, failed = lock_all_files(service, files)
            print("\n" + "=" * 60)
            print("📊 SUMMARY")
            print("=" * 60)
            print(f"✅ Successfully locked: {locked}")
            print(f"⏭️  Already locked: {skipped}")
            print(f"❌ Failed: {failed}")
            print(f"📁 Total files: {len(files)}")
    
    elif choice == '2':
        # Lock specific folder
        folder_id = input("\nEnter folder ID (from Drive URL): ").strip()
        recursive = input("Include subfolders? (yes/no): ").strip().lower() == 'yes'
        
        files = get_all_files(service, folder_id, recursive)
        print(f"\n✅ Found {len(files)} files")
        
        if files:
            confirm = input(f"\nLock these {len(files)} files? (yes/no): ")
            if confirm.lower() == 'yes':
                locked, skipped, failed = lock_all_files(service, files)
                print("\n" + "=" * 60)
                print("📊 SUMMARY")
                print("=" * 60)
                print(f"✅ Successfully locked: {locked}")
                print(f"⏭️  Already locked: {skipped}")
                print(f"❌ Failed: {failed}")
    
    elif choice == '3':
        # Unlock all files
        confirm = input("\n⚠️  This will unlock ALL files in your Drive. Continue? (yes/no): ")
        if confirm.lower() != 'yes':
            print("Cancelled.")
            return
        
        files = get_all_files(service)
        print(f"\n✅ Found {len(files)} files")
        
        if files:
            unlocked, skipped, failed = unlock_all_files(service, files)
            print("\n" + "=" * 60)
            print("📊 SUMMARY")
            print("=" * 60)
            print(f"✅ Successfully unlocked: {unlocked}")
            print(f"⏭️  Already unlocked: {skipped}")
            print(f"❌ Failed: {failed}")
    
    elif choice == '4':
        # Show statistics
        files = get_all_files(service)
        locked_count = sum(1 for f in files if f.get('copyRequiresWriterPermission', False))
        unlocked_count = len(files) - locked_count
        
        print("\n" + "=" * 60)
        print("📊 STATISTICS")
        print("=" * 60)
        print(f"📁 Total files: {len(files)}")
        print(f"🔒 Locked files: {locked_count}")
        print(f"🔓 Unlocked files: {unlocked_count}")
        print(f"📈 Locked percentage: {(locked_count/len(files)*100):.1f}%")
    
    elif choice == '5':
        print("Goodbye!")
        return
    
    else:
        print("Invalid choice!")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⏹️  Stopped by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
