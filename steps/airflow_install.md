

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


` pip install apache-airflow[async,postgress,goolge]==2.3.1 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.3.1/constraints-3.8.txt" `
