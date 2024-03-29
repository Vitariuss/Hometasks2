from zeep import Client, Settings
import yaml

with open('NewNew\config.yaml') as f:
    data = yaml.safe_load(f)

print(data)

def check_word(word):
    url = data["url"]
    settings = Settings(strict=False)
    client = Client(wsdl=url, settings=settings)
    # print(client.service.checkText("cloun")[0]['s']) 
    return client.service.checkText(word)[0]['s']