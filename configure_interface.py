#!/usr/bin/env python3
"""
Goose Interface Configuration Tool

This script allows users to change their interface mode after initial setup.
"""

import yaml
from pathlib import Path
import sys

# Define the persistent path for user preferences
PERCEPTION_DIR = Path("~/.local/share/goose-perception").expanduser()
PREFS_PATH = PERCEPTION_DIR / "user_prefs.yaml"

def load_user_prefs():
    """Load user preferences from the YAML file."""
    if not PREFS_PATH.exists():
        return {}
    try:
        with open(PREFS_PATH, "r") as f:
            return yaml.safe_load(f) or {}
    except (yaml.YAMLError, IOError) as e:
        print(f"Error loading user preferences: {e}")
        return {}

def save_user_prefs(prefs):
    """Save user preferences to the YAML file."""
    try:
        PERCEPTION_DIR.mkdir(parents=True, exist_ok=True)
        with open(PREFS_PATH, "w") as f:
            yaml.dump(prefs, f, default_flow_style=False)
        print("✅ Preferences saved successfully!")
    except IOError as e:
        print(f"❌ Error saving user preferences: {e}")

def show_current_config():
    """Show the current interface configuration."""
    prefs = load_user_prefs()
    
    print("\n🪿 Current Goose Interface Configuration:")
    print("=" * 45)
    
    interface_mode = prefs.get('interface_mode', 'floating')
    
    print(f"Interface Mode: {interface_mode}")
    
    if interface_mode == 'menubar':
        print("🍎 Menu Bar Mode: Goose lives in your menu bar with popup window")
    else:
        print("🪟 Floating Mode: Traditional floating avatar")
    
    print()

def configure_interface():
    """Interactive interface configuration."""
    print("\n🪿 Goose Interface Configuration")
    print("=" * 35)
    print("\nChoose your preferred interface mode:")
    print("1. Floating Avatar (traditional)")
    print("2. Menu Bar Icon (minimal)")
    print("3. Show current configuration")
    print("4. Exit")
    
    while True:
        try:
            choice = input("\nEnter your choice (1-4): ").strip()
            
            if choice == "1":
                set_floating_mode()
                break
            elif choice == "2":
                set_menu_bar_mode()
                break
            elif choice == "3":
                show_current_config()
                continue
            elif choice == "4":
                print("👋 Goodbye!")
                sys.exit(0)
            else:
                print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            sys.exit(0)
        except EOFError:
            print("\n👋 Goodbye!")
            sys.exit(0)

def set_floating_mode():
    """Set floating avatar mode."""
    prefs = load_user_prefs()
    prefs['interface_mode'] = 'floating'
    save_user_prefs(prefs)
    
    print("\n🪟 Floating Avatar Mode enabled!")
    print("The traditional floating avatar will appear on your screen.")

def set_menu_bar_mode():
    """Set menu bar mode."""
    prefs = load_user_prefs()
    prefs['interface_mode'] = 'menubar'
    save_user_prefs(prefs)
    
    print("\n🍎 Menu Bar Mode enabled!")
    print("Goose will appear as an icon in your Mac menu bar.")
    print("Right-click the icon to access features.")

def main():
    """Main function."""
    print("🪿 Goose Interface Configuration Tool")
    
    # Check if preferences file exists
    if not PREFS_PATH.exists():
        print("\n⚠️  No preferences file found.")
        print("Please run Goose first to complete initial setup.")
        sys.exit(1)
    
    # Show current configuration
    show_current_config()
    
    # Run configuration menu
    configure_interface()

if __name__ == "__main__":
    main() 