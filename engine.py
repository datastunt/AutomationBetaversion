import io
import os
import time
import random
import string
from io import BytesIO
from PIL import Image
import sys
import matplotlib
import pandas as pd
from datetime import datetime
from googletrans import Translator
from matplotlib import pyplot as plt
from selenium.common import NoSuchElementException
from config import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datastorage import uncompleted_contact, completed_contact, current_contact_data_status

matplotlib.use('Agg')
terminate_flag = False
completed_task = []
uncompleted_task = []
contact_persons = ""


def run_automation(bulk_file, media, text):
    try:

        time.sleep(20.5)

        if not terminate_flag:
            if media:
                media.save(media.filename)
                media = media.filename
            else:
                media = None
            bulk_file_management(bulk_file, media, text)
        else:
            sys.exit()
    except Exception as e:
        error_msg = f"Error occurred during opening WhatsApp link: : {str(e)}"
        print(error_msg)
        log_error(error_msg)


def bulk_file_management(bulk_file, media, text):
    global contact_persons
    if bulk_file and not terminate_flag:
        try:
            jobid = generate_job_id()
            bulk_file.save(bulk_file.filename)
            bulk_file = bulk_file.filename
            contacts_list = extracting_contacts(bulk_file)
            contact_persons = len(contacts_list)
            for number, name in contacts_list:
                name = str(name)
                name = name.rstrip().lstrip()
                if not terminate_flag:
                    try:
                        # Find the search input textbox
                        search_btn = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[title='New chat']")))

                        # Once the element is clickable, perform a click action
                        search_btn.click()
                        time.sleep(2.5)

                        # Find the search box
                        search_input = WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, "div[title='Search input textbox']")))

                        # Clear the input box first
                        search_input.clear()

                        # Input the name into the search input
                        for letter in name:
                            search_input.send_keys(letter)
                            # Add a small delay if needed
                            time.sleep(0.2)  # Adjust this value as needed
                        # Wait for some time (optional, if needed)
                        time.sleep(2.5)

                        try:
                            # Locate the element to check if contact is unavailable
                            selector = f"div.x9f619.x78zum5.xdt5ytf.x6s0dn4.x40yjcy.x2b8uid.x1c4vz4f.x2lah0s.xdl72j9.x1nhvcw1.xt7dq6l.x15uerrv.x13omvei.x1j3kn9t.x1m6arcz > div.x1f6kntn.x1fc57z9.x40yjcy > span._ao3e"
                            select_unavailable_contact = driver.find_element(By.CSS_SELECTOR, selector)
                            condition_text = select_unavailable_contact.text
                            condition = f"No results found for '{name}'"
                            if condition_text == condition:
                                # Code to handle contact being unavailable
                                back_btn = driver.find_element(By.XPATH,
                                                               "//*[@id='app']/div/div[2]/div[2]/div[1]/span/div/span/div/div[1]/div[2]/button")
                                back_btn.click()
                                timestamp = datetime.now().strftime('%H:%M:%S %d-%m-%Y')
                                unavlbl_contact_data = {'JobID': jobid,
                                                        'contact': name,
                                                        'status': "Unavailable on WhatsApp.",
                                                        'timestamp': timestamp
                                                        }
                                current_contact_data_status([unavlbl_contact_data])
                                uncompleted_contact([unavlbl_contact_data])
                                uncompleted_task.append(unavlbl_contact_data)
                        except NoSuchElementException:
                            search_input.send_keys(Keys.ENTER)
                            time.sleep(2.5)
                            if text:
                                select_text_box = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
                                    (By.CSS_SELECTOR, "div[role='textbox'][title='Type a message']")))
                                # Once the element is present, perform actions on it
                                select_text_box.click()
                                # Clear the text box first
                                select_text_box.clear()

                                if "{name}" in text:
                                    translator = Translator()
                                    translated_text = translator.translate(name, src='en', dest='hi')
                                    user = translated_text.text
                                    text_data = text.replace("{name}", user)
                                else:
                                    text_data = text
                                for msg in text_data:
                                    select_text_box.send_keys(msg)
                                    time.sleep(0.2)

                            if media:
                                attach_btn = driver.find_element(By.CSS_SELECTOR, "div.x11xpdln.x1d8287x.x1h4ghdb")
                                driver.execute_script("arguments[0].click();", attach_btn)
                                time.sleep(2.5)

                                # Wait for the parent li element to be present in the DOM
                                # select_media = driver.find_element(By.CSS_SELECTOR, "div.x1c4vz4f.xs83m0k.xdl72j9.x1g77sc7.x78zum5.xozqiw3.x1oa3qoh.x12fk4p8.xeuugli.x2lwn1j.x1nhvcw1.x1q0g3np.x6s0dn4.x1ypdohk.x1vqgdyp.x1i64zmx.x1gja9t")
                                # Click the input element to trigger the file selection dialog

                                select_media_input = driver.find_element(By.CSS_SELECTOR,
                                                                         "input[type='file'][accept='image/*,video/mp4,video/3gpp,video/quicktime']")
                                media_absolute_path = os.path.abspath(media)
                                select_media_input.send_keys(media_absolute_path)

                                # select_media.click()

                            time.sleep(3.5)

                            if text and media or media:
                            # To send message
                                send_button = driver.find_element(By.CSS_SELECTOR, "#app > div > div.two._aigs > div._aigu > div._aigv._aigz > span > div > span > div > div > div.x1n2onr6.xyw6214.x78zum5.x1r8uery.x1iyjqo2.xdt5ytf.x1hc1fzr.x6ikm8r.x10wlt62 > div > div._ajwz > div._ajx2 > div > div > span")
                                # Click the send button
                                send_button.click()

                            if text and not media:
                                send_button_selector = 'button[aria-label="Send"].x1c4vz4f.x2lah0s.xdl72j9.xfect85.x1iy03kw.x1lfpgzf'
                                send_button = driver.find_element(By.CSS_SELECTOR, send_button_selector)
                                send_button.click()

                            timestamp = datetime.now().strftime('%H:%M:%S %d-%m-%Y')
                            avlbl_contact_data = {'JobID': jobid,
                                                  'contact': name,
                                                  'status': "Message sent successfully.",
                                                  'timestamp': timestamp
                                                  }
                            current_contact_data_status([avlbl_contact_data])
                            completed_contact([avlbl_contact_data])
                            completed_task.append(avlbl_contact_data)
                        except Exception as e:
                            print(e)
                    except Exception as e:
                        error_msg = f"Error occurred during processing contact : "
                        print(error_msg, e)
                        log_error(error_msg)
                        continue

                else:
                    sys.exit()
        except Exception as e:
            error_msg = f"Error occurred during opening bulk file contact: {str(e)}"
            print(error_msg)
            log_error(error_msg)
        finally:
            os.remove(bulk_file)
            if media:
                os.remove(media)
            driver.quit()


def extracting_contacts(bulk_file):
    all_sheets_data = pd.read_excel(bulk_file, sheet_name=None)
    contacts_list = []
    for sheet_name, sheet_data in all_sheets_data.items():
        if sheet_data is not None and not sheet_data.empty:
            for index, row in sheet_data.iterrows():
                contacts_list.append((row['Number'], row['Name']))
    return contacts_list


def job_time():
    current_hour = datetime.now().hour
    if current_hour < 5 or current_hour >= 22:
        return True
    return False


def take_qr_code_screenshot():
    # Find the QR code element
    link = "https://web.whatsapp.com/"
    driver.get(link)
    qr_code_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "canvas[aria-label='Scan me!']")))
    # Get the location and size of the QR code element
    location = qr_code_element.location
    size = qr_code_element.size

    # Take a screenshot of the QR code area
    qr_code_screenshot = driver.get_screenshot_as_png()
    qr_code_image = Image.open(BytesIO(qr_code_screenshot))
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']
    qr_code_image = qr_code_image.crop((left, top, right, bottom))

    # Save the image to a file
    qr_code_image_path = "static/whatsapp_qr_code.png"
    qr_code_image.save(qr_code_image_path)
    # Return the path to the image file
    return qr_code_image_path


# Function to log errors
def log_error(error_msg):
    with open('error_log.txt', 'a') as f:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f'{timestamp}: {error_msg}\n')


def kill_automation():
    global terminate_flag
    terminate_flag = True
    return terminate_flag


def generate_job_id():
    alphabet = string.ascii_uppercase
    current_date = datetime.now().strftime('%d-%m-%Y')  # Get current date
    random_string = ''.join(random.choices(alphabet, k=6))  # Generate a random string of alphabets
    job_id = f"JOB-{current_date}-{random_string}"  # Combine current date and random string
    return job_id


def generate_pdf(df):
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis('tight')
    ax.axis('off')
    table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(8)  # Adjust font size as needed
    table.scale(1, 1.5)  # Adjust table scale for better fit in PDF
    # Save the figure as a PDF to a bytes buffer
    pdf_output = io.BytesIO()
    plt.savefig(pdf_output, format='pdf', bbox_inches='tight')
    pdf_output.seek(0)
    plt.close(fig)
    return pdf_output.getvalue()


def create_vcf(input_excel):
    try:
        # Read Excel file into DataFrame
        df = pd.read_excel(input_excel)

        # Create output directory for vCards
        output_dir = "vcards"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        vcf_paths = []

        # Iterate over rows in the DataFrame
        for index, row in df.iterrows():
            # Split the name based on the last space
            name_parts = str(row["Name"]).rsplit(' ', 1)
            first_name = name_parts[0]
            last_name = name_parts[1] if len(name_parts) > 1 else ''  # Extract last name if available

            # Create vCard content for the current row
            vcard_content = f'BEGIN:VCARD\n'
            vcard_content += f'VERSION:2.1\n'
            vcard_content += f'N:{last_name};{first_name}\n' if last_name else f'N:;{first_name}\n'
            vcard_content += f'FN:{first_name} {last_name}\n' if last_name else f'FN:{first_name}\n'
            vcard_content += f'TEL;CELL;VOICE:{row["Number"]}\n'
            vcard_content += f'REV:{pd.Timestamp.now().strftime("%Y%m%dT%H%M%SZ")}\n'
            vcard_content += f'END:VCARD\n'

            # Define output vCard file path based on the person's name
            if last_name:
                output_vcf = os.path.join(output_dir, f'{first_name} {last_name}.vcf')
            else:
                output_vcf = os.path.join(output_dir, f'{first_name}.vcf')

            # Write vCard content to file
            with open(output_vcf, 'w', encoding='utf-8') as vcf_file:
                vcf_file.write(vcard_content)

            vcf_paths.append(output_vcf)  # Append the path to the list of VCF paths

        # Return the list of generated vCard file paths
        return vcf_paths
    except Exception as e:
        print("Error occur during generating .VCF", e)
