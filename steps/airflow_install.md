
# Install and Open Airflow!


### Install WSL packages Airflow depends on
From [System Dependencies](https://airflow.apache.org/docs/apache-airflow/stable/installation/dependencies.html#system-dependencies)

```
sudo apt-get install -y --no-install-recommends \
        freetds-bin \
        # krb5-user \
        ldap-utils \
        libffi6 \
        libsasl2-2 \
        libsasl2-modules \
        libssl1.1 \
        locales  \
        lsb-release \
        sasl2-bin \
        sqlite3 \
        unixodbc
```

### Create and activate virtual environment
```
pip install venv
python -m venv ./af_venv
source .af_venv/bin/activate
```

### pip install airflow to airflow folder
```
pip install psycopg2
mkdir airflow
cd airflow
pip install apache-airflow[async,postgress,goolge]==2.3.1 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.3.1/constraints-3.8.txt"
```

### Activate airflow scheduler for just a moment to create the `airflow.cfg` file
```
export PATH=$PATH:/home/your_user/.local/bin/
airflow scheduler
# wait a moment
```
#### use `ctrl`+`c` to stop the scheduler


### Edit `airflow.cfg`

open airflow/airflow.cfg (with `vim`, `nano`, or even `notepad`)
find and edit the following variables:
 - `executor` = LocalExecutor
 - `sql_alchemy_conn` = postgresql+psycopg2://airflow:airflow@localhost/airflow

`save` and close file.



### Get Airflow started!!!!!
**NOTE**: run each of these commands that start with `airflow` in a new command window.

```
airflow db init
airflow users create -r Admin -u admin -e admin@example.com -f admin -l user -p test
```

```
airflow webserver
```

```
airflow scheduler
```
open chrome to `http://localhost:8080/`, log in with `admin` and `test`, and you have airflow running!! WHOOHOO!


