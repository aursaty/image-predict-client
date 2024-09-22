import requests
import typer
from pathlib import Path
# from client.utils import save_results

app = typer.Typer()

@app.command()
def predict(image_path: str):
    print(image_path)
    url = "http://localhost:8000/predict/"
    with open(image_path, "rb") as image_file:
        files = {"file": (Path(image_path).name, image_file, "image/jpeg")}
        response = requests.post(url, files=files)
        results = response.json()
        print(results)

if __name__ == "__main__":
    app()