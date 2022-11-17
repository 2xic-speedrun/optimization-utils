import requests

def send(host, loss=None, accuracy=None, metadata={}):
    requests.post(host,json={
        "loss": loss,
        "accuracy": accuracy,
        "metadata":metadata,
    })

if __name__ == "__main__":
    send("http://localhost:8080", loss=10)