-- Whenever user eneters '--script-help' they will see this
description = "My first script"

-- If someone wants to run all the scripts of a specific
-- category, they do --script discovery
categories = {"discovery"}

-- One of the possible nmap default functions you
-- must use if you want to use a nmap script.
-- Ex. hostrule, prerule, postrule
-- This function checks the host/port and
-- filters through it, only accepting valid ones.
-- Once the port has been accepted, it is sent to 'action'
-- This function currently accepts all ports.
-- as long as its open
portrule = function(host, port) -- SHOULD I RUN IT?
        return true
end

-- This is the function that actually runs when given a port
-- is accepted from 'portrule;
-- open ports on a host will have it say 80: Port is: open
action = function(host, port) -- WHAT SHOULD I DO?
        return "Port is: " .. port.state
end
