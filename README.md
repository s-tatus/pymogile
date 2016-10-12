MogileFS client library for Python2/Python3
===========================================

This project has been forked from https://github.com/AloneRoad/pymogile.
This version has Python3 support added, but unfortunately we do not have working tests
so cannot confirm that everything works as expected.

This code runs under Python 2 but Python 3 has issues at the moment. It is under (slow) active development.


Original Docs from AloneRoad version
------------------------------------

### 1. Connect to MogileFS

```python
from pymogile import Client, MogileFSError
datastore = Client(domain='test', trackers=['127.0.0.1:7001'])
```


### 2. New file

```python
fp = datastore.new_file('foobar.txt')
fp.write('foo')
fp.close()
```


### 3. Get paths

```python
> datastore.get_paths('foobar.txt')
['http://127.0.0.1:7500/dev4/0/000/251/0000251237.fid', 'http://127.0.0.1:7500/dev6/0/000/251/0000251237.fid']
> print datastore.get_paths('404.txt')
[]
```

### 4. Get file data

```python
> datastore.get_file_data('404.txt')
> datastore.get_file_data('foobar.txt')
'foo'
```


### 5. Rename file


```python
> datastore.rename('404.txt', 'test.txt')
False
> datastore.rename('foobar.txt', 'foo.txt')
True
> datastore.get_file_data('foobar.txt')
> datastore.get_file_data('test.txt')
> datastore.get_file_data('foo.txt')
'foo'
```

### 6. Remove file

```python
> datastore.delete('foobar.txt')
False
> datastore.delete('foo.txt')
True
> datastore.get_file_data('foo.txt')
```
