"""
Name:
    SanitizeURL
Author:
    William Walker @ Crutchfield
Description:
            Provides functionality to sanitize URLs by working around characters
    such as '.' and 't' so that links are no longer clickable or
    accidentally visited. Useful for safely displaying potentially
    malicious or sensitive URLs in logs, reports, or analysis.

imports:
    @WalkerLog.py
    pyperclip ---> For clipboard manipulation
    termcolor ---> For colored text
"""
from WalkerLog import *
import pyperclip
from termcolor import colored


def sanitize_http(url):
    return url.replace("https://", "hxxps://").replace("http://", "hxxp://")

def bracket_dots(url):
    return url.replace(".", "[.]")

def SanitizeURL(url):
    if url.startswith("hxxp") or "[.]" in url:
        return url

    sanitizedHttp = sanitize_http(url)
    log(f"\n[SAND1] SanitizedHTTP: {sanitizedHttp}")

    sanitizedHttpandBrackets = bracket_dots(sanitizedHttp)
    log(f"\n[SAND2] Fully Sanitized: {sanitizedHttpandBrackets}")

    return sanitizedHttpandBrackets


def SanitizeURLMain():
    print(colored("\n    *---------------------🧪 Sanitization Zone 🧪--------------------------*", "green"))
    url = input("\n    Paste a URL to sanitize: ").strip()
    log(f"\n[INPUT_SAND] User Input For URL: {url}")

    sanitizedHttpandBrackets = SanitizeURL(url)

    print(colored(f"\n    🔒 Sanitized URL: {sanitizedHttpandBrackets}", "green"))

    pyperclip.copy(sanitizedHttpandBrackets)

    print(colored("    📋 Sanitized URL copied to clipboard\n", "green"))

    print(colored("\n    *----------------------------------------------------------------------*", "green"))

