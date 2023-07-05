## Customizations


### Code editor
[code editor](https://github.com/andreax79/airflow-code-editor)
[black formatter](https://github.com/psf/black)

`pip install black==21.12b0`
`pip install airflow-code-editor==7.3.0`


### fernet secret
```
pip install cryptography
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```
returns: 81HqDtbqAywKSOumSha3BhWNOdQ26slT6K0YaZeZyPs=

then edit the airflow.cfg
`fernet_key = 81HqDtbqAywKSOumSha3BhWNOdQ26slT6K0YaZeZyPs=`

### Time zone

# Default timezone to display all dates in the UI, can be UTC, system, or
# any IANA timezone string (e.g. Europe/Amsterdam). If left empty the
# default value of core/default_timezone will be used
# Example: default_ui_timezone = America/New_York
default_ui_timezone = America/New_York


# If set to True, Airflow will track files in plugins_folder directory. When it detects changes,
# then reload the gunicorn.
reload_on_plugin_change = True
