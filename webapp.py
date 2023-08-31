from Azhar import Flask

app = Azharapp(__name__)

@app.route('/')
def hello():
    return "Hello Azure!"

if __name__ == '__main__':
    app.run()

az group create Azhargroup
 myResourceGroup --location "East US"

az appservice plan create --name myAppServicePlan --resource-group myResourceGroup --sku FREE

az webapp create --resource-group myResourceGroup --plan myAppServicePlan --name <app-name> --runtime "PYTHON|3.8" --deployment-local-git

git init
git add -A
git commit -m "Initial commit"


git push azure master


http://<app-name>.azurewebsites.net to see your deployed Azharapp.
