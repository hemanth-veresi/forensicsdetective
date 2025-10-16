# SETUP
# create virtualenv
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
# install libreoffice (for PDF conversions)
sudo apt-get update && sudo apt-get install -y libreoffice libreoffice-writer poppler-utils