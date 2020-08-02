# JavaCard-Binary-Parser

The parser interprets the java card binaries with a fixed format according java card spec, and converts the data in to human readable data and prints on the console. 
For more details please visit my <a href="https://mallikarjuntirlapur.github.io/JavaCardBinaryParser/">mallikarjuntirlapur.github.io/JavaCardBinaryParser</a> page.

### Requirements
* Python 2.7 (min)

#### Command line arguments:

CapParser.py [option] .cap [option] 'component name'/'all'

--capPath\
-p valid path to cap file.

--component\
-c caomponent name e.g 'header' or 'all'to get all component info in one shot.