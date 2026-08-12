import urllib.request
import os

url = "https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/concrete.csv"
target_dir = r"c:\Users\swaya\OneDrive\Documents\Codetech\concrete_strength_prediction\data"
target_file = os.path.join(target_dir, "concrete.csv")

print(f"Downloading Concrete dataset from {url}...")
urllib.request.urlretrieve(url, target_file)
print(f"Dataset successfully downloaded and saved to {target_file}")
