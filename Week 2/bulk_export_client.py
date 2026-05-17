import time
import requests

FHIR_BASE_URL = "http://localhost:8080/fhir"

def start_bulk_export():
    url = f"{FHIR_BASE_URL}/Patient/$export"
    headers = {
        "Accept": "application/fhir+json",
        "Prefer": "respond-async"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 202:
        print("Bulk export was not accepted.")
        print("Status:", response.status_code)
        print(response.text)
        return None

    content_location = response.headers.get("Content-Location")
    print("Export started.")
    print("Status URL:", content_location)
    return content_location

def poll_export_status(status_url):
    headers = {
        "Accept": "application/fhir+json"
    }

    while True:
        response = requests.get(status_url, headers=headers)

        if response.status_code == 202:
            print("Export still processing...")
            time.sleep(5)

        elif response.status_code == 200:
            print("Export complete.")
            return response.json()

        else:
            print("Unexpected status:", response.status_code)
            print(response.text)
            return None

def download_ndjson_files(output):
    counts = {}

    for item in output.get("output", []):
        resource_type = item.get("type")
        file_url = item.get("url")

        print(f"Downloading {resource_type}: {file_url}")

        response = requests.get(file_url)

        if response.status_code == 200:
            lines = response.text.strip().splitlines()
            counts[resource_type] = len(lines)

            filename = f"{resource_type}.ndjson"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(response.text)

        else:
            print("Failed to download:", file_url)

    return counts

if __name__ == "__main__":
    status_url = start_bulk_export()

    if status_url:
        result = poll_export_status(status_url)
        if result:
            counts = download_ndjson_files(result)
            print("\nRecord counts by resource type:")
            for resource_type, count in counts.items():
                print(resource_type, count)