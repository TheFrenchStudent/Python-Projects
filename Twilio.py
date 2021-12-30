# Programme utilisant la méthode REST API pour envoyer un message via Twilio.
# Nous pouvons également mettre les variables account_sid et auth_token dans un autre fichier qui sera caché dans notre repository GitHub afin de mieux sécuriser notre code.

from twilio.rest import Client

account_sid = "ACe76c6715054cc89db57f7699b16d8985"
auth_token = "cbce417d3cc1281a7bd8559ee8cb28b0"

Client(account_sid, auth_token)

Client.message.create(
    to="...",
    from_="...",
    body="This is our first message"
)
