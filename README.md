# JavaCard-Binary-Parser

The parser extracts and reads binaries from a .cap file and prints in human readable format on the console. CAP files are generated using <a href="https://www.oracle.com/java/technologies/javacard-downloads.html">Java Card 3.0.5</a> tools. 
The current version of the tool only understands JC3.0.5 spec format.
For more details please visit my <a href="https://mallikarjuntirlapur.github.io/JavaCardBinaryParser/">mallikarjuntirlapur.github.io/JavaCardBinaryParser</a> page.

### Requirements
* Python 2.7 (min)

#### Command line arguments:

CapParser.py [option] .cap [option] 'component name'/'all'

--capPath\
-p valid path to cap file.

--component\
-c caomponent name e.g 'header' or 'all'to get all component info in one shot.