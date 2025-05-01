<h1 align="center">
  <a href="https://github.com/lorenzomatheo/guardiaoeleitoral">
  </a>
</h1>

<div align="center">
  Electoral Guardian
  <br />
  <a href="#about"><strong>Explore the documentation »</strong></a>
  <br />
  <br />
  <a href="https://github.com/lorenzomatheo/guardiaoeleitoral/issues/new?assignees=&labels=bug&template=01_BUG_REPORT.md&title=bug%3A+">Report a bug</a>
  ·
  <a href="https://github.com/lorenzomatheo/guardiaoeleitoral/issues/new?assignees=&labels=enhancement&template=02_FEATURE_REQUEST.md&title=feat%3A+">Request a feature</a>
  ·
  <a href="https://github.com/lorenzomatheo/guardiaoeleitoral/issues/new?assignees=&labels=question&template=04_SUPPORT_QUESTION.md&title=support%3A+">Ask a question</a>
</div>

<div align="center">
<br />

[![Project license](https://img.shields.io/github/license/lorenzomatheo/guardiaoeleitoral.svg?style=flat-square)](LICENSE)

[![Pull Requests welcome](https://img.shields.io/badge/PRs-welcome-ff69b4.svg?style=flat-square)](https://github.com/lorenzomatheo/guardiaoeleitoral/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22)
[![code with love by lorenzomatheo](https://img.shields.io/badge/%3C%2F%3E%20with%20%E2%99%A5%20by-lorenzomatheo-ff1414.svg?style=flat-square)](https://github.com/lorenzomatheo)
[![josiasbatista](https://img.shields.io/badge/%3C%2F%3E%20with%20%E2%99%A5%20by-josiasbatista-ff1414.svg?style=flat-square)](https://github.com/josiasdev)
[![matheusbittencourt](https://img.shields.io/badge/%3C%2F%3E%20with%20%E2%99%A5%20by-matheusbittencourt-ff1414.svg?style=flat-square)](https://github.com/mabitten)

</div>

<details open="open">
<summary>Contents</summary>

- [About](#about)
- [Tech Stack](#tech-stack)
- [Presentation](#presentation)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Support](#support)
- [Project Assistance](#project-assistance)
- [Contributing](#contributing)
- [Authors & Contributors](#authors--contributors)
- [Security](#security)
- [License](#license)
- [Acknowledgements](#acknowledgements)

</details>

---

## About

> The "Electoral Guardian" project was developed to automate the verification of the authenticity of electoral videos. It integrates various computer vision technologies and deepfake detection models, enabling the analysis of submitted videos and the generation of reports on their reliability.

> The main goal is to combat misinformation during the electoral period by saving time for journalists, fact-checkers, and voters through a centralized virtual assistant for analyzing suspicious content.

> The project was born out of the author's desire to create a socially impactful tool that uses artificial intelligence to promote information integrity.

### Tech Stack

> Programming Language: Python

> APIs: Hugging Face Transformers (ViT_Deepfake_Detection), WhatsApp Business API (simulated)

> Frameworks and Libraries:

> OpenCV,  
> PIL (Pillow),  
> Transformers (pipeline),  
> Requests,  
> LangChain (core for future integration),
> os
> shutil

> Infrastructure: Docker, ffmpeg (for media processing), integration with local files simulating input via WhatsApp

> Others: Docker, cURL, Flask and ngrok to host the webhooks

### Presentation
> Slide used in the demonstration video presentation [slides presentation](docs/slides.pdf).


## Getting Started

### Prerequisites

> Python 3.12
  Recommended for compatibility with torch, opencv-python, and other libraries.

> Hugging Face account with access to the Wvolf/ViT_Deepfake_Detection model
  Required to use the deepfake detection pipeline. 

> Dependencies installed via pip
> langgraph
> langsmith(for future monitoring of the agents)
> transformers
> pyngrok
> opencv-python
> Pillow
> flask
> python-dotenv
> pyngrok

### Installation

> **1. Clone the repository**

> Download or clone the repository containing the following project files:

```bash
git clone https://github.com/lorenzomatheo/guardiaoeleitoral
cd guardiaoeleitoral
```

> **Included files:**

> - electoralguardian.ipynb  
> - server.py  
> - LICENSE.txt
> - SECURITY.md
> - CONTRIBUTING.md  
> - requirements.txt  

> **2. ENV Configuration**

> Set the `API_INSTANCE_ZAPI`,`INSTANCE_TOKEN`,`PHONE_NUMBER`,`CLIENT_TOKEN`and `PORT` in your .env file with your keys:

```bash
API_INSTANCE_ZAPI = "<Z-API instance ID>"
INSTANCE_TOKEN = "<Instance token provided by Z-API>"
PHONE_NUMBER = "<WhatsApp phone number with country and area code, e.g., 5511999999999>"
CLIENT_TOKEN = "<Client token (separate from the instance, depending on Z-API>"
PORT = "<Port where your Flask application will run, e.g., 5001>"
```
All this informations you take here: https://app.z-api.io/

> **3. Install dependencies**

> Run locally:

```bash
! pip freeze > requirements.txt
! pip install -r requirements.txt
```
> **4. Run the server**

> Run in 2 different terminals:

```bash
ngrok http 5001
```
```bash
python server.py
```

The ngrok NEEDS to be in the same port of the Flask beacuse the Falsk server don't catch the webhook received from ngrok, and in the moment you restart the application, you need to paste the new "Forwarding" in the Z-API camp 'Upon receiving"

More about this: https://developer.z-api.io/

## Usage

> **Sending the media and executing the notebook**

> Just send the video for the contact who you scanned the QR Code in Z-Api instance web and execute the cells

## Roadmap

Check out the [open issues](https://github.com/lorenzomatheo/guardiaoeleitoral/issues) to see the list of proposed features (and known issues).

- [Top Feature Requests](https://github.com/lorenzomatheo/guardiaoeleitoral/issues?q=label%3Aenhancement+is%3Aopen+sort%3Areactions-%2B1-desc) (Add your 👍 to vote)  
- [Top Bugs](https://github.com/lorenzomatheo/guardiaoeleitoral/issues?q=is%3Aissue+is%3Aopen+label%3Abug+sort%3Areactions-%2B1-desc) (Add your 👍 to vote)  
- [Most Recent Bugs](https://github.com/lorenzomatheo/guardiaoeleitoral/issues?q=is%3Aopen+is%3Aissue+label%3Abug)

## Support

Contact the maintainer via one of the following channels:

- [GitHub Issues](https://github.com/lorenzomatheo/guardiaoeleitoral/issues/new?assignees=&labels=question&template=04_SUPPORT_QUESTION.md&title=support%3A+)  
- Contact options listed on this [GitHub profile](https://github.com/lorenzomatheo)

## Project Assistance

If you'd like to say **thanks** and/or support the active development of Electoral Guardian:

- Leave a [star on GitHub](https://github.com/lorenzomatheo/guardiaoeleitoral)  
- Tweet about Electoral Guardian  
- Write interesting articles about the project on [Dev.to](https://dev.to/), [Medium](https://medium.com/), or your personal blog  

Together we can make Electoral Guardian even **better**!

## Contributing

First of all, thank you for taking the time to contribute! Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contribution you make will benefit everyone and is **greatly appreciated**.

Please read our [contributing guidelines](docs/CONTRIBUTING.md) and thank you for being part of it!

## Authors & Contributors

The original setup for this repository was done by [Lorenzo Matheo](https://github.com/lorenzomatheo), [Josias Batista](https://github.com/josiasdev) and [Matheus Bittencourt](https://github.com/mabitten).

For a full list of all authors and contributors, see the [contributors page](https://github.com/lorenzomatheo/guardiaoeleitoral/contributors).

## Security

Electoral Guardian follows good security practices, but 100% security cannot be guaranteed.

Electoral Guardian is provided **"as is"**, without any **warranty**. Use at your own risk.

_For more information and to report security issues, please see our [security documentation](docs/SECURITY.md)._

## License

This project is licensed under the **MIT license**.

See the [LICENSE](LICENSE) file for more information.

## Acknowledgements

Thanks to the work of [Gartner](https://www.gartner.com/en) that made this idea possible.
