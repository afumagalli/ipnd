from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACb211f8a7a342fa8e895d128c6086e97c"
auth_token  = "33181ad54d30a1e474baa07af7f56920"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Hey Anthony",
    to="+16193419571",    # Replace with your phone number
    from_="+14193181672") # Replace with your Twilio number
print message.sid