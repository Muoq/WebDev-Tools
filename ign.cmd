@echo off
cd python
IF "%1"=="state" (
  SET isQuery=True
  GOTO evalstate
) ELSE (
  GOTO runpy
)
:runpy
python "tempignore.py"
GOTO evalstate
:evalstate
FOR /F "delims=" %%i IN (ignore_state.txt) do SET "statevar=%%i"
IF "%statevar%"=="0" (
  echo State: Tracked
)
IF "%statevar%"=="1" (
  echo State: Ignored
)
GOTO end
:end
cd ..
@echo on
