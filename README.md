
===
## Project Information
- Title:  `Google's BARD model for consumption through API`


## Install & Dependence
- python 3.10
- Docker


## Use
- using python
  ```
  python3 pip install -r requirements.txt
  python3 -m uvicorn app:app --host 0.0.0.0 --port 8080 --reload --timeout-keep-alive 600
  ```
- using docker
  ```
  docker build -t bard:latest .
  docker run -d -p 8080:80 bard:latest
  ```
## Execute

- using python
  ```
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

  ```

## Directory Hierarchy
```
|—— .gitignore
|—— Dockerfile
|—— LICENCE
|—— app.py
|—— readme.MD
|—— requirements.txt
```

## References
- [source](https://github.com/dsdanielpark/Bard-API)
  
## License
- MIT
