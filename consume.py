import requests

url = "http://localhost:8080/ask"
session_id ="XXXX" #use your cookie value for __Secure-1PSID


payload = {
    "session_id": session_id,
    "message": "Cual es el centro de Chile?"
}
response = requests.request("POST", url, json=payload)



print("Status Code: ", response.status_code)
print("JSON Response: ", response.text)



"ZAirF-Ur-UgrJjsy7JQtpdycxIvG1pX_KucTypvPp5dXMPbNggOBBbO_x6MREM5OXUJ4kQ."