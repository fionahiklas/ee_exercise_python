import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

print("Full path: %s" %(sys.path))

# Import the application code
import fizzbuzz

