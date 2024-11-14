REM THIS FILE IN NOT CURRENTLY IN USE, DO NOT RUN

@echo off

:Variables
 SETLOCAL
 SET "#SOURCE=https://googlechromelabs.github.io/chrome-for-testing/#stable"
 SET "#HTML=%TEMP%\HTML_Contents.TXT"
 SET "#REPLACE=%TEMP%\Replacement.TXT"
 SET "#SEARCHFOR=/win32/chromedriver"

REM Generate Replacement Config File for READABLE

:MakeReplacement
 ( rem - Write to File
	 ECHO ^<;\n^<
	 ECHO ^>;^>\n
 ) >"%#REPLACE%"


:GetLatestURL
 CURL "%#SOURCE%" -o "%#HTML%"
 FOR /F "TOKENS=*" %%U IN ('READABLE "%#HTML%" -f "stable" -x -r "%#REPLACE%" ^| FIND /I "%#SEARCHFOR%"') DO IF NOT DEFINED #DOWNLOAD_URL SET "#DOWNLOAD_URL=%%~U"
 ECHO:
 ECHO Latest Stable Chrome Driver is: "%#DOWNLOAD_URL%"

REM Wrap things up and exit

:ExitBatch
 IF NOT DEFINED DEBUG FOR %%V IN ("%#HTML%" "%#REPLACE%") DO IF EXIST "%%~V" DEL "%%~V" >NUL
 TIMEOUT 60
 ENDLOCAL
 EXIT /B