# classification_models.py


import os
import cv2
import numpy as np
import pandas as pd
from tqdm import tqdm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score, classification_report
from joblib import dump


def extract_features(image_path):
    """Read an image and compute mean, std, and color histogram features."""
    img = cv2.imread(image_path)
    if img is None:
        return None

    img = cv2.resize(img, (128, 128))
    mean_val = np.mean(img)
    std_val = np.std(img)
    hist = cv2.calcHist([img], [0], None, [16], [0, 256]).flatten()
    features = np.concatenate(([mean_val, std_val], hist))
    return features


def build_feature_dataset(img_dir="data/images"):
    X, y = [], []
    all_imgs = [f for f in os.listdir(img_dir) if f.endswith(".png")]

    for f in tqdm(all_imgs, desc="Extracting image features"):
        path = os.path.join(img_dir, f)
        feats = extract_features(path)
        if feats is not None:
            X.append(feats)
            # For this assignment, we simulate 4 classes by splitting IDs
            # (since real labels aren’t provided)
            file_num = int(f.split("_")[1].replace("page1.png", ""))
            label = file_num % 4   # fake 4-category pattern
            y.append(label)

    X = np.array(X)
    y = np.array(y)
    return X, y


def train_models(X, y, output_dir="results/models"):
    os.makedirs(output_dir, exist_ok=True)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    models = {
        "SVM": SVC(kernel="linear", random_state=42),
        "SGD": SGDClassifier(random_state=42, max_iter=1000, tol=1e-3),
        "RandomForest": RandomForestClassifier(n_estimators=100, random_state=42),
        "MLP": MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=300, random_state=42),
    }

    for name, model in models.items():
        print(f"\n🔹 Training {name} ...")
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)
        print(f"{name} Accuracy: {acc:.4f}")
        print(classification_report(y_test, preds))

        dump(model, os.path.join(output_dir, f"{name}_model.joblib"))

    print(f"\nModels saved in: {output_dir}")


if __name__ == "__main__":
    X, y = build_feature_dataset()
    train_models(X, y)
