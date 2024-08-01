# ez caddy v2

## Description

Caddy webserver is AWESOME, using a neat and compact syntax you can do a lot of powerful things, e.g. wanna know if your browser supports HTTP3? Or TLS1.3? etc

Flag is located at GET /$(head -c 18 /dev/urandom | base64) go fetch it.

## Solution

<https://caddyserver.com/>

Review the handout files and notice that MTLS looks interesting and doesn't escape the first set of curly braces

```caddy
mtls.caddy.chal-kalmarc.tf {
    tls internal {
        client_auth {
            mode require
        }
    }
    templates
    import html_reply `You are connected with client-cert {http.request.tls.client.subject}`
}
```

Create a pcks12 cert

```bash
┌──(kali㉿kali)-[~/Desktop/handout-caddy]
└─$ openssl req -x509 -newkey rsa:4096 -keyout myKey.pem -out cert.pem -days 365 -nodes



```