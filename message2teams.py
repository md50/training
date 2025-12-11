import requests
import json

def send_teams_message(message):
    webhook_url = "https://defaultb22e8eaf1f9b40708b26fe63f9fc8f.e7.environment.api.powerplatform.com:443/powerautomate/automations/direct/workflows/bf0287d003d849119c73af6092b10942/triggers/manual/paths/invoke?api-version=1&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=rnBha0P3VseJyMrdkuwass_bR63nQgiadRpwgTfeCdE"
    payload = { "message": message }
    headers = { "Content-Type": "application/json" }

    response = requests.post(webhook_url, headers=headers, data=json.dumps(payload))
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")


send_teams_message("Test")

