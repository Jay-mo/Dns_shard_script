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
+----------------+----------------+
| Meraki Shard   | IPv4 Address   |
+================+================+
| n1.meraki.com  | 209.206.53.169 |
+----------------+----------------+
```

For help 

```python
python index.py --help
```
