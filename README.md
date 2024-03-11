<img src="https://github.com/redroostertech/DiFFGEN/assets/8765750/93a1a122-e772-480d-b5cd-3edd51ac285e"
     alt="logo"
     height="225" />
# DiFFGEN

### Overview

DiFFGEN is an innovative tool I developed to deepen my understanding of both Python programming and working with OpenAI. It aims to streamline the development workflow by automatically generating meaningful commit messages and pull request descriptions from git diffs. Leveraging the power of AI, DiFFGEN analyzes the changes in your code to create concise, informative summaries that capture the essence of each update. This project began as a personal endeavor driven by a desire to enhance my skills and knowledge in Python and AI technologies, while also addressing a practical need in the software development process. Through working on DiFFGEN, I've gained valuable insights into both the technical aspects of coding and the applications of artificial intelligence in real-world scenarios. 

### Why DiffGen?

DiFFGEN offers significant value to developers and teams by:

- **Saving Time**: Automates the generation of commit messages and PR descriptions, freeing up developers to focus on coding.
- **Improving Clarity**: Generates clear and concise summaries of changes, making it easier for team members to understand the context and impact of modifications.
- **Enhancing Collaboration**: With better documentation of changes, teams can collaborate more efficiently, leading to higher quality code and faster project progression.
- **Streamlining Workflows**: Integrates into existing development workflows, supporting a seamless transition and immediate productivity gains.

### Getting Started

**Prerequisites**

1. Git installed on your system
2. Python 3.6 or higher
3. Access to OpenAI's API (API key required)

### Installation

1. Clone the Repository

```
git clone https://github.com/yourusername/DiFFGEN.git
cd DiFFGEN
```
2. Set up a Virtual Environment (Optional)

```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install Dependencies

```
pip install -r requirements.txt
```

or 

```
./init_repo.sh
```

4. Configuration

- Create a `.env` file in the root directory.
- Add the following values:

```
PROMPT_PATH=source/prompt_v2.txt <- Provided prompt or create your own!
OPENAI_ENGINE=text-davinci-003
OPENAI_API_KEY=123456789
ENV=LOCAL <- More so for logging
```

### Usage

1. Navigate to Your Git Repository
    - Ensure DiFFGEN is located in the root directory of the Git repository you want to analyze.

2. Run DiFFGEN

```
python3 source/commit_generator.py
```

or

```
./commit.sh
```

Follow any on-screen instructions to select the diffs or commits you wish to analyze.

### Contributing

We welcome contributions to DiFFGEN! If you have suggestions for improvements or bug fixes, please open an issue or pull request.

### License

DiFFGEN is released under the MIT License. See the LICENSE file for more information.

### Acknowledgments

This project utilizes OpenAI's API for generating content based on code diffs.

Thanks to all contributors and users of DiFFGEN for your support and feedback.
