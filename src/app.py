#!/usr/bin/env python3

from os import system
from shutil import get_terminal_size

SIZE = get_terminal_size()

def _clear() -> None: system("clear")
def _center_text(txt:str) -> str:
    margin = int((SIZE.columns-len(txt))/2)
    return f"{' ' * margin}{txt}{' ' * margin}"
def _bold(txt:str) -> str: return f"\u001b[1m{txt}\u001b[0m"

def _quit() -> None:
    _clear()
    quit(0)

def _welcome_screen() -> None:
    print(f"""{_bold(_center_text("Hello and welcome!"))}
{_center_text("If you're here you probably want to become a member of rainbow.sh!")}

{_bold(_center_text("And lucky for you, it's actually quite easy!"))}
{_center_text("All you need to do is fill out a short membership application form.")}
{_center_text("We will ask you a couple of questions about your CLI/TUI development knowledge which you will then submit.")}

{_bold(_center_text("The only things you'll need before we get started are:"))}
{_center_text("1.A github account,")}
{_center_text("2.A discord account,")}
{_center_text("3.And some basic programming skills.")}

{_bold(_center_text("Oh, and also, before you start!"))}
{_center_text("Please read our membership requirements if you do get accepted.")}
{_center_text("They are available at: https://github.com/rainbow-sh/membership/blob/main/docs/membership-requirements.md")}

{_bold(_center_text("If everything sounds good, we can continue to the first question!"))}""", end="\n\n")

    if input("I agree with all of the membership policies and want to become a member of rainbow.sh [y/N]: ").lower() != "y": _quit()

def main() -> None:
    _clear()
    
    _welcome_screen()

    _clear()

if __name__=="__main__":
    main()