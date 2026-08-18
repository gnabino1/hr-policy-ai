### STEPS TO PRACTICE

1. Install UV
```
pip install uv
```
```
$uvPath = "C:\Users\Lenovo\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\Scripts"
```
```
[Environment]::SetEnvironmentVariable("Path", [Environment]::GetEnvironmentVariable("Path", "User") + ";" + $uvPath, "User")
```
```
uv --verion
```
2. Activate a new venv
```
.venv\Scripts\activate
```
### STEPS FOR GIT
1. Install Git
2. Make id in github
3. Make a repository in gituhb(Donot touch anything)
4. Make a .gitignore files
5. Commands
```
git add .
```
```
git commit -m "Some Message"
```
```
git push origin master
```
### MAKE requirements file
```
python-dotenv

langchain
langchain-core
langchain-community

## LLM PROVIDER
langchain-groq
langchain-text-splitters

## VECTOR STORE
faiss-cpu

##notebook
jupyter
ipykernel

## webapp
streamlit
```

