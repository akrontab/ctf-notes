# Toon Town Fan Club - Web

## Description

The Toon Resistance needs you! Join now to help defeat the cogs from taking over Toontown!

https://toontown-fan-club.ctf.ritsec.club/

## Solution

Sending a single tick (') causes an error

```http
POST /search HTTP/1.1
Host: toontown-fan-club.ctf.ritsec.club
Content-Type: application/json
Content-Length: 22

{
    "searchTerm":"'"
}
```

Looking for a SQLi vulnerability but having trouble finding it.
