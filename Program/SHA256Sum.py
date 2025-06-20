"""
Name:
    SHA256Sum
Author:
    William Walker @ Crutchfield
Description:
        Module for generating SHA256 hashes from either plaintext input or a selected file.
imports:
    @WalkerLog.py
    termcolor   ---> For colored console output
"""
from WalkerLog import *
import hashlib
import os
from termcolor import colored
import win32ui

def SHA256SelectFile():
    dlg = win32ui.CreateFileDialog(1)
    dlg.DoModal()
    return dlg.GetPathName()

def SHA256FromFile():
    print(colored("\n    🗂️  Opening File Explorer to select a file...", "cyan"))
    path = SHA256SelectFile()

    if not path or not os.path.isfile(path):
        print(colored("    ❌ No file selected or invalid path.\n", "red"))
        return

    filename = os.path.basename(path)
    hash_sha256 = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha256.update(chunk)
    except Exception as e:
        print(colored(f"    ❌ Error reading file: {e}", "red"))
        return

    digest = hash_sha256.hexdigest()
    formatted = f"{filename}|{digest}"

    print(colored(f"\n    ✅ SHA256 Hash: {digest}", "green"))
    print(colored(f"\n    📋 {formatted}", "green"))
    log(f"\n[SHA256] File hashed: {filename}")
    log(f"\n[SHA256] {formatted}")
    return formatted

def SHA256FromString(text):
    if not text:
        print(colored("    ❌ No input received. Empty string provided.\n", "red"))
        return

    hash_sha256 = hashlib.sha256()
    hash_sha256.update(text.encode("utf-8"))

    digest = hash_sha256.hexdigest()
    formatted = f"{text}|{digest}"

    print(colored(f"\n    ✅ SHA256 Hash: {digest}", "green"))
    print(colored(f"\n    📋 {formatted}", "green"))
    log(f"\n[SHA256] String hashed: {text}")
    log(f"\n[SHA256] {formatted}")
    return formatted



def SHA256FromPlaintext():
    text = input("\n    Enter plaintext to hash: ").strip()

    if not text:
        print(colored("    ❌ No input received. Please enter a valid string.\n", "red"))
        return

    hash_sha256 = hashlib.sha256()
    hash_sha256.update(text.encode("utf-8"))

    digest = hash_sha256.hexdigest()
    formatted = f"{text}|{digest}"

    print(colored(f"\n    ✅ SHA256 Hash: {digest}", "green"))
    print(colored(f"\n    📋 {formatted}", "green"))
    log(f"\n[SHA256] Plaintext hashed: {text}")
    log(f"\n[SHA256] {formatted}")
    return formatted

def SHA256SumMain():
    print(colored("\n    *---------------------------💫 SHA256SUM 💫----------------------------*", "yellow"))

    choice = input("\n    File or Plaintext SHA256 hash? (f/p): ").strip().lower()

    if choice == "f":
        SHA256FromFile()
    elif choice == "p":
        SHA256FromPlaintext()
    else:
        print(colored("    ❌ Invalid option. Returning to menu.", "red"))

    print(colored("\n    *----------------------------------------------------------------------*", "yellow"))
