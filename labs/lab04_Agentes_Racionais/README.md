Create a virtual environment in your project directory and use it with Jupyter notebook on a Linux system:

1. **Navigate to your project directory**:
```bash
cd /path/to/your/project
```
Replace `/path/to/your/project` with the path to your project directory.

2. **Create a new virtual environment in your project directory**:
```bash
python3 -m venv .venv
```
This will create a new virtual environment named `.venv` in your project directory.

3. **Activate the virtual environment**:
```bash
source venv/bin/activate
```

4. **Install Jupyter in the virtual environment**:
```bash
pip install jupyter
```

5. **Install the IPython kernel in the virtual environment**:
```bash
pip install ipykernel
```

6. **Add your virtual environment to Jupyter**:
```bash
python -m ipykernel install --user --name=.venv
```
This will add your virtual environment to Jupyter. You can replace `venv` with any name you want to give to your kernel.

7. **Install other dependencies**:
```bash
pip install package-name
```
Replace `package-name` with the name of the package you want to install.

Now, when you start Jupyter notebook, you can select the new kernel (named `venv` or whatever name you gave) from the 'Kernel' -> 'Change kernel' menu.

Remember to **deactivate the virtual environment** when you're done:
```bash
deactivate
```
