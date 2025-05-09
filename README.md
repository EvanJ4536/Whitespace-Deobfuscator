# Whitespace-Deobfuscator
This script deobfuscates files that have whitespace obfuscation and saves hidden code to a file.  It will save any hidden code found in a new file named [sourceName]_deobfuscated

Remove all indentation from file before running the script

## Usage
&emsp;python whitespace_deobfuscator.py [filename] [flags]
    
&emsp;Flags:
        
&emsp;&emsp;-nws : Don't write whitespaces between each line in the output file.
        
&emsp;&emsp;-oneLine : Write all obfuscated text to one line in the output file.
