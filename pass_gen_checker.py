# ============================================================
# SECTION: IMPORTS & SETUP
# ============================================================
import os
import re
import sys
import time
import math
import string
import secrets
from typing import Dict, Any

try:
    import colorama
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich import box
except ImportError:
    print("Missing required libraries. Please install them using: pip install -r requirements.txt")
    sys.exit(1)

colorama.init()
console = Console()

# ============================================================
# SECTION: UTILITIES (scoring, crack time, common passwords)
# ============================================================

COMMON_PASSWORDS = {
    "password", "123456", "123456789", "qwerty", "abc123", "password1",
    "111111", "12345678", "iloveyou", "admin", "letmein", "monkey",
    "1234567", "sunshine", "master", "welcome", "shadow", "dragon",
    "654321", "superman", "qwerty123", "michael", "football", "baseball",
    "login", "hello", "charlie", "donald", "password123", "passw0rd",
    "pass123", "root", "toor", "test", "guest", "default", "changeme"
}

def clear_screen() -> None:
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate_crack_time(password: str) -> str:
    """Calculates the estimated crack time of a password."""
    if not password:
        return "Instantly ⚡"
        
    charset_size = 0
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    if has_lower: charset_size = 26
    if has_upper: charset_size += 26
    if has_digit: charset_size += 10
    if has_special: charset_size += 33
        
    if charset_size == 0:
        charset_size = 26
        
    combinations = charset_size ** len(password)
    seconds = combinations / 10_000_000_000
    
    if seconds < 1:
        return "Instantly ⚡"
    elif seconds < 60:
        return f"{int(seconds)} seconds"
    elif seconds < 3600:
        return f"{int(seconds / 60)} minutes"
    elif seconds < 86400:
        return f"{int(seconds / 3600)} hours"
    elif seconds < 31536000:
        return f"{int(seconds / 86400)} days"
    elif seconds < 3153600000:
        return f"{int(seconds / 31536000)} years"
    else:
        return f"{int(seconds / 3153600000)} centuries 🏛️"

def evaluate_password(password: str) -> Dict[str, Any]:
    """Analyzes password strength and returns scoring data."""
    score = 0
    length = len(password)
    
    # CHECK 1 - Length Score
    if 1 <= length <= 5:
        score += 0
    elif 6 <= length <= 7:
        score += 10
    elif 8 <= length <= 11:
        score += 20
    elif 12 <= length <= 15:
        score += 30
    elif length >= 16:
        score += 40
        
    # CHECK 2 - Character Variety
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    if has_upper: score += 10
    if has_lower: score += 10
    if has_digit: score += 10
    if has_special: score += 15
    
    # CHECK 3 - Pattern Penalty
    lower_pass = password.lower()
    common_patterns = ["123", "abc", "qwerty", "111", "000"]
    has_pattern = any(p in lower_pass for p in common_patterns)
    if has_pattern:
        score -= 10
        
    # CHECK 4 - Common Password Check
    is_common = lower_pass in COMMON_PASSWORDS
    if is_common:
        score -= 20
        
    # Ensure score is within 0-100 (never negative)
    score = max(0, min(100, score))
    
    if score <= 25:
        strength = "VERY WEAK"
        color = "red"
        emoji = "⚠️"
    elif score <= 45:
        strength = "WEAK"
        color = "red"
        emoji = "⚠️"
    elif score <= 65:
        strength = "MEDIUM"
        color = "yellow"
        emoji = "👍"
    elif score <= 85:
        strength = "STRONG"
        color = "green"
        emoji = "💪"
    else:
        strength = "VERY STRONG"
        color = "cyan"
        emoji = "🛡️"
        
    # For strength level string in table
    strength_label = f"{strength} {emoji}"
    
    return {
        "score": score,
        "strength_name": strength,
        "strength_label": strength_label,
        "color": color,
        "length": length,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digit": has_digit,
        "has_special": has_special,
        "has_pattern": has_pattern,
        "is_common": is_common
    }

# ============================================================
# SECTION: BANNER
# ============================================================

def show_banner() -> None:
    """Displays the initial animated startup banner."""
    clear_screen()
    try:
        import pyfiglet
        f = pyfiglet.Figlet(font='doom')
        ascii_art = f.renderText("Pass_Gen_&_Checker")
        console.print(f"[bold cyan]{ascii_art}[/bold cyan]")
    except Exception:
        console.print("[bold cyan]Pass_Gen_&_Checker[/bold cyan]")
        
    lines = [
        ("  Password Generator & Strength Checker", "bold white"),
        ("  v1.0  |  github.com/CyberBros435", "magenta"),
        ("─────────────────────────────────────────", "cyan")
    ]
    
    for text, style in lines:
        console.print(f"[{style}]{text}[/{style}]")
        time.sleep(0.05)

# ============================================================
# SECTION: MAIN MENU
# ============================================================

def display_main_menu() -> str:
    """Displays the main menu and returns the user's choice."""
    menu_content = """\
[bold white]      MAIN MENU                 
                                
  [1]  Generate Password        
  [2]  Check Password Strength  
  [3]  Exit                     [/bold white]"""
    console.print(Panel(menu_content, border_style="cyan", box=box.ROUNDED, expand=False))
    
    choice = console.input("  [cyan]»[/cyan] Enter choice [1/2/3]: ").strip()
    return choice

# ============================================================
# SECTION: PASSWORD GENERATOR
# ============================================================

def password_generator() -> None:
    """Handles the password generation tool logic."""
    while True:
        clear_screen()
        console.print(Panel("[bold white]🎲 Password Generator[/bold white]", border_style="cyan", expand=False))
        
        # Ask for length
        length_str = console.input("\n  Enter password length (min 1 - max 999): ").strip()
        try:
            length = int(length_str)
            if not 1 <= length <= 999:
                console.print("  [bold red]❌ Invalid input. Please enter a valid number.[/bold red]")
                time.sleep(1.5)
                continue
        except ValueError:
            console.print("  [bold red]❌ Invalid input. Please enter a valid number.[/bold red]")
            time.sleep(1.5)
            continue
            
        break
        
    charset = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    
    while True:
        # Generate password
        password = "".join(secrets.choice(charset) for _ in range(length))
        
        # Show password
        pwd_panel = f"""\
[bold white]  🔑 Generated Password:             
                                     
     [bold cyan]{password}[/bold cyan]               [/bold white]"""
        console.print()
        console.print(Panel(pwd_panel, border_style="cyan", box=box.ROUNDED, expand=False))
        
        while True:
            again = console.input("\n  [cyan]»[/cyan] Generate another? [y/n]: ").strip().lower()
            if again in ['y', 'n']:
                break
            console.print("  [bold red]❌ Please enter y or n.[/bold red]")
            
        if again == 'y':
            continue
        else:
            console.print("  [bold green]✅ Returning to main menu...[/bold green]")
            time.sleep(1)
            break

# ============================================================
# SECTION: PASSWORD CHECKER
# ============================================================

def password_checker() -> None:
    """Handles the password strength checking tool logic."""
    while True:
        clear_screen()
        console.print(Panel("[bold white]🔐 Password Strength Checker[/bold white]", border_style="cyan", expand=False))
        
        while True:
            password = console.input("\n  Enter your password: ")
            if not password:
                console.print("  [bold red]❌ Password cannot be empty.[/bold red]")
            else:
                break
                
        eval_data = evaluate_password(password)
        crack_time = calculate_crack_time(password)
        
        # Build Table
        table = Table(border_style="cyan", box=box.ROUNDED, show_header=False)
        table.add_column("Property", style="bold white")
        table.add_column("Value")
        
        table.add_row("Password", password)
        table.add_row("Length", f"{eval_data['length']} characters")
        table.add_row("Score", f"[{eval_data['color']}]{eval_data['score']} / 100[/{eval_data['color']}]")
        table.add_row("Strength Level", f"[{eval_data['color']}]{eval_data['strength_label']}[/{eval_data['color']}]")
        table.add_row("Estimated Crack Time", crack_time)
        
        table.add_section()
        
        table.add_row("Has Uppercase", "[bold green]✅ Yes[/bold green]" if eval_data['has_upper'] else "[bold red]❌ No[/bold red]")
        table.add_row("Has Lowercase", "[bold green]✅ Yes[/bold green]" if eval_data['has_lower'] else "[bold red]❌ No[/bold red]")
        table.add_row("Has Numbers", "[bold green]✅ Yes[/bold green]" if eval_data['has_digit'] else "[bold red]❌ No[/bold red]")
        table.add_row("Has Special Chars", "[bold green]✅ Yes[/bold green]" if eval_data['has_special'] else "[bold red]❌ No[/bold red]")
        
        table.add_row("Common Patterns", "[bold red]❌ Found (weak!)[/bold red]" if eval_data['has_pattern'] else "[bold green]✅ Not found[/bold green]")
        table.add_row("Common Password", "[bold red]❌ Common![/bold red]" if eval_data['is_common'] else "[bold green]✅ Not common[/bold green]")
        table.add_row("Length 12+ Suggested", "[bold green]✅ Good length[/bold green]" if eval_data['length'] >= 12 else "[bold red]❌ Too short[/bold red]")
        
        console.print()
        console.print(table)
        
        while True:
            again = console.input("\n  [cyan]»[/cyan] Check another password? [y/n]: ").strip().lower()
            if again in ['y', 'n']:
                break
            console.print("  [bold red]❌ Please enter y or n.[/bold red]")
            
        if again == 'y':
            continue
        else:
            console.print("  [bold green]✅ Returning to main menu...[/bold green]")
            time.sleep(1)
            break

# ============================================================
# SECTION: MAIN ENTRY POINT
# ============================================================

def main() -> None:
    """Main program loop and exit handling."""
    try:
        show_banner()
        while True:
            console.print()
            choice = display_main_menu()
            
            if choice == '1':
                password_generator()
            elif choice == '2':
                password_checker()
            elif choice == '3':
                console.print("\n  [bold cyan]👋 Goodbye![/bold cyan]")
                break
            else:
                console.print("  [bold red]❌ Invalid choice. Try again.[/bold red]")
                
    except KeyboardInterrupt:
        console.print("\n  [bold cyan]👋 Goodbye![/bold cyan]")
        sys.exit(0)

if __name__ == "__main__":
    main()
