# UnityMLPySocket

UnityMLPySocket is an open-source project that demonstrates how to perform local machine learning (ML) inference with Unity using a Python socket server. The project consists of a simple client-server architecture where a Unity application communicates with a Python server running a pre-trained ML model. This serves as a resource for game developers and ML practicioners.

## Table of Contents

- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [Usage](#usage)
    - [Running the Server](#running-the-server)
    - [Running the Unity Client](#running-the-unity-client)
- [Example: Sentiment Analysis](#example-sentiment-analysis)
- [Open Source AI Game Jam](#open-source-ai-game-jam)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Getting Started

### Prerequisites

- Python 3.6+
- Unity 2020.3+
- [🤗 Transformers](https://huggingface.co/docs/transformers/index)
    ```
    pip install transformers
    ```

### Installation

1. Clone this repository
    ```
    git clone https://github.com/dylanebert/UnityMLPySocket.git
    ```
2. Open the `Unity` folder with the Unity Editor

## Usage

### Running the Server

1. Open the repository in your preferred terminal / IDE
2. Navigate to the server directory
    ```
    cd UnityMLPySocket/Server
    ```
3. Start the server
    ```
    python server.py
    ```

If working correctly, the server should display `Listening on port 5000...`

### Running the Unity Client

1. Open the `UnityProject` folder with the Unity Editor
    - Alternatively, copy the `Assets/UnityMLPySocket` folder to your own Unity project
2. Open the sample scene located at `Assets/UnityMLPySocket/Examples/Scenes/SimpleExample`
3. Press the play button to start the client

If working correctly, the editor should log the message `Received response: {"label": "POSITIVE", "score": 0.9997431635856628}`

## Example: Sentiment Analysis

This project comes with an example that demonstrates sentiment analysis, where the text from Unity is sent to the Python server, then the server predicts the sentiment of the text using a pre-trained model hosted on Hugging Face.

Refer to the code in `PythonServer/scripts/example_model.py` for the server-side implementation. This can be easily replaced with your own ML code for any model hosted on [Hugging Face](https://huggingface.co/models), or your own custom ML code. While the provided example is intended only for inference, it can easily be adapted for training and fine-tuning.

Refer to the code in `Unity/Assets/UnityMLPySocket/Examples/Scripts/SimpleExample.cs` for the client-side implementation. This connects to the client and sends a `Hello World!` message.

> ⚠️ Note: This is a blocking implementation that will block the main Unity thread until a response is received. A multithreaded or coroutine-based solution may be preferred for non-blocking requests.

## Open Source AI Game Jam

Join the upcoming Open Source AI Game Jam where we'll be exploring cutting-edge applications of AI in game development! [Sign up here!](https://itch.io/jam/open-source-ai-game-jam)

[![Open Source AI Game Jam](https://github.com/huggingface/blog/blob/main/assets/145_gamejam/thumbnail.png?raw=true)](https://itch.io/jam/open-source-ai-game-jam)

## Contributing

Your contributions are greatly appreciated! Please follow these steps:

1. Fork the project
2. Create your feature branch `git checkout -b feature/MyFeature`
3. Commit your changes `git commit -m "my cool feature"`
4. Push to the branch `git push origin feature/MyFeature`
5. Open a Pull Request

## License

Distributed under the Apache 2.0 License. See `LICENSE` for more information.

## Contact

To participate in the community, join the [Hugging Face Discord](https://hf.co/join/discord). To contact the repo owner directly, ping me @IndividualKex or email me directly (email in discord bio).