# DiffGen

### Overview

DifGen is an innovative tool designed to streamline the development workflow by automatically generating meaningful commit messages and pull request descriptions from git diffs. Leveraging the power of advanced AI, DifGen analyzes the changes in your code to create concise, informative summaries that capture the essence of each update, helping teams to understand code modifications quickly and improving the documentation process.

### Why DiffGen?

DifGen offers significant value to developers and teams by:

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
git clone https://github.com/yourusername/DifGen.git
cd DifGen
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

4. Configuration

- Create a `.env` file in the root directory.
- Add your OpenAI API key: `OPENAI_API_KEY=your_api_key_here`

### Usage

1. Navigate to Your Git Repository
    - Ensure you're in the root directory of the Git repository you want to analyze.

2. Run DifGen

```
python difgen.py
```

Follow any on-screen instructions to select the diffs or commits you wish to analyze.

### Contributing

We welcome contributions to DifGen! If you have suggestions for improvements or bug fixes, please open an issue or pull request.

### License

DifGen is released under the MIT License. See the LICENSE file for more information.

### Acknowledgments

This project utilizes OpenAI's API for generating content based on code diffs.

Thanks to all contributors and users of DifGen for your support and feedback.