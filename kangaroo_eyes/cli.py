import sys
import time
from colorama import Style
from typing import Any
from .utils import (
    print_color,
    typewriter,
    clear_screen,
    display_results
)
from .scanner import NetworkScanner
from .api import get_historical_ips
from .const import BANNER, COLORS

class KangarooCLI:
    def __init__(self):
        self.scanner = NetworkScanner()
        self.target = ""

    def show_menu(self) -> None:
        clear_screen()
        print_color("║=================== WELCOME =====================║", 'error')
        typewriter("                                  -       +     ", 'error')
        typewriter("                                 -%%+   @++     ", 'error')
        typewriter(" █ █ █▀█ █▀█ █▀▀ █▀█ █▀█ █▀█ █▀█  +%%*%@++      ", 'error')
        typewriter(" █▀▄ █▀█ █ █ █ █ █▀█ █▀▄ █ █ █ █  -%%%%%+       ", 'error')
        typewriter(" ▀ ▀ ▀ ▀ ▀ ▀ ▀▀▀ ▀ ▀ ▀ ▀ ▀▀▀ ▀▀▀   #%%@%%%      ", 'error')
        typewriter(" █▀▀ █ █ █▀▀ █▀▀                  @::|%%%%%     ", 'error')
        typewriter(" █▀▀  █  █▀▀ ▀▀█                 @@%%==.%%@@    ", 'error')
        typewriter(" ▀▀▀  ▀  ▀▀▀ ▀▀▀ V:1.0       @@@@%%%::          ", 'error')
        typewriter(" AUTHOR : dronXploit    @:#%%%%%%%#::.          ", 'error')
        typewriter("                     @%%%%%%%%%%%+*:::.         ", 'error')
        typewriter("                   %%%%%%%%%%%%++++:::          ", 'error')
        typewriter("                 #%%%%++++%%%%++++::::          ", 'error')
        typewriter("                %%%%%++++++++++++::::           ", 'error')
        typewriter("               .#++++++++++::+::::+             ", 'error')
        typewriter("               %+++++++%+::::@::.++             ", 'error')
        typewriter("               %+++++++++::::+.::.+.            ", 'error')
        typewriter("              .%%*+++++++-++++ .: +=            ", 'error')
        typewriter("              @%%%%*+++++=+++-  % @.            ", 'error')
        typewriter("              %%+:%%%+++:++++  %%.              ", 'error')
        typewriter("              %%+:: %++::+++                    ", 'error')
        typewriter("             %%+::   :::+++                     ", 'error')
        typewriter("            %%+::   .::.++                      ", 'error')
        typewriter("          =%%=:     :: ++++++++@@@@.            ", 'error')
        typewriter(" +%%%%%%%%%::.     .::::::::%.                  ", 'error')
        typewriter("   .::::::.              ...%%%%%               ", 'error')
        print_color("╠=-----------------------------------------------=╣", 'error')
        print_color("║ FOLLOW && SUPPORT:                              ║", 'error')
        print_color("║  saweria.co/dronxploit                          ║", 'error')
        print_color("║  instagram/com/dronxploit                       ║", 'error')
        print_color("╚=================================================╝", 'error')
        print_color("")
        typewriter("Selamat bersenang-senang, nak", 'error')
        print_color("")
        print_color("")
        
        menu_items = [
            ("Masukkan URL dulu", "1"),
            ("Rekaman DNS", "2"),
            ("IP Historia", "3"),
            ("Scane Port", "4"),
            ("WHOIS bruh", "5"),
            ("Exit", "6")
        ]
        
        for text, num in menu_items:
            print_color(f"[{num}] {text}", 'warn')

    def run(self) -> None:
        results = get_historical_ips(self.target)
        display_results(results)
        while True:
            self.show_menu()
            choice = input(f"\n{COLORS['warn']}Select option (1-6): ").strip()
            
            if choice == "6":
                typewriter("\nGoodbye! Stay secure!", 'success')
                sys.exit()
                
            elif choice == "1":
                self.target = input(f"{COLORS['warn']}Masukkan URL dulu: ").strip()
                if self.target:
                    print_color(f"✓ Target set: {self.target}", 'success')
                else:
                    print_color("✗ Target cannot be empty", 'error')
                time.sleep(1)
                
            elif choice in ["2", "3", "4", "5"]:
                if not self.target:
                    input(f"{COLORS['warn']}Enter target domain: ").strip()
                    print_color(f"✓ Target set: {self.target}", 'success')
                
                try:
                    if choice == "2":
                        results = self.scanner.dns_enum(self.target)
                    elif choice == "3":
                        results = get_historical_ips(self.target)
                    elif choice == "4":
                        results = self.scanner.port_scan(self.target)
                    elif choice == "5":
                        results = self.scanner.whois_lookup(self.target)
                    
                    display_results(results)
                    
                except Exception as e:
                    print_color(f"✗ Operation failed: {str(e)}", 'error')
                
                input(f"\n{COLORS['warn']}Press Enter to continue...")

            else:
                print_color("✗ Invalid option! Please choose 1-6", 'error')
                time.sleep(1)
