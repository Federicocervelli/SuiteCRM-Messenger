import requests
from util import statics

# API endpoint for the module you want to update
url = "https://your-suitecrm-instance/api/8/modules/{module_name}/{record_id}"

# Set the module name and record ID you want to update
module_name = "accounts"
record_id = "12345"

# Construct the request payload with the field(s) you want to update
payload = {
    "field_name": "new_value",
    "another_field_name": "another_value"
}

# Set the headers and authentication token
headers = {
    "Authorization": "Bearer your_auth_token",
    "Content-Type": "application/vnd.api+json"
}

# Make the PATCH request
response = requests.patch(url.format(module_name=module_name, record_id=record_id), json=payload, headers=headers)

# Check the response status code
if response.status_code == 200:
    print("Module entry updated successfully.")
else:
    print("Failed to update module entry:", response.text)