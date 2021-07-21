# SimpleTools

## installation
```
pip install git+https://github.com/JL710/SimpleTools.git
```
## updating
```
pip install --force-reinstall git+https://github.com/JL710/SimpleTools.git
```
## usage
```Python
ping()
```
Returns true and gives output in console

### OneLine
OneLine is for data management in a one line file.
```Python
Oneline(file, seperation)
```
File needs to be a link to the file.
> NOTE: it is recomended to be a file within only one line.

Seperation means the character that separates the data in the file.

If you set the file_create parameter True, the file will be created when not exist.

```python
addElement(element)
```
The `element` can be anything. Recomended are strings and numbers.
> NOTE: be carefull to not store data within the separation mark.

The `element` will be added to the data and the data file.

```Python
removeElement(element)
```
Removes the `element` from the data list.

### file_create
```Python
file_create(file)
```