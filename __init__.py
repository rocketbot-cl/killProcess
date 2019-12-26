# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

import os
import platform
import signal

"""
    Obtengo el modulo que fue invocado
"""
module = GetParams("module")

if module == "killProcess":

    pid_ = os.getpid()
    print(pid_)
    #pid_ = int(pid_)

    try:
        platform_ = platform.system().lower()
        print(platform_)

        if platform_ == 'windows':
            subprocess.Popen("taskkill /F /T /PID %i" % pid_, shell=True)
        else:
            os.kill(-pid_,signal.SIGTERM)


    except Exception as e:
        PrintException()
        raise (e)



