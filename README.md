<img align="right" src="https://github.com/aapeebles/airflow-setup-win/blob/47a4e8564bc5c9a0ffc6947af7c7abde98bc946f/img/clippy_short.png" height = "200"/>


# Setting up Airflow on Windows (local)

Hi! 95% of the blog posts and aides online say "Set up Airflow quickly using this docker image!", "Use managed Airflow on Azure!", or "Set up Airflow on AWS/GCS!" And those solutions are great. And sometimes you have to do a proof of concept without those tools or the tool-set you have available is limited. All of the instructions here I have done on my own personal computer.

> **Scenario**: you have a Windows machine/server and you want an open-source, code-based solution to scheduling your code, but a GUI interface would be appropriate for the larger team.

### The 1,000 feet view of the solution:
 - Windows Server (or Windows 10 machine)
 - WSL 1 (This was the limiting factor)
 - Ubuntu 18.04.6
 - Apache Airflow 2.3

Now I get it, the number of steps below might look a little suspect, even more steps than needed. I think it's worth noting that some of these steps are **_essential_**, some are because I want to have a **_reproducible environment_** ( same Python specs inside and outside of WSL), and others cause I want to set up some foundational pieces of **_good coding practice_**.


| Step | Essential | Reproducable | Good coding | Notes |
|:-----|-----------|--------------|-------------|:------|
| Powershell | X | | | The version installed already on Windows should be fine. *I* personally like version 7. |
| Visual Studio Code | | | X | Any coding IDE will do, but I really like vscode for a lot of reasons these days |
| Ubuntu | X | | | | You need to install **some** version of Ubuntu. I don't think 18 vs 20 matters, but I used 18 at the time |
| `pyenv-win` | | X | | I use this to not accidentally upgrade Python and to keep versions constraints the same across environments |
| `Python` | | X | | if you want to code in your Windows environment and not just in WSL, that is why this is installed |
| `pip install` | | X | X | everything listed there is for reproducibility and good coding. |
| Activate `WSL` | X | | | |need to run this command in PowerShell or look up how to do it through Windows GUI |
| VScode setup | | X | X | not essential if you have a different prefered IDE |

## All before opening WSL:
 - Microsoft Store Downloads: (you can access the store from Windows programs/windows search!)
   - **PowerShell 7**: I like the newer version provided in the store because it comes with `git` installed. I also encounter less bugs with setting up `PnPOnline` modules(a different project!)
   - **Visual Studio Code**: You will see a feature preview version and the regular version. Get the regular.
   - **Ubuntu 18.04.6**: I list the version so you can know what I used in case there are any differences in later versions. This was not an intentional choice, but listing it for the sake of reproducibility 
-  PowerShell 7 set up: (open PowerShell "as administrator") and do the following
   - **pyenv-win**: commands are here [PowerShell instructions](https://github.com/pyenv-win/pyenv-win#quick-start)
   - **Python 3.8.10**:
     - `pyenv install 3.8.10`
     - `pyenv version` and copy output for later.Mine was `3.8.10 (set by C:\Users\aapee\.pyenv\pyenv-win\version)`
   - **pip install**: I want these available no matter what the virtual environment. (I use pip in this example because collaborators are not as familiar with anaconda/conda/miniconda. Also, miniconda felt like one more thing to install. I know `conda-forge` handles packages dependencies better, please don't come at me :D )
     - `pyvenv`
     - `pipreqs`
     - `black`
     - `pylint`
   - activating **WSL**:
     - `Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux`
     - [great instructions](https://www.toptechskills.com/windows-10-tutorials-courses/how-to-install-enable-windows-subsystem-for-linux-wsl-windows-10/)
- Set up Visual Studio Code
   - Choose a Python interpreter
     - open vscode
     - `ctrl`+`shift`+`p` to open the settings search bar
     - type "Python: select" and click on the `Python: select interpreter` option
     - look for the `pyenv` interpreter choice (it will say 3.8.10 on the left and `pyenv` in blue on the right)
   - Import profile of choice, or select extensions that speak to you. I can do a separate post of my fav vscode stuff. 

## Upcoming Steps:
 - WSL, Python & PostgreSQL
 - Apache Airflow install & initial config
 - Apache Airflow customizations
 - REST API & vscode
 - MinIO xcom backend

