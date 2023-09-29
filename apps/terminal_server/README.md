# __Terminal Chat__
This allows you to participate in a ParlAI world as an agent using the terminal.
This extends the `websocket` chat service implementation to run a server locally,
which you can send and receive messages from using the terminal.

## __Run__
Start the bot as follows,
```
python main.py --config < ParlAI_config > --port < Listen_port >
```
The default port is `34596`. So, to connect to the chatbot, one should connect to `localhost:34596`. If the bot is hosted on a cloud instance, say GCP, one should ping the public IP of the instance at port `34596`.

## __Config__
See configuration `YAML` files under the folder [config](./config/) for how you can control the model loaded.
