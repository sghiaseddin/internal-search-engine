#!/bin/bash

# === Clean and prepare build directory ===
echo "[BUILD] Cleaning build directory..."
rm -rf build
mkdir -p build/app

# === Copy required folders ===
echo "[BUILD] Copying directories..."
cp -r app/* build/app/
touch build/app/__init__.py

# === Convert notebook to Python with BUILD-filtered cells only ===
echo "[BUILD] Filtering notebook cells with #BUILD flag..."
jupyter nbconvert --to python search_engine.ipynb --output temp_converted

# Keep only lines under cells that start with '#BUILD'
awk '
    BEGIN { keep=0 }
    /^\#BUILD/ { keep=1; next }
    /^#/ && !/^#BUILD/ { keep=0 }
    { if (keep) print }
' temp_converted.py > build/app/search_engine.py
rm temp_converted.py

# === Copy start.py into build root ===
echo "[BUILD] Copying start.py..."
cp start.py build/

echo "[BUILD] Done. Project is built in ./build"