# SETUP

Environment (Colab recommended):
1. Open a new Colab notebook.
2. Mount Google Drive if you want persistent storage:
   from google.colab import drive
   drive.mount('/content/drive')

3. Install dependencies (run in Colab cell):
!pip install -r requirements.txt

4. Example workflow:
 - Run src/data_generation.py to create small test dataset (set n=50)
 - Run src/image_conversion.py to create images
 - Run src/classification.py to train classifiers
 - Run src/analysis.py to produce metrics and confusion matrices
