#!/bin/bash 

python3 extractor.py
python cleaner.py
python transformer.py
python loader.py
