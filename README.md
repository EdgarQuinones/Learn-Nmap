# NmapNSE-scripts
Scripts using Nmap NSE to more easily use it.

## Main idea
- Scripts for the 4 steps of attack (Discovery, Vulnerabilities, Exploiting, and Authentication)
- Using custom categories so users can only run these scripts 
- Simple enough to understand, but complex enough to be useful 
- Auto transfer important info info a separate file (Might make a bash script specifically for this)
- Give the users control to be specific for different expertise levels of users. 
## How to use
I tried to keep it as straightforward as possible to use these scripts. While you can call specific scripts, I added a category to each type, that way you can call all scripts of a specific category without finding them all. This is seperate from the nmap default categories, but those are added too for advance users.
### Categories 
For scanning hosts, use the following format:

`nmap --script <CATEGORY> host`
- `erq-discovery`
- `erq-vuln`
- `erq-exploit`
- `erq-auth`
- `erq-all` (If you wanted to run all the scripts in this repo at once, please note this will take a while, makes a lot of files, and may not work as intended)

_Note: erq is being used for the front to not overwrite any nmap categories._
### Reports
I wanted to make this differnet from simply scanning nmaps for you, since if that was it, you wouldn't need to use this. I am sure nmap has their own reporting options, but I am also using this as a learning experience, so hopfully I still provide useful information. 

Whenever any script is executed, a report is always made. The script will NOT be a copy and paste of the nmap report. It will take the report, parse the important portions, and give some form of integrity rating to see potential next directions. 

The reports are quite differnet based on the category, for example, discovery will be discussing more about possible services to look into, while vuln will be finding issues, and recommending other tools to try and get C2.
## Notes
I did this because I love cyber, but from a programming perspective. I am not a fan of doing the actual pen testing, because to be honest, I'm not the best under pressure. I like time to plan and come up with ideas. I like to support a team anyway I can, and so if I can makes scripts that are flexiable enough that they help even a little, I'll be happy. 

I hope they can use these scripts this year, tell me the pros and cons, and I can slowly improve them little by little. Thank you for taking the time to read this. I hope these scripts benefit you!
