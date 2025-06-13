# D:/script.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Giờ có thể import như trong src/
from src.database.base import Base

if Base:
    print ("true")
