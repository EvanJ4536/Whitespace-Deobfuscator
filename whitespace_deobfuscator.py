#########################################################################
# This script deobfuscates code hidden by whitespace code obfuscation   #
#                             By: Evan                                  #
#                                                                       #
#       Remove all initial indentation from your script first.          #
#                                                                       #
# This script will go through each line of another file and try to      #
# grab any text that is obfuscated by Whitespace code obfuscation       #
# by only grabbing text that is located after 10 consecutive            #
# white spaces                                                          #
#########################################################################

import sys


nws = False
oneLine = False

for arg in sys.argv:
    if arg == '-nws':
        nws = True
    if arg == '-oneLine':
        oneLine = True
    if nws and oneLine:
        nws = False
    
if len(sys.argv) > 1:
    with open(sys.argv[1], "r", encoding="utf-8") as file:
        hidden_buffer = ''
        hidden_string = ''
        
        for line in file:
            if hidden_string != '':
                if nws:
                    hidden_buffer += hidden_string
                
                elif oneLine:
                    hidden_buffer += hidden_string.strip('\n')
                    
                else:
                    hidden_buffer += hidden_string + '\n'
            
            hidden_string = ''
            ctr = 0
            ws = 0
            target_found = 0
            ws_ctr = 0
            
            for letter in line:
                if ws == 0:
                    if letter == ' ':
                        ws_ctr += 1
                        
                        if ws_ctr >= 10:
                            ws = 1
                            
                    else:
                        ws_ctr = 0
                        
                ctr += 1
                
                if ws:
                    if letter != ' ':
                        target_found = 1
                    
                    if target_found:
                        hidden_string += letter
        
    inFileName, fileExt = sys.argv[1].rsplit('.', 1)
        
    outFileName = inFileName + "_deobfuscated." + fileExt
    
    with open(outFileName, "w", encoding="utf-8") as file:
        file.write(hidden_buffer)
            
else:
    print("""
    
    Usage: python whitespace_deobfuscator.py [filename] [flags]
    
    Flags:
        
        -nws : Don't write whitespace between each line in the output file.
        
        -oneLine : Write all obfuscated text to one line in the output file.
    
    """)