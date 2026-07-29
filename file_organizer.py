import os
import shutil
import logging

logging.basicConfig(
    filename="file_organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

path = input("Enter Path: ").strip()

try:
    if not os.path.exists(path):
        raise FileNotFoundError("The specified path does not exist.")

    files = os.listdir(path)
    logging.info(f"Directory scanned: {path}")

    for file in files:
        file_path = path + "/" + file

        if os.path.isdir(file_path) or file == "file_organizer.log":
            continue

        name, extension = os.path.splitext(file)
        extension = extension[1:]  

        if not extension:
            extension = "No_Extension"

        target_folder = path + "/" + extension
        destination_path = target_folder + "/" + file

        if os.path.exists(target_folder):
            shutil.move(file_path, destination_path)
            logging.info(f"File moved: {file} -> {target_folder}")
        else:
            os.makedirs(target_folder)
            logging.info(f"Folder created: {target_folder}")
            shutil.move(file_path, destination_path)
            logging.info(f"File moved: {file} -> {target_folder}")

    print("Files organized successfully!")

except FileNotFoundError as e:
    print(f"Error: {e}")
    logging.error(f"Error occurred: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
    logging.error(f"Unexpected error: {e}")