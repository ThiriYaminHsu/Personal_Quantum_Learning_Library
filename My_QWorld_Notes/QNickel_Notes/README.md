Nickel is QWorld's intermediate-level tutorial on conventional quantum algorithms.

## Installation

To work with these jupyter notebooks, you need a number of packages. The following instructions ensure that the python verson and package versions are consistent and work with the notebooks.

1. Download this repository and extract it somewhere.

Then either use Conda, venv or virtualenv as follows.

### Conda (Recommended)

The following two steps are for installing the required packages.

1. Open a terminal or command prompt at the directory where you extracted the files.
2. Run the following command to create a new Conda environment and install all necessary packages.

```bash
conda env create -f environment.yml
```

The following steps should be followed every time you want to work on the notebooks.

1. Activate the Conda environment.

```bash
conda activate nickel
```

After activation, your command prompt or terminal prompt should change to indicate that you are now working within the virtual environment. 

2. You can now launch jupyter notebook.

```bash
jupyter notebook
```

3. Deactivate the Conda environment when you're done.

```bash
conda deactivate
```


### Using venv or virtualenv

1. Make sure you are using Python 3.10.8.
2. Open a terminal or command prompt at the directory where you extracted the files.
3. Run one of the following commands (depending on whether you want to use venv or virtualenv) to create a virtual environment.

```bash
# create environment using venv
python -m venv nickelenv
# OR create environment using virtualenv
pip install virtualenv
virtualenv nickelenv
```

4. Activate the virtual environment.

On Windows
```bash
nickelenv\Scripts\activate
```

On macOS or Linux:
```bash
source nickelenv/bin/activate
```

After activation, your command prompt or terminal prompt should change to indicate that you are now working within the virtual environment.

5. Install packages using pip. 

```bash
pip install -r requirements.txt
```

If you are a Mac OS user you might need to install the qiskit[visualization] in the following way
```bash
pip install 'qiskit[visualization]'
```

6. You can now launch jupyter notebook.

```bash
jupyter notebook
```

7. Deactivate the Conda environment when you're done.

```bash
conda deactivate
```

Every time you work on the notebooks, you should reexecute steps 4, 6 and 7, remembering to switch to the directory where you created the virtual environment.

### Binder 

You may launch Nickel in the cloud with binder but **please be aware of that**
- each time a new session is created, which takes some time to be initiated, and all changes are lost when ending the session; and,
- the session might be terminated if a new tab is not opened within 10 minutes.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gl/qworld%2Fnickel/HEAD?urlpath=lab/tree/content.ipynb) 


