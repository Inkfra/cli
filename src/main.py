import typer
import requests

api_url = "http://localhost:8000/api/v1"

app = typer.Typer()
get_app = typer.Typer()
app.add_typer(get_app, name="get")

@get_app.command()
def devices():
    response = requests.get(f"{api_url}/devices/get")
    if response.status_code == 200:
        devices = response.json().get("devices", [])
        for device in devices:
            print(f"{device[1]}")
    else:
        print(f"Error fetching devices: {response.status_code}")

if __name__ == "__main__":
    app()