# Contributing to Prime Analysis Toolkit

We welcome contributions of all kinds, whether it's fixing bugs, adding new features, improving documentation, or anything else that makes Prime Analysis Toolkit even better!

## 1. Fork the Repository

Start by forking the repository to your own GitHub account. This creates a copy under your account, where you can make changes freely.

## 2. Clone Your Fork

Clone your fork to your local machine:

```bash
git clone https://github.com/<your-username>/prime_analysis_toolkit.git
cd prime_analysis_toolkit
```

## 3. Create a Branch

Create a new branch for your work. Use a descriptive name, for example:

```bash
git checkout -b feature/add-new-command
# or
git checkout -b fix/issue-123
```

## 4. Install Dependencies

Install the toolkit and its development requirements in editable mode:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

Alternatively, use the requirements files:

```bash
pip install -r requirements.txt
pip install -r dev-requirements.txt
```

## 5. Make Your Changes

* Follow existing code style and conventions (PEP 8, type hints, docstrings).
* Add or update tests in the `tests/` directory.
* Ensure all tests pass:

  ```bash
  pytest
  ```

## 6. Commit Your Work

Write clear, concise commit messages. For example:

```
feat(vowel): support custom vowel mapping rules
fix(factor): handle large integers without overflow
docs(readme): correct usage example for CLI
```

Use `git add` to stage your changes and then:

```bash
git commit -m "<type>(<scope>): <short description>"
```

## 7. Push and Open a Pull Request

Push your branch to your fork:

```bash
git push -u origin feature/add-new-command
```

Then open a pull request against `main` in the original repository:

1. Describe your changes and why they’re needed.
2. Reference any related issues (e.g., `Closes #123`).
3. Ensure all CI checks pass.

## 8. Address Feedback

We may request changes or clarifications. Please respond promptly by updating your branch. When all feedback is addressed and checks are green, your PR will be merged.

---

Thank you for contributing! We appreciate your time and effort in improving Prime Analysis Toolkit.

## License for Contributions

By submitting a pull request to this repository, you agree that your contributions will be licensed under the Apache License 2.0, and you warrant that you have the right to grant this license. Please ensure any third-party code you add is compatible with Apache 2.0.
