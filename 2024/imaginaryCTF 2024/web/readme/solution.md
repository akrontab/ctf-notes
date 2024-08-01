# readme - web

by maple3142

## Description

Try to read the flag.txt file.

Attachments
https://cybersharing.net/s/67af3fd941707117 http://readme.chal.imaginaryctf.org/

## Solution

All you had to do was read the DockerFile...... really???

```dockerfile
FROM node:20-bookworm-slim

RUN apt-get update \
    && apt-get install -y nginx tini \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /app
COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile
COPY src ./src
COPY public ./public

COPY default.conf /etc/nginx/sites-available/default
COPY start.sh /start.sh

ENV FLAG="ictf{path_normalization_to_the_rescue}"

ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["/start.sh"]
```

FLAG: `ictf{path_normalization_to_the_rescue}`
