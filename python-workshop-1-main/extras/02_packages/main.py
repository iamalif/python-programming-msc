"""
main.py - Demonstrates different ways to import from packages
=============================================================
Run this file: python main.py
"""

print("=== Method 1: Full import path ===")
print()
import science.physics.display
science.physics.display.show_info()

print()
print("=== Method 2: Import with alias ===")
print()
import science.chemistry.display as chem
chem.show_info()

print()
print("=== Method 3: Import function directly ===")
print()
from science.biology.display import show_info
show_info()

print()
print("=== Method 4: Import function with alias ===")
print()
from science.physics.display import show_info as physics_info
physics_info()
