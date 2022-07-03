#!/usr/bin/env python3

"""
Hi! I know why you're here, you don't trust me and want to check the code yourself.
Well, I won't stop you, even if I wanted to.
I even left a few comments for you!
So go ahead, read the code;
That what open-source is all about, right? ;)

- G_cat
"""

# IMPORTS
from os import system # Clearing the terminal
from shutil import get_terminal_size # Terminal size for centering text
from urllib.parse import quote_plus # Url encoding for submit url

# CONSTANTS
SIZE = get_terminal_size() # Terminal size

# VARIABLES
answers = { # Form answers dictionary
    "langs": [], # Preferred languages 
    "fav_lang": "", # Favorite language
    "code": "", # Code question answer
    "discord": "" # Discord tag
}

# FUNCTIONS
def _clear() -> None: system("clear") # Clearing the screen
def _center_text(txt:str) -> str: # Centering the text
    margin = int((SIZE.columns-len(txt))/2) # Get margin
    return f"{' ' * margin}{txt}{' ' * margin}" # Return centered
def _bold(txt:str) -> str: return f"\u001b[1m{txt}\u001b[0m" # Make text BOLD
def _quit() -> None: # Clear terminal and quit app
    _clear() # Clear
    quit(0) # Quit no err

# SCREENS
def _welcome_screen() -> None: # Welcome
    print(f"""{_bold(_center_text("Hello and welcome!"))}
{_center_text("If you're here you probably want to become a member of rainbow.sh!")}

{_bold(_center_text("And lucky for you, it's actually quite easy!"))}
{_center_text("All you need to do is fill out a short membership application form.")}

{_bold(_center_text("The only things you'll need before we get started are:"))}
{_center_text("1.A github account,")}
{_center_text("2.A discord account,")}
{_center_text("3.And some basic programming skills.")}

{_bold(_center_text("Oh, and also, before you start!"))}
{_center_text("Please read our membership requirements.")}
{_center_text("They are available at: https://github.com/rainbow-sh/membership/blob/main/docs/membership-requirements.md")}

{_bold(_center_text("If everything sounds good, we can continue to the first question!"))}""", end="\n\n")
    if input("I agree with all of the membership requirements and want to become a member of rainbow.sh [y/N]: ").lower() != "y": _quit()

def _lang_screen() -> None: # Language question
    print(f"""{_bold(_center_text("Great! Now tell me, what are your preferred programming languages?"))}
{_center_text("We are currently looking for Python, Go, Rust, Bash, POSIX-shell and C++ developers, but if you think your language will be useful, you can also mention it.")}""", end="\n\n")
    answers["langs"] = input("My preferred languages are (comma seperated): ").split(",")

    print() # Separator
    
    # If multiple languages
    if len(answers["langs"]) > 1:
        print(_bold(_center_text(f"Now, out of all the ones you've listed ({', '.join(answers['langs'])}), which one is your favorite?")), end="\n\n")
        answers["fav_lang"] = input("My favorite language is: ") # Ask which one is the favorite
    else: answers["fav_lang"] = answers["langs"][0] # Otherwise, set the only one as the favorite

def _code_screen() -> None: # Code question
    print(f"""{_bold(_center_text(f'Good, but can you print a simple "hello world" in red in your favorite language ({answers["fav_lang"]})?'))}
{_center_text("You are allowed to use google.")}""", end="\n\n")
    answers["code"] = input('''Piece of code (don't include boilerplate (ex. "fn main() {}"), just the code you wrote yourself): ''')

def _discord_screen() -> None: # Discord tag
    print(f"""{_bold(_center_text("We'll check this one later..."))}
{_center_text("Now for the final question, what is your discord tag? If you get accepted you will receive a message from us.")}""", end="\n\n")
    answers["discord"] = input("Discord tag (numbers included): ")

def _submit_screen() -> None: # Submit
    body = f"""# Membership application

## Preferred languages

{", ".join(answers["langs"])}

## Favorite language

{answers["fav_lang"]}

## Code question answer

{answers["code"]}

## Discord tag

{answers["discord"]}

""" # Github issue body

    print(f"""{_bold(_center_text("And we're done!"))}
{_center_text('The last thing you need to do is submit an "issue" to our github membership repository.')}

{_bold(_center_text("THIS IS IMPORTANT!"))}
{_bold(_center_text(f"Click on this link and submit your membership application:"))}
{_center_text(f"https://github.com/rainbow-sh/membership/issues/new?title={quote_plus(answers['discord'].split('#')[0])}&body={quote_plus(body)}")}&labels=Membership+application

{_bold(_center_text("And congrats!"))}
You have completed the membership application form! Now all you have to do is wait. If your application is closed as "Not planned", that means it has been rejected, submit a new one in 2 weeks. If it gets closed as "resolved" however, you're in luck! You will just have to wait until we contact you on discord with the tag you provided.""", end="\n\n")
    input("[Press enter to quit]") # Quit

# MAIN FUNCTION
def main() -> None:
    _clear() # Clear the screen
    
    # For every screen
    for screen in (_welcome_screen, _lang_screen, _code_screen, _discord_screen, _submit_screen):
        screen() # Show the screen
        _clear() # Clear the terminal

# START
if __name__=="__main__": # If not imported
    try: main() # Run main function
    except KeyboardInterrupt: _quit() # Quit on ctrl+c

# That's it, are you happy now?