import requests
import json

# Prepare request for authorization token from tenant.
tenant_url = "https://login.microsoftonline.com/" + "TENANT" + ".onmicrosoft.com/oauth2/v2.0/token"
data = {
        "grant_type": "client_credentials",
        "client_id": "APP_ID",
        "scope": "https://graph.microsoft.com/.default",
        "client_secret": "SECRET",
}

# Execute token request
request_token = requests.post(tenant_url, data=data)
token = request_token.json().get("access_token")


# Prepare query
example  = "https://graph.microsoft.com/v1.0/" + "TENANT.TLD" + "/groups/"

headers = {
        "Authorization": "Bearer {}".format(token)
}

# Execute query
query_example = requests.get(example, headers=headers)

# Parse results
parsed_json  = json.loads(query_example.text)

# Print results
print(json.dumps(parsed_json, indent = 4, sort_keys = True))
