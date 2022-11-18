import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "h2vJ937H5pAJq9TjZs1TKvsBeVKaTkrFIYx4QQpAOoQ-"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}


payload_scoring = {"input_data": [{"fields": [['f0','f1','f2','f3','f4','f5','f6']],
                                       "values": [[2014,6.7,7.5,203,6.857891819,0.1,27]]}]}

response_scoring = requests.post(
        'https://us-south.ml.cloud.ibm.com/ml/v4/deployments/68c0c00b-cf33-4ac9-a40f-e4835b4935e4/predictions?version=2022-11-18',
        json=payload_scoring,
        headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
#print(response_scoring.json())
pred=response_scoring.json()
output = pred['predictions'][0]['values'][0][0]
print("The predicted WQI is " +str(output))
