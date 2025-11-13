import requests

def save_webpage_title(url, output_file):
    response = requests.get(url)
    html = response.text

    # extract <title>...</title>
    start = html.find("<title>") + len("<title>")
    end = html.find("</title>")
    title = html[start:end]

    with open(output_file, "w") as f:
        f.write(title)

    print("✔ Title saved:", title)

# Example:
save_webpage_title("https://example.com", "title.txt")
