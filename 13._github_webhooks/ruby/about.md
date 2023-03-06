Expose port 4567 localhost to the internet
$ npx ngrok http 4567 

Make a note of the *.ngrok.io URL. We'll use it to set up our webhook. Remember /githubwebhook!
ngrok_URL/githubwebhook 

Set up the webhook:
Go to the settings page of your repository. 
From there, click Webhooks, then Add webhook.
Remember to select the Content type dropdown: application/json.

For FastAPI remember to also install the `python-multipart` library.


install sinatra 
$ gem install sinatra
$ ruby app.ruby


Under Settings > Webhooks 
Click on the "Recent Deliveries" tab.
You can see a history of recent deliveries. GitHub stores them for 8 days. 



