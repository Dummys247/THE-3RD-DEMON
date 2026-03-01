@echo off
set "GIT_CMD=C:\Users\Lenovo\AppData\Local\GitHubDesktop\app-3.5.1\resources\app\git\cmd\git.exe"

"%GIT_CMD%" add .
"%GIT_CMD%" commit -m "FIX_REVERT_TO_VERSION_A"
"%GIT_CMD%" push origin main --force
