import os
from datetime import datetime


def convert():
    for count, filename in enumerate(os.listdir(folder)):
        date = f'{filename.split("(")[0]}' if "(" in filename else f"{filename.split('.')[0]}"
        try:
            date = datetime.strptime(date, '%d_%m_%Y').date()
            date = date.strftime('%Y-%m-%d')

            new_name = f'{count}_{date}.jpeg'
            os.rename(f'{folder}/{filename}', f'{folder}_renamed/{new_name}')
        except ValueError:
            print("Error reading", filename)


def print_names():
    for _, filename in enumerate(os.listdir(f'{folder}_renamed')):
        if ".jpeg" in filename:
            print(f'"{filename}",')


if __name__ == '__main__':
    print("Copy the example files to photos folder to test")
    folder = "photos"
    #convert()
    print_names()
