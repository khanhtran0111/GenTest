setlocal enabledelayedexpansion
set code=%~n0
set count=0
set testfol=test
g++ -std=c++17 %code%.cpp -o %code%.exe
for /D %%i in (*) do (
%code% < %%~nxi\%code%.INP > %%~nxi\%code%.OUT
)