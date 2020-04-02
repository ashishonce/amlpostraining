
import os
import json

from azureml.core import Workspace
from azureml.core.authentication import ServicePrincipalAuthentication

from azureml.core import Experiment
from fetchmetric import getMetrics
def get_spAuth(azure_credentials):
    sp_auth = ServicePrincipalAuthentication(
            tenant_id=azure_credentials.get("tenantId", ""),
            service_principal_id=azure_credentials.get("clientId", ""),
            service_principal_password=azure_credentials.get("clientSecret", "")
        )
    return sp_auth;

def main():
    azure_credentials = os.environ.get("INPUT_AZURECREDENTIALS", default='{}')
    azureml_workSpaceName = os.environ.get("INPUT_WORKSPACENAME", default=None)
    github_SHA = os.environ.get("INPUT_COMMIT_SHA", default="7a6fe10d22b5c44be55698f6d123c6480451e18b")

    if azureml_workSpaceName == None or azure_credentials == {}:
        print(" credentials empty or worksapce name can not be empty")
        return;
    ws = None;
    sp_auth = get_spAuth(azure_credentials)
    try:
        print("::debug::Loading existing Workspace")
        ws = Workspace.get(
            name=azureml_workSpaceName,
            subscription_id=azure_credentials.get("subscriptionId", ""),
            auth=sp_auth
        )
        print("::debug::Successfully loaded existing Workspace")
        print(ws)
        getMetrics(ws,experiment_name,{"github_SHA" : github_SHA});
    except Exception as e:
        
        print(" workspace doesn't exists or authentication error")

if __name__ == "__main__":
    main()