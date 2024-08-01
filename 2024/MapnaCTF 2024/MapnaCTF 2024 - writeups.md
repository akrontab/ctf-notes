# Write ups

Sat, 20 Jan. 2024, 15:00 UTC — Sun, 21 Jan. 2024, 15:00 UTC

<https://mapnactf.com/>

## Tampered (209) - Warmup, Forensics

>Tampered
>Our MAPNA flags repository was compromised, with attackers introducing one invalid flag. Can you identify the counterfeit flag?
>
>Note: Forgot the flag format in the rules pages, just find the tampered one.
>
>You are not allowed to brute-force the flag in scoreboard, this will result in your team being blocked.

We are given a `flags.txt` file with a large number of strings that look like the flags for the CTF

```bash
┌──(kali㉿kali)-[~/Desktop/tampered]
└─$ head flags.txt                                
MAPNA{X9JMN#CO4W1YrE%8%!ULanDXl$Yy=H>PLe5pJ*pk}
MAPNA{m+0ORa'p2TIqjBH3On+SbjjG1w*?p&hWMlW8D[cU}
MAPNA{6;,//u%ED<<K)Vlq</NCcsgM?nwdKwE8O4p?/>wq}
MAPNA{H9q(/3oNRmp4I(UZ9GIf'4*=Nz&60dkUJ?ymR7M@}
MAPNA{EprAuVKi\v<'.ACK>ier"Fgs(5o3)ZdUTdI7K66@}
MAPNA{lQE?RV0s7tuz6s3IQCx=E"i,YCxo;/N%uS=WpQ.L}
MAPNA{AfHAr6L++57S3;8hQTfO9,ppVoNn*VRxh(8Y3QM\}
MAPNA{.Rb3,:d2JJ4Sii%C9>lmGWA8O+Oni%zl3bS6I):v}
MAPNA{Ps?u1UgN+[d-d.V(pgXOiP6Z%gX(tq)2m=4K,e/t}
MAPNA{pB($5JY\jhj'1G??DtxsAAxQeg!y7&llu&[O2wqg}

┌──(kali㉿kali)-[~/Desktop/tampered]
└─$ cat flags.txt | wc -l
31337
```

That's a lot of flags and more than we could manually scroll through to try and spot any differences. One idea is to count the number of characters in each flag and see if there are any differences

```bash
┌──(kali㉿kali)-[~/Desktop/tampered]
└─$ cat flags.txt | awk '{print length}' | uniq -c
   9790 49
      1 48
      1 50
  21545 49
```

Looks like either the 48 or 50 length flags might be what we are looking for

```bash
┌──(kali㉿kali)-[~/Desktop/tampered]
└─$ cat flags.txt | awk 'length($0) == 48'     
MAPNA{Tx,D51otN\eUf7qQ7>ToSYQ\;5P6jTIHH#6TL+uv}
                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/tampered]
└─$ cat flags.txt | awk 'length($0) == 50'
MAPNA{R6Z@//\>caZ%%k)=ci3$IyOkSGK%w<"V7kgesY&k}
```

If we try both flags the flag with length 48 is the valid one

`MAPNA{Tx,D51otN\eUf7qQ7>ToSYQ\;5P6jTIHH#6TL+uv}`

## Flag Holding (37) - Warmup, Web

>Flag Holding
>Hopefully you know how web works...
>
>http://18.184.219.56:8080/

Navigating to the website gives a page with the message:

`You are not coming from "http://flagland.internal/".`

This looks like it'a reference to the `Referer` header. More info on this header here: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer>

Using Burp Suite we can tamper with the request and include the header `Referer: http://flagland.internal/` in the request

```http
GET / HTTP/1.1
Host: 18.184.219.56:8080
Referer: http://flagland.internal/


```

That request gives us a new page with the message in the content:

`<div class="msg" style="">Unspecified "secret".</div>`

This could be a clue to use a query parameter in the url. Let's modify the request to include it and set the 

```http
GET /?secret HTTP/1.1
Host: 18.184.219.56:8080
Referer: http://flagland.internal/


```

Bingo! This gives us another clue

```html
<div class="msg" style="">
	Incorrect secret. <!-- hint: secret is ____ which is the name of the protocol that both this server and your browser agrees on... -->
</div>
```

The protocol being used is `http` so let's set the value of the `secret` query parameter to `secret=http`

```html
<div class="msg" style="">
	Sorry we don't have "GET" here but we might have other things like "FLAG".
</div>
```

Another clue. Let's change the GET in the request to FLAG 

```http
FLAG /?secret=http HTTP/1.1
Host: 18.184.219.56:8080
Referer: http://flagland.internal/


```

And this last request gets us the flag!

`MAPNA{533m5-l1k3-y0u-kn0w-h77p-1836a2f}`

## PLC I 🤖 (32) - Warmup, Forensics

>PLC I 🤖
>The MAPNA CERT team has identified an intrusion into the plant's PLCs, discovering a covert message transferred to the PLC. Can you uncover this secret message?

We are given a pcap for this challenge. We can see there are two hosts communicating with each other and  `10.19.31.85` looks like it's the host sending messages to the PLC at `192.168.110.40`

If we look at all the ACK packets coming from `10.19.31.85` there is some interesting padding at the end of the packet that looks like it follows the format `<sequence#>:<data>`. If we extract the padding data and put it in order we get the flag.

```text
1:MAPNA{y
2:0U_sHOu
3:Ld_4lW4
4:yS__CaR
5:3__PaAD
6:d1n9!!}

MAPNA{y0U_sHOuLd_4lW4yS__CaR3__PaADd1n9!!}

```
