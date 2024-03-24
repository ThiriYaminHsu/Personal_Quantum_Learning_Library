# QWorld's Nickel
Welcome to QWorld's Nickel!


Nickel is QWorld's intermediate level tutorial on conventional quantum algorithms.

## Installation

In order to work with these jupyter notebooks, you need a number of packages. The following instructions ensure that the python verson and package versions are consistent and work with the notebooks.

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

## Credits

Most of the <font style="color: #A9A9A9;"><b><i>Nickel</i></b></font> is prepared under the project QPool2019 [GitLab repository](https://gitlab.com/qkitchen/qpool2019) in 2019-2020 and it is expected to have contributions from public as well. 

We would like to thank participants of the QSilver Revision Week organized in January 2021 and the participants of the QSilver Pilot Workshop organized in April 2021 for revising the material. We would like to thank Yasir Ölmez for his technical help in finalizing the notebooks.


### Conventional Quantum Algorithms

This part is mostly developed collaboratively by <a href="https://qworld.net/qturkey/" target="_blank">QTurkey</a>. The contributors are Arda Çınar, Berat Yenilen, Cenk Tüysüz, <a href="https://www.cmpe.boun.edu.tr/~ozlem.salehi/" target="_blank">Dr. Özlem Salehi</a> ([IITiS PAN](https://iitis.pl/en/)), and Utku Birkan. Simon's Algorithm notebook is developed by Vishal Bapje and Kenneth Isamande and revised by <a href="https://www.cmpe.boun.edu.tr/~ozlem.salehi/" target="_blank">Dr. Özlem Salehi</a>. 

### Solving Max-Cut problem using Grover's Search

This section in prepared by [Dr. Adam Glos](https://iitis.pl/en/person/aglos) ([IITiS PAN](https://iitis.pl/en/), [QPoland](https://qworld.net/qpoland/)) and updated by <a href="https://www.cmpe.boun.edu.tr/~ozlem.salehi/" target="_blank">Dr. Özlem Salehi</a> and Dr. Abuzer Yakaryilmaz (<a href="https://qworld.net/qlatvia/" target="_blank">QLatvia</a>). We would like to thank Dr. Maksim Dimitrijev (<a href="http://qworld.lu.lv/index.php/qlatvia/" target="_blank">QLatvia</a>) for revising the materials.

## Making Contributions

If you are interested, you are welcome to contribute to Nickel. Please read QWorld's rules for developing projects.

https://qworld.net/wp-content/uploads/2020/09/Rules-for-the-projects-developed-under-the-QEducation-2020-Sep-22.pdf

## License

The code of this project is licensed under the Apache License, Version 2.0
(the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   [http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

The text and figures of this work is licensed under a Creative Commons Attribution 4.0 International License, available at [https://creativecommons.org/licenses/by/4.0/legalcode](https://creativecommons.org/licenses/by/4.0/legalcode).

