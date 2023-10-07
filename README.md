# __Customized `ParlAI` for Empathic Conversation 2.0__
## __What's `ParlAI`__
[`ParlAI`](https://parl.ai/docs/tutorial_basic.html) (pronounced "par-lay") is a framework for dialogue research and training of AI models in conversational settings developed by Facebook AI Research (FAIR), which is a part of Meta (previously known as Facebook, Inc.). It aims to provide the research community with a consistent platform for experimenting with dialogue models, thereby fostering reproducibility and collaboration. Since its introduction, ParlAI has become an influential tool in the conversational AI research domain.

## __`ParlAI` Core Concepts__
[The introduction](https://parl.ai/docs/tutorial_basic.html) gives a comprehensive overview of the core concepts employed by `ParlAI` and you should at least read through this documentation. One should pay particular attention to the notion of [`Worlds`](https://parl.ai/docs/tutorial_basic.html#worlds) and [`Agents`](https://parl.ai/docs/tutorial_basic.html#agents) because here are where most customization happens. Further, one can read [this tutorial](https://parl.ai/docs/tutorial_worlds.html#introduction) about parameter-sharing (across multiple chat sessions) to understand how a chatbot is initialized whe a chat server spins up. On a high level, when we start a server, a "parent" chatbot is initialized according to configuration, e.g., model weights are loaded into the memory. When the server receives an incoming connection (`ParlAI` handles this with [`tornado`](https://www.tornadoweb.org/en/stable/)), it will instantiate a copy from this initial parent, and one can customize this init-from-share process by overwriting the logic of `Agent.share(self)` method and the `shared` parameter of `Agent.__init__(self, opt, shared)`.

## __What's in This Repository__
### __`ParlAI` Customization__
Archive for `ParlAI` with customized chatbot implemented for the EC2 project, stored under [`packages/ParlAI`](./packages/ParlAI/). Specifically, one can go directly to [this folder](./packages/ParlAI/parlai/agents/_custom/) for customized GPT-based style transfer implementations.

### __Simple Terminal Chatbot Server__
We modified the original example from `ParlAI` into a simple terminal-based chatbot server that can process in-coming connections from chatting clients or other `websocket` connections. Please read the [`README.md`](./apps/terminal_server/README.md) for more details about how to use the code.

### __Local Search Engine__
The chatbot used by the EC2 project is based on [`BlenderBot2`](https://ai.meta.com/blog/blender-bot-2-an-open-source-chatbot-that-builds-long-term-memory-and-searches-the-internet/), which requires a search-engine as an augmented knowledge base for response generation. You may refer to [the source code](./packages/SearchEngine/main.py) for implementation details. You can also simply refer to [this script](./scripts/start-search-engine.sh) for how to start the search engine. [The documents](./packages/SearchEngine/data/title_text.csv) are already pre-indexed under [`indexdir`](./packages/SearchEngine/indexdir/). One may refer to [this notebook](./packages/SearchEngine/notebooks/whoosh_add_docs.ipynb) for how to rebuild the index.

### __Browser-based Chatting Client__
One may use a [browser-based chat client](./apps/browser_client/main.py) during the development stage to see if the chatbot works properly. Please read the [`README.md`](./apps/browser_client/README.md) for more details about how to use the code.

## __Scripts__
__All scripts assumes running under the project folder, i.e., the folder where this `README.md` file resides.__

### __Start `BlenderBot2`__
Please refer to [this script](./scripts/start-bb2.sh) for how to host `BlenderBot2` via a [`terminal_server`](./apps/terminal_server/). 

### __Environment Creation__
We assume environment management using `conda`. To create the environment for `BlenderBot2` hosting, one can refer to [this environment creation script](./scripts/create-environment.sh). This script installs dependencies for running `BlenderBot2` and its accompany local search engine. You will encounter version conflicts during the installation process but the conflicts does not seem to substantially affect the normal usage. We ran the [`terminal_server`](./apps/terminal_server/) with `Python 3.10` and it seems to work just fine.
