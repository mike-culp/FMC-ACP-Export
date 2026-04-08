# prompts.py
import getpass

from utils import normalize_base_url


def prompt_connection():
    base = normalize_base_url(input("FMC IP/Hostname: "))
    user = input("Username: ")
    pwd = getpass.getpass("Password: ")
    verify_tls = prompt_tls_verification()
    return base, user, pwd, verify_tls


def prompt_tls_verification() -> bool:
    choice = input("Verify TLS certificate? [y/N]: ").strip().lower()
    return choice in {"y", "yes"}


def choose_policy(policies):
    for i, p in enumerate(policies, 1):
        print(f"{i}. {p['name']}")

    while True:
        sel = input("Select: ")
        if sel.isdigit():
            return policies[int(sel) - 1]