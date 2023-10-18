# 0x01. NoSQL

## Learning Objecives

### What NoSQL means

NoSQL stands for "Not Only SQL" and is a category of database management systems designed to handle various types of data, including unstructured, semi-structured, and rapidly changing data. It provides flexibility and scalability, making it suitable for modern applications with diverse data requirements.

### Difference between SQL and NoSQL

SQL databases are relational databases that use structured schemas, while NoSQL databases do not enforce a fixed schema. NoSQL databases offer more flexibility and are designed for handling dynamic and diverse data.

### ACID

ACID stands for Atomicity, Consistency, Isolation, and Durability. It is a set of properties that guarantee reliable processing of database transactions. NoSQL databases often prioritize performance and scalability over strict ACID compliance.

### Document Storage

Document storage is a type of NoSQL database that stores data in semi-structured documents, such as JSON or XML. Each document can have different fields, providing flexibility in data modeling.

### NoSQL Types

NoSQL databases come in various types, including document stores, key-value stores, column-family stores, and graph databases. Each type is optimized for specific use cases.

### Benefits of a NoSQL Database

NoSQL databases offer benefits like scalability, high performance, flexibility, and the ability to handle diverse data types. They are suitable for applications with evolving data needs.

### Querying NoSQL Databases

To query information from a NoSQL database, you can use query languages specific to the database type, such as MongoDB's query language for document stores.

### Inserting/Updating/Deleting in NoSQL Databases

NoSQL databases provide APIs and methods to insert, update, and delete data. The operations vary depending on the database type and API used.

### Using MongoDB

MongoDB is a popular NoSQL database. To use MongoDB, you need to understand its data model, query language, and how to interact with it programmatically.


## Requirements:

## MongoDB Command File:

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using MongoDB (version 4.2).
- All files should end with a new line.
- The first line of all files should be a comment: `// my comment`.
- A `README.md` file at the root of the project folder is mandatory.
- The length of your files will be tested using `wc`.

## Python Scripts:

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using `Python3` (version 3.7) and `PyMongo` (version 3.10).
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file at the root of the project folder is mandatory.
- Your code should follow the `pycodestyle` style (version 2.5.*).
- The length of your files will be tested using `wc`.
- All your modules should have documentation `(use python3 -c 'print(__import__("my_module").__doc__))`.
- All your functions should have documentation `(use python3 -c 'print(__import__("my_module").my_function.__doc__))`.
- Your code should not be executed when imported (use `if __name__ == "__main__":`).

* Resource on the database's official installation guide can be found [here](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/).

### Create a virtual environment
- Environment needed for the project package dependency's isolation and intergrity.
```bash 
$: python3 -m venv .0x01-nosql-env
$: . .0x01-nosql-env/bin/activate
(.0x01-nosql-env)$:
```

- Ugrade `pip` before running necessary installations incase its current version happens to be out-dated.
```bash
(.0x01-nosql-env)$: pip install --upgrade pip
Collecting pip
  Downloading https://files.pythonhosted.org/packages/e0/63/b428aaca15fcd98c39b07ca7149e24bc14205ad0f1c80ba2b01835aedde1/pip-23.3-py3-none-any.whl (2.1MB)
    100% |████████████████████████████████| 2.1MB 4.2MB/s
Installing collected packages: pip
  Found existing installation: pip 19.0.3
    Uninstalling pip-19.0.3:
      Successfully uninstalled pip-19.0.3
Successfully installed pip-23.3

```

### Version Deprecation
* As instructed in the project, the version of MongoDB to be utilized is v4.2 however on website it was clearly stated
that isn't supported anymore and has been archived due to a time span (=<4 years) placed on every version's shipped to
production, this leads to the installation of the version's predecessor instead being v4.4.
* The following statements contain links to its Official website providing more clarity.
  - Information on [MongoDB Software Lifecycle Schedules](https://www.mongodb.com/support-policy/lifecycles)
  - [MongoDB 4.2 Manual](https://www.mongodb.com/docs/v4.2/).

### MongoDB Installation
- Remove existing MongoDB installations, if any.
```bash
(.0x01-nosql-env)$: sudo apt-get purge mongodb-org*
(.0x01-nosql-env)$: sudo rm -r /var/log/mongodb
(.0x01-nosql-env)$: sudo rm -r /var/lib/mongodb

```

- Import MongoDB's Public Key and Add Repository for Version 4.4
```bash
(.0x01-nosql-env)$: sudo apt-get install gnupg curl
(.0x01-nosql-env)$: curl -fsSL https://www.mongodb.org/static/pgp/server-4.4.asc | sudo gpg --dearmor -o 
/usr/share/keyrings/mongodb-archive-keyring.gpg
(.0x01-nosql-env)$: echo "deb [signed-by=/usr/share/keyrings/mongodb-archive-keyring.gpg] https://repo.mongodb.
org/apt/ubuntu bionic/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list

```

- Update package list and install MongoDB 4.4
```bash
(.0x01-nosql-env)$: sudo apt-get update
(.0x01-nosql-env)$: sudo apt-get install -y mongodb-org

```

- Confirm if installation was successful
```bash
(.0x01-nosql-env)$: which mongo
/usr/bin/mongo
(.0x01-nosql-env)$:
(.0x01-nosql-env)$: ls -la /etc/apt/sources.list.d
total 4
drwxr-xr-x 1 root root  34 Oct 17 10:37 .
drwxr-xr-x 1 root root  28 Mar 15  2022 ..
-rw-r--r-- 1 root root 134 Oct 17 10:37 mongodb-org-4.4.list
(.0x01-nosql-env)$:
(.0x01-nosql-env)$: /usr/share/keyrings
total 56
drwxr-xr-x 1 root root   41 Oct 17 10:37 .
drwxr-xr-x 1 root root   47 Mar 30  2022 ..
-rw-r--r-- 1 root root 1162 Oct 17 10:37 mongodb-archive-keyring.gpg
-rw-r--r-- 1 root root 2247 Jan 20  2022 ubuntu-advantage-cc-eal.gpg
-rw-r--r-- 1 root root 2274 Jan 20  2022 ubuntu-advantage-cis.gpg
-rw-r--r-- 1 root root 2236 Jan 20  2022 ubuntu-advantage-esm-apps.gpg
-rw-r--r-- 1 root root 2264 Jan 20  2022 ubuntu-advantage-esm-infra-trusty.gpg
-rw-r--r-- 1 root root 2275 Jan 20  2022 ubuntu-advantage-fips.gpg
-rw-r--r-- 1 root root 2235 Jan 20  2022 ubuntu-advantage-ros.gpg
-rw-r--r-- 1 root root 7399 Sep 17  2018 ubuntu-archive-keyring.gpg
-rw-r--r-- 1 root root 6713 Oct 27  2016 ubuntu-archive-removed-keys.gpg
-rw-r--r-- 1 root root 4097 Feb  6  2018 ubuntu-cloudimage-keyring.gpg
-rw-r--r-- 1 root root    0 Jan 17  2018 ubuntu-cloudimage-removed-keys.gpg
-rw-r--r-- 1 root root 1227 May 27  2010 ubuntu-master-keyring.gpg

```

- Create data directory at location you're most comfortable with
```bash
(.0x01-nosql-env)$: sudo mkdir -p ~/data/db
```

### Start MongoDB
- Applying this command syntax with the primary MongoDB daemon will annul any failure on execution:
```bash
(.0x01-nosql-env)$: sudo mongod --dbpath /root/alx-backend-storage/0x01-NoSQL/data/db
```

- Output: Daemon starts up and listens for signals indefinitely:
```bash
{"t":{"$date":"2023-10-17T17:58:26.073+00:00"},"s":"I",  "c":"CONTROL",  "id":23285,   "ctx":"main","msg":"Automatically disabling TLS 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'"}
{"t":{"$date":"2023-10-17T17:58:26.163+00:00"},"s":"I",  "c":"NETWORK",  "id":4648601, "ctx":"main","msg":"Implicit TCP FastOpen unavailable. If TCP FastOpen is required, set tcpFastOpenServer, tcpFastOpenClient, and tcpFastOpenQueueSize."}
{"t":{"$date":"2023-10-17T17:58:26.166+00:00"},"s":"I",  "c":"STORAGE",  "id":4615611, "ctx":"initandlisten","msg":"MongoDB starting","attr":{"pid":2508,"port":27017,"dbPath":"/root/alx-backend-storage/0x01-NoSQL/data/db","architecture":"64-bit","host":"d38b1132de14"}}
{"t":{"$date":"2023-10-17T17:58:26.166+00:00"},"s":"W",  "c":"CONTROL",  "id":20720,   "ctx":"initandlisten","msg":"Available memory is less than system memory","attr":{"availableMemSizeMB":256,"systemMemSizeMB":15718}}
{"t":{"$date":"2023-10-17T17:58:26.166+00:00"},"s":"I",  "c":"CONTROL",  "id":23403,   "ctx":"initandlisten","msg":"Build Info","attr":{"buildInfo":{"version":"4.4.25","gitVersion":"3e18c4c56048ddf22a6872edc111b542521ad1d5","openSSLVersion":"OpenSSL 1.1.1  11 Sep 2018","modules":[],"allocator":"tcmalloc","environment":{"distmod":"ubuntu1804","distarch":"x86_64","target_arch":"x86_64"}}}}
{"t":{"$date":"2023-10-17T17:58:26.167+00:00"},"s":"I",  "c":"CONTROL",  "id":51765,   "ctx":"initandlisten","msg":"Operating System","attr":{"os":{"name":"Ubuntu","version":"18.04"}}}
{"t":{"$date":"2023-10-17T17:58:26.167+00:00"},"s":"I",  "c":"CONTROL",  "id":21951,   "ctx":"initandlisten","msg":"Options set by command line","attr":{"options":{"storage":{"dbPath":"/root/alx-backend-storage/0x01-NoSQL/data/db"}}}}
{"t":{"$date":"2023-10-17T17:58:26.170+00:00"},"s":"I",  "c":"STORAGE",  "id":22270,   "ctx":"initandlisten","msg":"Storage engine to use detected by data files","attr":{"dbpath":"/root/alx-backend-storage/0x01-NoSQL/data/db","storageEngine":"wiredTiger"}}
{"t":{"$date":"2023-10-17T17:58:26.170+00:00"},"s":"I",  "c":"STORAGE",  "id":22300,   "ctx":"initandlisten","msg":"The configured WiredTiger cache size is more than 80% of available RAM. See http://dochub.mongodb.org/core/faq-memory-diagnostics-wt","tags":["startupWarnings"]}
{"t":{"$date":"2023-10-17T17:58:26.171+00:00"},"s":"I",  "c":"STORAGE",  "id":22315,   "ctx":"initandlisten","msg":"Opening WiredTiger","attr":{"config":"create,cache_size=256M,session_max=33000,eviction=(threads_min=4,threads_max=4),config_base=false,statistics=(fast),log=(enabled=true,archive=true,path=journal,compressor=snappy),file_manager=(close_idle_time=100000,close_scan_interval=10,close_handle_minimum=250),statistics_log=(wait=0),verbose=[recovery_progress,checkpoint_progress,compact_progress],"}}
{"t":{"$date":"2023-10-17T17:58:32.166+00:00"},"s":"I",  "c":"STORAGE",  "id":22430,   "ctx":"initandlisten","msg":"WiredTiger message","attr":{"message":"[1697565512:166323][2508:0x7fc3f873bac0], txn-recover: [WT_VERB_RECOVERY_PROGRESS] Recovering log 1 through 2"}}
{"t":{"$date":"2023-10-17T17:58:33.855+00:00"},"s":"I",  "c":"STORAGE",  "id":22430,   "ctx":"initandlisten","msg":"WiredTiger message","attr":{"message":"[1697565513:855786][2508:0x7fc3f873bac0], txn-recover: [WT_VERB_RECOVERY_PROGRESS] Recovering log 2 through 2"}}
{"t":{"$date":"2023-10-17T17:58:35.676+00:00"},"s":"I",  "c":"STORAGE",  "id":22430,   "ctx":"initandlisten","msg":"WiredTiger message","attr":{"message":"[1697565515:676186][2508:0x7fc3f873bac0], txn-recover: [WT_VERB_RECOVERY | WT_VERB_RECOVERY_PROGRESS] Main recovery loop: starting at 1/168960 to 2/256"}}
{"t":{"$date":"2023-10-17T17:58:38.572+00:00"},"s":"I",  "c":"STORAGE",  "id":22430,   "ctx":"initandlisten","msg":"WiredTiger message","attr":{"message":"[1697565518:565182][2508:0x7fc3f873bac0], txn-recover: [WT_VERB_RECOVERY_PROGRESS] Recovering log 1 through 2"}}
{"t":{"$date":"2023-10-17T17:58:39.756+00:00"},"s":"I",  "c":"STORAGE",  "id":22430,   "ctx":"initandlisten","msg":"WiredTiger message","attr":{"message":"[1697565519:756781][2508:0x7fc3f873bac0], txn-recover: [WT_VERB_RECOVERY_PROGRESS] Recovering log 2 through 2"}}
{"t":{"$date":"2023-10-17T17:58:40.455+00:00"},"s":"I",  "c":"STORAGE",  "id":22430,   "ctx":"initandlisten","msg":"WiredTiger message","attr":{"message":"[1697565520:454184][2508:0x7fc3f873bac0], txn-recover: [WT_VERB_RECOVERY | WT_VERB_RECOVERY_PROGRESS] Set global recovery timestamp: (0, 0)"}}
{"t":{"$date":"2023-10-17T17:58:40.455+00:00"},"s":"I",  "c":"STORAGE",  "id":22430,   "ctx":"initandlisten","msg":"WiredTiger message","attr":{"message":"[1697565520:455108][2508:0x7fc3f873bac0], txn-recover: [WT_VERB_RECOVERY | WT_VERB_RECOVERY_PROGRESS] Set global oldest timestamp: (0, 0)"}}
{"t":{"$date":"2023-10-17T17:58:40.472+00:00"},"s":"I",  "c":"STORAGE",  "id":22430,   "ctx":"initandlisten","msg":"WiredTiger message","attr":{"message":"[1697565520:472533][2508:0x7fc3f873bac0], WT_SESSION.checkpoint: [WT_VERB_CHECKPOINT_PROGRESS] saving checkpoint snapshot min: 1, snapshot max: 1 snapshot count: 0, oldest timestamp: (0, 0) , meta checkpoint timestamp: (0, 0) base write gen: 673"}}
{"t":{"$date":"2023-10-17T17:58:40.547+00:00"},"s":"I",  "c":"STORAGE",  "id":4795906, "ctx":"initandlisten","msg":"WiredTiger opened","attr":{"durationMillis":14376}}
{"t":{"$date":"2023-10-17T17:58:40.551+00:00"},"s":"I",  "c":"RECOVERY", "id":23987,   "ctx":"initandlisten","msg":"WiredTiger recoveryTimestamp","attr":{"recoveryTimestamp":{"$timestamp":{"t":0,"i":0}}}}
{"t":{"$date":"2023-10-17T17:58:40.608+00:00"},"s":"I",  "c":"STORAGE",  "id":22262,   "ctx":"initandlisten"
```

* The daemon's execution can be terminated with the Keybooard Interrupt <<**Ctl + C**>>

### Start MongoDB Shell
- Open a new terminal and execute the command for invoking the MongoDB Shell.
```bash
(.0x01-nosql-env)$: mongo
```

- Output will should be similar to this means MongoDB is running successfully.
```bash
(.0x01-nosql-env)$: mongo
MongoDB shell version v4.4.25
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("a7f6b435-4da6-4ad2-8ab6-6706235a63a0") }
MongoDB server version: 4.4.25
---
The server generated these startup warnings when booting:
        2023-10-17T17:58:26.170+00:00: The configured WiredTiger cache size is more than 80% of available RAM. See http://dochub.mongodb.org/core/faq-memory-diagnostics-wt
        2023-10-17T17:58:40.616+00:00: Access control is not enabled for the database. Read and write access to data and configuration is unrestricted
        2023-10-17T17:58:40.617+00:00: You are running this process as the root user, which is not recommended
        2023-10-17T17:58:40.617+00:00: This server is bound to localhost. Remote systems will be unable to connect to this server. Start the server with --bind_ip <address> to specify which IP addresses it should serve responses from, or with --bind_ip_all to bind to all interfaces. If this behavior is desired, start the server with --bind_ip 127.0.0.1 to disable this warning
---
> 
```

* As seen the MongoDB Shell springs up and displays its REPL interface with details about the shell version, the server to which connection is established, and important warnings related to server configuration and security best practices. It's important to pay attention to these warnings and address them as needed to ensure the proper and secure operation of the MongoDB server.

* Thank you and Happy Coding!

## Author: Emeka Emodi
