import os
import sys
import time
import random
import json
from typing import Any, Dict, List, Union
from colorama import Style
from colorama import init, Fore
from dotenv import load_dotenv
from datetime import datetime
from .const import COLORS

init(autoreset=True)
load_dotenv()

def get_api_key(service: str = 'WHOISXML') -> str:
    key = os.getenv(f"{service}_API_KEY")
    if not key:
        print_color(f"✗ Missing API key for {service}", "error")
    return key or ""

def print_color(text: str, color: str = 'info', end: str = '\n') -> None:
    color_code = COLORS.get(color, COLORS['info'])
    if isinstance(text, (dict, list)):
        text = json.dumps(text, indent=2, default=str)
    print(f"{color_code}{text}{Style.RESET_ALL}", end=end)

def typewriter(text: str, color: str = 'info', delay: float = 0.03, end: str = '\n') -> None:
    color_code = COLORS.get(color, COLORS['info'])
    text = str(text)
    for char in text:
        sys.stdout.write(f"{color_code}{char}")
        sys.stdout.flush()
        time.sleep(delay * random.uniform(0.2, 0.3))
    sys.stdout.write(Style.RESET_ALL + end)

def loading_animation(text: str = "Loading", duration: float = 2) -> None:
    chars = "⣾⣽⣻⢿⡿⣟⣯⣷"
    end_time = time.time() + duration
    while time.time() < end_time:
        for char in chars:
            sys.stdout.write(f"\r{COLORS['info']}{text} {char}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\r" + " " * (len(text) + 2) + "\r")

def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def display_results(data: Union[Dict, List, str], title: str = None) -> None:
    if not data:
        print_color("No results to display", "warn")
        return

    if isinstance(data, dict) and 'error' in data:
        print_color(data['error'], "error")
        return

    if not isinstance(data, dict):
        data = {"Results": data}

    title = str(title or data.get("operation", "Results"))
    max_width = min(80, os.get_terminal_size().columns - 4)
    
   
    border = f"{COLORS['border']}╔{'═' * (max_width + 2)}╗"
    title_line = f"{COLORS['border']}║ {COLORS['highlight']}{title.center(max_width)}{COLORS['border']} ║"
    print(f"\n{border}\n{title_line}\n{COLORS['border']}╠{'═' * (max_width + 2)}╣")

    _print_content(data, max_width)
    
    print(f"{COLORS['border']}╚{'═' * (max_width + 2)}╝{Style.RESET_ALL}")

def _print_content(data: Any, width: int, indent: int = 0) -> None:
    """Recursively print content with proper indentation"""
    if isinstance(data, dict):
        for key, value in data.items():
            if key in ['operation', 'timestamp', 'api_used', 'api_status']:
                continue
                
            key_str = f"{' ' * indent}{key}:"
            if isinstance(value, (dict, list)):
                print(f"{COLORS['border']}║ {COLORS['highlight']}{key_str.ljust(width)} {COLORS['border']}║")
                _print_content(value, width, indent + 2)
            else:
                value_str = str(value)
                print(f"{COLORS['border']}║ {COLORS['highlight']}{key_str.ljust(width - len(value_str) - 1)}{COLORS['success']} {value_str} {COLORS['border']}║")
    elif isinstance(data, (list, tuple)):
        for item in data:
            _print_content(item, width, indent)