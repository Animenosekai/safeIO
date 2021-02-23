# safeIO  

>  Safely make I/O operations to files in Python even from multiple threads... and more!  

# Table of Content  

1. [safeIO](#safeio)
2. [Table of Content](#table-of-content)
3. [What is it?](#what-is-it)
4. [Installation](#installation)
5. [Objects](#objects)
    - [TextFile()](#textfile)
    - [BinaryFile()](#binaryfile)
    - [JSONFile()](#jsonfile)
6. [Tips](#tips)


# What is it?
It's a module which lets you manage your files (most of the time, Input/Output operations) without worrying about accessing the file from two simultaneously.

Some functions may help you managing your files more easily as they are intuitive and things like substractions (TextFile object - TextFile Object returns the Cosine Similarity of the two files), equality (Object == Object), iteration (for line in TextFile object), the rename/move/delete methods are made easier!.

# Installation
**From PIP**
```sh
pip install safeIO --upgrade
```


# Objects
## TextFile(filepath, encoding="utf-8", blocking=True)  

> A Text File object  


### isfile  

*isfile(callback=None)*  

> Wether the file exists on the disk or not  

### delete  

*delete(callback=None)*  

> Deletes the file  

### rename  

*rename(newName,overwrite=False,callback=None)*  

> Renames the file and returns its new path  

### move  

*move(newPath,overwrite=False,callback=None)*  

> Moves the file and returns its new path  

### name  

*name(callback=None)*  

> Returns the file name  

### fileno  

*fileno(callback=None)*  

> Returns the file descriptor (int) used by Python to request I/O operations from the operating system.  

### read  

*read(position=0,callback=None)*  

> Reads the entire file and returns its content  

### write  

*write(data,position=0,callback=None)*  

> Writes (or overwrites) to the file and returns the number of characters written  

### append  

*append(data,callback=None)*  

> Appends to the file and returns the number of characters written  

### readline  

*readline(position=0,callback=None)*  

> Returns the line of the current position (from the position to the linebreak)  

### readlines  

*readlines(position=0,callback=None)*  

> Reads the whole file and returns the lines (separated by a line break)  

### writelines  

*writelines(data,position=0,callback=None)*  

> Writes (or overwrites) the given list of lines to the file  

### appendlines  

*appendlines(data,callback=None)*  

> Appends the given list of lines to the file  

### detach  

*detach(mode="r",callback=None)*  

> Returns the opened IO (TextIOWrapper)  

>   

**Warning: Make sure to close the file correctly after using the file with detach**

---  

## BinaryFile(filepath, blocking=True)  

> A Binary File object  

### isfile  

*isfile(callback=None)*  

> Wether the file exists on the disk or not  

### delete  

*delete(callback=None)*  

> Deletes the file  

### rename  

*rename(newName,overwrite=False,callback=None)*  

> Renames the file and returns its new path  

### move  

*move(newPath,overwrite=False,callback=None)*  

> Moves the file and returns its new path  

### name  

*name(callback=None)*  

> Returns the file name  

### fileno  

*fileno(callback=None)*  

> Returns the file descriptor (int) used by Python to request I/O operations from the operating system.  

### read  

*read(position=0,callback=None)*  

> Reads the entire file and returns its content  

### write  

*write(data,position=0,callback=None)*  

> Writes (or overwrites) to the file and returns the number of bytes written  

### append  

*append(data,callback=None)*  

> Appends to the file and returns the number of bytes written  

### readline  

*readline(position=0,callback=None)*  

> Returns the line of the current position (from the position to the linebreak)  

### readlines  

*readlines(position=0,callback=None)*  

> Reads the whole file and returns the lines (separated by a line break)  

### writelines  

*writelines(data,position=0,callback=None)*  

> Writes (or overwrites) the given list of lines to the file  

### appendlines  

*appendlines(data,callback=None)*  

> Appends the given list of lines to the file  

### detach  

*detach(mode="rb",callback=None)*  

> Returns the opened IO (TextIOWrapper)  

>   

> Tips: Make sure to include the "b" access mode in the mode\n  

**Warning: Make sure to close the file correctly after using the file with detach**

---  

## JSONFile(filepath, ensure_ascii=False, minify=False, indent=4, separators=(', ', ': '), encoding="utf-8", blocking=True)  

> A JSON File object  

### isfile  

*isfile(callback=None)*  

> Wether the file exists on the disk or not  

### delete  

*delete(callback=None)*  

> Deletes the file  

### rename  

*rename(newName,overwrite=False,callback=None)*  

> Renames the file and returns its new path  

### move  

*move(newPath,overwrite=False,callback=None)*  

> Moves the file and returns its new path  

### name  

*name(callback=None)*  

> Returns the file name  

### fileno  

*fileno(callback=None)*  

> Returns the file descriptor (int) used by Python to request I/O operations from the operating system.  

### read  

*read(position=0,callback=None)*  

> Reads the entire file and returns its content  

### write  

*write(data,position=0,callback=None)*  

> Writes (or overwrites) to the file and returns the number of characters written  

### append  

*append(data,callback=None)*  

> Appends to the file and returns the number of characters written  

### detach  

*detach(mode="r",callback=None)*  

> Returns the opened IO (TextIOWrapper)  

**Warning: Make sure to close the file correctly after using the file with detach**



# Tips
- You can temporarily make the operations blocking with the "with" statement like so:

```python
from safeIO import TextFile

f = TextFile("example.txt", blocking=False)
print(f.read()) # prints "None"
with f:
    print(f.read()) # prints the content of example.txt
with f as reading_file:
    print(reading_file.read()) # prints the content of example.txt
```

- Try to define the safeIO object at the top of your script and use the same object for all of the operations to the file with:

```python
from safeIO import JSONFile
data_file = JSONFile("data.json", minify=True, blocking=False)

# do a bunch of stuff
data_file.write({"type": "new_data"})

# do more stuff
with data_file as data:
    new = data.read()
new["type"] = "new!"
data_file.write(new)
```