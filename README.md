### Automate file renaming
script to rename files

### Usage
> $ files -s [sear pattern or word] -n [new_name]

"-s", "--searching", help = 'search pattern or word'  
"-p", "--prefix", help = 'Add specific prefix for all searched files'  
"-n", "--new_name", help = 'New name with digit index suffix'  

### Start
1. Download script
2. run 
> $chmod +x files.py
3. Add the script path to your shell configuration (.zshrc or .bshrc)
> alias files="python3 [PATH]/files.py" 
