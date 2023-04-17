# Quick explanation

with skipping data it should always be how many characters it takes to get over what you want to skip

for example if I have a file with UnityArchiveUnityFS (and then the real UnityFS header data) which would cause the script to fail

I'd count how many letters(16 in this hypothetical) then put it in the script 

but you'd only have to worry about this if you want to use it otherwise it'll just start from the beginning of the file
