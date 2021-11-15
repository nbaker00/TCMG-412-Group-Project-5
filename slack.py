#send message to slack
@app.route("/slack-alert/<string:message>")
def sendslackmessage(message):
    #create the slack client
    import slack_sdk 
    from slack_sdk.errors import SlackApiError   
    try:
        client = slack_sdk.WebClient(token=os.environ['SLACK_TOKEN'])
    except:
        return jsonify(input=message, output=False, error='Could not talk to slack service'), 503
    
    #send slack the message
    try:
        response = client.chat_postMessage(channel="C011KJWHA22", text=message)
    except SlackApiError as e:
        return jsonify(input=message, output=False, error='there was a slack api error'), 500
        
    #check for success
    if response.status_code == 200:
        return jsonify(input=message, output=True)
    else:
        return jsonify(input=message, output=False, error='slack returns not 200 error'), 502
