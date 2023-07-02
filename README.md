![clippy](clippy_airflow_banner.png)
# Setting up Airflow locally on Windows

Hi! 95% of the blog posts and aides online say "set up Airflow quickly using this docker image!", "use managed Airflow on Azure!", or "set up Airflow on AWS/GCS!" And those solutions are great. And sometimes you have to do a proof of concept without those tools or the tool-set you have available is limited. All of the instructions here I have done on my own personal computer.

**Scenario** : you have a Windows machine/server and you want an open-source, code-based solution to scheduling your code, but a GUI interface would be appropriate for the larger team.

### The 1,000 feet view of the solution:
 - Windows Server (or Windows 10 machine)
 - WSL 1 (This was the limiting factor)
 - Ubuntu 18.04.6
 - Apache Airflow 2.3

## All before opening WSL:
 - Microsoft Store Downloads:
   - PowerShell 7: I like the newer version provided in the store because it comes with `git` installed. I also encounter less bugs with setting up `PnPOnline` modules(a different project!)
   - Visual Studio Code: You will see a feature preview version and the regular version. Get the regular.
   - Ubuntu 18.04.6
-  PowerShell 7 set up
   - pyenv-win: [PowerShell instructions](https://github.com/pyenv-win/pyenv-win#quick-start)
   - Python 3.8.10:
     - `pyenv install 3.8.10`
     - `pyenv version` and copy output for later.Mine was `3.8.10 (set by C:\Users\aapee\.pyenv\pyenv-win\version)`
   - pip install: I want these available no matter what virtual environment. (I use pip in this example because collaborators are not as familiar with anaconda/conda/miniconda. Also, miniconda felt like one more thing to install. I know `conda-forge` handles packages dependencies better, please don't come at me :D )
     - `pyvenv`
     - `pipreqs`
     - `black`
     - `pylint`
   - activating WSL:
     - `Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux`
     - [great instructions](https://www.toptechskills.com/windows-10-tutorials-courses/how-to-install-enable-windows-subsystem-for-linux-wsl-windows-10/)
- Set up Visual Studio Code
   - Choose a Python interpreter
     - open vscode
     - `ctrl`+`shift`+`p` to open the settings search bar
     - type "Python: select" and click on the `Python: select interpreter` option
     - look for the `pyenv` interpreter choice (it will say 3.8.10 on the left and `pyenv` in blue on the right)
   - Import profile of choice. A selection of my own preferences:

## Upcoming Steps:
 - WSL, Python & PostgreSQL
 - Apache Airflow install & initial config
 - Apache Airflow customizations
 - REST API & vscode
 - MinIO xcom backend

