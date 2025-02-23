# Instagram: https://www.instagram.com/pycode.hubb/
# Telegram: https://t.me/pycode_hubb

import os
import time

HEADER = """
░██╗░░░░░░░██╗███████╗██████╗░  ██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
░██║░░██╗░░██║██╔════╝██╔══██╗  ██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██████╦╝  ██████╦╝██║░░░░░██║░░██║██║░░╚═╝█████═╝░█████╗░░██████╔╝
░░████╔═████║░██╔══╝░░██╔══██╗  ██╔══██╗██║░░░░░██║░░██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
░░╚██╔╝░╚██╔╝░███████╗██████╦╝  ██████╦╝███████╗╚█████╔╝╚█████╔╝██║░╚██╗███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░  ╚═════╝░╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
                                                                                        by Pycode.Hubb
"""

def normalize_website(site):
    if site.startswith("www."):
        return site[4:]
    return site

def block_website(site):
    site = normalize_website(site)
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
    redirect = "127.0.0.1"

    entry = f"{redirect} {site}\n"
    entry_www = f"{redirect} www.{site}\n"

    try:
        with open(hosts_path, 'r+') as file:
            content = file.read()
            if entry.strip() not in content and entry_www.strip() not in content:
                if not content.endswith('\n'):
                    file.write('\n')
                file.write(entry)
                file.write(entry_www)
                print(f"{site} has been blocked.")
            else:
                print(f"{site} is already blocked.")
    except Exception as e:
        print(f"Error: {e}")

def block_sites_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            sites = file.readlines()
            for site in sites:
                block_website(site.strip())
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

def print_blocked_websites():
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
    redirect = "127.0.0.1"
    
    try:
        with open(hosts_path, 'r') as file:
            content = file.readlines()
            blocked_sites = [line.split()[1].replace('www.', '') for line in content if line.startswith(redirect)]
            blocked_sites = list(set(blocked_sites))
            if blocked_sites:
                print("Blocked websites:")
                for site in blocked_sites:
                    print(site)
            else:
                print("No websites are currently blocked.")
    except Exception as e:
        print(f"Error: {e}")

def unblock_website(site):
    site = normalize_website(site)
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
    redirect = "127.0.0.1"

    entry = f"{redirect} {site}\n"
    entry_www = f"{redirect} www.{site}\n"

    try:
        with open(hosts_path, 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            file.truncate()
            for line in lines:
                if line.strip() != entry.strip() and line.strip() != entry_www.strip():
                    file.write(line)
        print(f"{site} has been unblocked.")
    except Exception as e:
        print(f"Error: {e}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear_screen()
        print(HEADER)
        print("Select an option:")
        print("  1. Block a website")
        print("  2. Bulk Block websites with a TXT file")
        print("  3. Print blocked websites")
        print("  4. Unblock a website")
        print("  5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            site_to_block = input("Enter the website to block (e.g., www.example.com): ").strip()
            block_website(site_to_block)
            time.sleep(2)
        elif choice == "2":
            file_path = input("Enter the path to the TXT file: ").strip()
            block_sites_from_file(file_path)
            time.sleep(2)
        elif choice == "3":
            print_blocked_websites()
            input("Press Enter to continue...")
        elif choice == "4":
            site_to_unblock = input("Enter the website to unblock (e.g., www.example.com): ").strip()
            unblock_website(site_to_unblock)
            time.sleep(2)
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
            time.sleep(2)

if __name__ == "__main__":
    main()

# By pycode.hubb