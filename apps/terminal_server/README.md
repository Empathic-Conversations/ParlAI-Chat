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
See configuration `YAML` files under the folder [config](./config/).

### __Control Models__
You should check the source code of chatbot agent defined in [`gpt3_render.py`](../../packages/ParlAI/parlai/agents/_custom/gpt3_render.py) when reading the config files to help you better understand how the configurations are consumed. You may notice the `RenderBot` key under `models` in the config files. This key is only used during bot creation. See `RenderBotChatTaskWorld.generate_world()` in [`worlds.py`](./src/worlds.py).

### __Execution Logic__
`ParlAI` rely on the notion of [`Worlds`](https://www.parl.ai/docs/tutorial_worlds.html). See [`worlds.py`](./src/worlds.py) on how the server process the incoming data and how a new (shared) model is created with new connection. We customized our own worlds for the EC2 study, and you should specify the world used in the config `YAML` file.
