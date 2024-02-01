import os
import datetime

diary = "diary.txt"

def add_entry():
    entry = input("add to your diary?\n")
    date = datetime.datetime.now()

    with open(diary, 'a') as f:
        f.write(f'\n{date.strftime("%B %d, %Y %I:%M%p")}\n')
        f.write(entry)

def read_entry():
    try:
        with open(diary, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print('Diary not found.... add new entry. ')

def clear_diary():
    confirm = input("Are you sure you want to clear all entries? (y/n)\n ")
    if confirm.lower()=='y':
        with open(diary, 'w') as f:
            f.write("")
        print("All entries have been cleared. ")
    else:
        print("No entries have been cleared. ")

