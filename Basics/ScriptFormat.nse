--[ 
3 Steps to Nmap NSE scripts
    1. Multiple types of Field
    2. Rules for when the script is executed
    3. Action for what the script actually does
--]

-- Description Fields
description = "Gives info on hosts" -- What does this script do
categories = {"basics","erq-basics"} -- run this with other similar scripts
author = "Edgar Quinones" -- Who wrote it!!
license = "Same as Nmap--See https://nmap.org/book/man-legal.html" -- Free and opensource!
dependencies = {} -- Run other scripts first 

-- Rules: Should a script run against a target?
    -- If a rule function returns true, then yes
-- Rules must contains ONE or MORE of the following: 
prerule() -- Runs once before any hosts scanned
hostrule(host) -- After batch of hosts are scanned
portrule(host, port) -- After batch of hosts are scanned
postrule() -- After all hosts are scanned
-- A script may run multiple times if it has multiple rules

-- Use PRERULE for host discovery (DISCOVERY SECTION)
-- Use POSTRULE for data and stats (AI REPORT)

-- Action: Heart of the script
    -- Same arguments as the rule
    -- Returns name-values, string, or nil

    
