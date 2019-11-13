@echo off
set venv-name=PokAR_venv
cmd /k "python -m venv %venv-name% & cd /d .\%venv-name%\Scripts & activate & cd /d .. & cd /d .. & pip install -r requirements.txt"