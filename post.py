import requests
import json

json_file = open("matt_obrien_resume.json")
write_data = json.load(json_file)

# Ensure JSON loaded
print(write_data)

end_point = 'https://contact.plaid.com/jobs'
r = requests.post(url = end_point, json = test)

print(r.status_code)
print(r.reason)