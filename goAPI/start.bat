REM start.bat

SET PATH=D:\oracle_instantclient;%PATH%

setx CGO_CFLAGS "D:\oracle_instantclient\sdk\include"
setx CGO_LDFLAGS "-LD:\oracle_instantclient -loci"
setx PKG_CONFIG_PATH "D:\msys64\mingw64\lib\pkgconfig"
setx path "%path%;D:\msys64\mingw64\bin;D:\msys64"