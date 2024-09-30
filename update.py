import os
import sys
import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

def fetch_latest_file(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(filename, "w") as file:
            file.write(response.text)
        logging.info(f"\033[92mSuccessfully updated {filename}\033[0m")
    except requests.RequestException as e:
        logging.error(f"\033[91mFailed to update {filename}: {e}\033[0m")
        sys.exit(1)

def update_main():
    main_url = "https://raw.githubusercontent.com/TeamD-404/Pep-GPT/main/PepGPT.py"
    fetch_latest_file(main_url, "PepGPT_updated.py")
    os.replace("PepGPT_updated.py", "PepGPT.py")

if __name__ == "__main__":
    print("\033[0m")
    print("\033[92m")
    print("""\033[0m

 __      __                        _____________________________
            
         🍁 PepGPT 🍁

      Created By: @sethMacfl
      
 __      __                        _____________________________

    """)
    logging.info("Starting update process...")
    update_main()
    logging.info("Update process completed successfully.")
