# Dns_shard_script

 A python script to query Meraki Shards


## Usage

This will print all the available meraki shards
```python
python index.py
```



To query a specific shard 

```python
python index.py --shard 1
```

```
+----------------+----------------+-------------------------------------+
| Meraki Shard   | IPv4 Address   | IPv6 Address                        |
+================+================+=====================================+
| n1.meraki.com  | 209.206.53.169 | 2620:12f:c002:0:faa7:3aff:fe0c:313c |
+----------------+----------------+-------------------------------------+
```


For help 

```python
python index.py --help
```



### Modules needed
This script requires the following python modules

click

dnspython

tabulate

install them using pip

```python
pip install click
pip install dnspython
pip install tabulate
```
