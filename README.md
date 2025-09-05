# NmapNSE-scripts
Scripts using Nmap NSE to more easily use it.

## Main idea
- Scripts for the 4 steps of attack (Discovery, Vulnerabilities, Exploiting, and Authentication)
- Using custom categories so users can only run these scripts 
- Simple enough to understand, but complex enough to be useful 
- Auto transfer important info info a separate file (Might make a bash script specifically for this)
- Give the users control to be specific for different expertise levels of users. 

## How to use
I tried to keep it as straight forward as possible to use these scripts. While you can call specific scripts, I added a category to each type, that way you can call all scripts of a specific category without finding them all. This is seperate from the nmap default categories, but those are added too for advance users.

For scanning hosts, use the following format:

`nmap --script <CATEGORY> host`
- erq-discovery
- erq-vuln
- erq-exploit
- erq-auth

## Notes
I did this because I love cyber, but from a programming perspective. I am not a fan of doing the actual pen testing, because to be hounest, im not the best underpressure. I like time to plan and come up with ideas. I like to support a team anyway I can, and so if I can makes scripts that are flexiable enough that they help even a little, I'll be happy. 

I hope they can use these scripts this year, tell me the pros and cons, and I can slowly improve them little by little. 
