import requests
import typer
from pathlib import Path
from utils import extract_and_store_predictions, save_image

app = typer.Typer()

@app.command()
def predict(image_path: str):
    url = "http://127.0.0.1:8000/predictClassesJson/"
    with open(image_path, "rb") as image_file:
        files = {"file": (Path(image_path).name, image_file, "image/jpg")}
        response = requests.post(url, files=files)
        response.raise_for_status
        results = response.json()
        if 200 <= response.status_code <= 299:
            extract_and_store_predictions(results['result'])
    
    url = "http://127.0.0.1:8000/predictClassesOnImage/"
    with open(image_path, "rb") as image_file:
        files = {"file": (Path(image_path).name, image_file, "image/jpg")}
        response = requests.post(url, files=files)
        response.raise_for_status
        if 200 <= response.status_code <= 299:
            save_image(response.content)

if __name__ == "__main__":
    app()
