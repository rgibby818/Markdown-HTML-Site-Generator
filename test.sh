# Changed from this:
# python3 -m unittest discover -s src/ src/tests

# To this to allow tests to be inside their own directory
PYTHONPATH=src python3 -m unittest discover -s src/ src/tests