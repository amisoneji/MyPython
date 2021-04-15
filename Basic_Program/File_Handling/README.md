**File Handling:**

- Step 1:
	open a file

- step 2:
	read or write

- step 3:
	close the file

**open()**

it is used to open a file in a specific mode.
	
var=open('file path','mode')


**Commonly used modes:**

- r-->read in text
- w-->write in text
- rb-->read in binray
- wb-->write in binary
- a-->append in text
- r+-->read and write
- w+-->write and read
- a+-->append and read
  

**File Variables:**

file.mode---->returns mode of file

file.closed---->returns True if file is closed else False

**File Methods:**

- file.tell()---->returns current position of internal pointer
		initially,position of file pointer is just before first char i.e. 0

- file.seek()---->sets the current position of pointer in absolute manner(by default)

- file.read()---->read all chars as string from next char of pointer position and also moves pointer position by number of read chars.

- file.read(5)---->read 5 chars as string from next char of pointer position.

- file.readline()---->read a line as string from next char of pointer position.

- file.readlines()---->read all lines as strings and return them as list.

- file.write()---->write() a string to file buffer.

- file.flush()---->flush the buffer(write data to actual file).

- file.close()---->close() the file by flushing the buffer(if write mode).

**With Statement:**

- with resource as alias:
	      statements

- Here resource may be:
	  
    -->opening a file
    
    -->database connection

	-->socket connection
	etc.

**Advantage:**

- We need not to close the resource explicitly.
- Resource gets closed automatically when we complete with block.
