# CELLxGENE Deep Dive Workshop

Site here: https://maximilianlombardo.github.io/cxg-deep-dive-workshop/intro.html

## Usage

### Building the book

If you'd like to develop and/or build the CELLxGENE Segmentation Course book, you should:

1. Clone this repository
2. Run `pip install -r requirements.txt` (it is recommended you do this within a virtual environment)
3. (Optional) Edit the books source files located in the `content/` directory
4. Run `jupyter-book clean content/` to remove any existing builds
5. Run `jupyter-book build content/`

A fully-rendered HTML version of the book will be built in `content/_build/html/`.

## Code of Conduct

This project adheres to the Contributor Covenant [code of conduct](https://github.com/chanzuckerberg/.github/blob/master/CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to [opensource@chanzuckerberg.com](mailto:opensource@chanzuckerberg.com).

## License

This website and all its contents are made available under the MIT License.

Copyright (c) 2022 Chan Zuckerberg Initiative

## Reporting Security Issues

If you believe you have found a security issue, please responsibly disclose by contacting us at [security@chanzuckerberg.com](mailto:security@chanzuckerberg.com).

## Credits

The CELLxGENE team developed this course based off of Napari's segmentation workshop: https://chanzuckerberg.github.io/napari-segmentation-workshop/intro.html

This project is created using the excellent open source [Jupyter Book project](https://jupyterbook.org/) and the [executablebooks/cookiecutter-jupyter-book template](https://github.com/executablebooks/cookiecutter-jupyter-book).
