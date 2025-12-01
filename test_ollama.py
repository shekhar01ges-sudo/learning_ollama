import requests

BASE = "http://localhost:11434"  # or "https://ai.example.com" if using TLS reverse proxy

def generate(prompt: str, model: str = "llama3:latest"):
    url = f"{BASE}/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "max_tokens": 512
    }
    resp = requests.post(url, json=payload, timeout=300)
    resp.raise_for_status()
    return resp.json()

if __name__ == "__main__":
    out = generate("Write a short README for me.")
    print(out)