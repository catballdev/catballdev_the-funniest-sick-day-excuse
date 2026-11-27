#!/usr/bin/env python3
"""
make.fun entry: The Funniest Sick-Day Excuse

Reads line.txt and writes its exact contents to entry.txt in the
output directory (honouring MAKEFUN_OUTPUT_DIR or defaulting to /output).
"""

import os

# Read the sick-day excuse from line.txt (UTF-8, one straight-line excuse)
with open("line.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Determine output directory from environment variable, default to /output
output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Write entry.txt with the exact contents of line.txt
output_path = os.path.join(output_dir, "entry.txt")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(content)

# Set file permissions to 0644 (readable by everyone)
os.chmod(output_path, 0o644)