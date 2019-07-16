import math
import matplotlib.pyplot as plt
import tkinter as tk
import sys
#Aqui va tu programa 
import FormularioPIC as tuprog

tt=tuprog

def leeDatosFormulario():
    iL=int(sL.get())
    iNi=int(sNi.get())
    iWp=int(sWp.get())
    iNpCell=int(senNpCell.get())
    iModo=int(sModo.get())
    fDx0=float(sDx0.get())
    iQm1=int(sQpm1.get())
    iV1=int(sV1.get())
    iQm2=int(sQm2.get())
    iV2=int(sV2.get())
    fDt=float(sDt.get())
    fTol=float(sTol.get())
    iFps=int(sFps.get())
    iSubit=int(sSubit.get())
    bFase=bool(chk_fase.get())
    bRho=bool(chk_Rho.get())
    bPhi=bool(chk_Phi.get())
    listaDatos=[iL,iNi,iWp,iNpCell,iModo,fDx0,iQm1,iV1,iQm2,iV2,fDt,fTol,iFps,iSubit,bFase,bRho,bPhi]
    return listaDatos

def InicioClicked():
    sTexto=btInicioOParada.cget('text');
    if sTexto=="Iniciar":
        btInicioOParada.configure(text="Finalizar")
        #iL,iNi,iWp                   primera fila del formulario
        #iNpCell,iModo,fDx0,iQm1      segunda fila del formulario
        #iV1,iQm2,iV2,fDt             tercera fila
        #fDt,fTol,iFps,iSubit         cuarta fila
        #iSubit,bFase,bRho,bPhi       quinta fila booleanos para definir que gráficos mostrar
        L=leeDatosFormulario()
        iL,iNi,iWp,iNpCell,iModo,fDx0,iQm1,iV1,iQm2,iV2,fDt,fTol,iFps,iSubit,bFase,bRho,bPhi=L        
        tt.bParada=False
        tt.bPause=False
        #L=[iL,iNi,iWp,iNpCell,iModo,fDx0,iQm1,iV1,iQm2,iV2,fDt,fTol,iFps,iSubit,bFase,bRho,bPhi]
        #Aquí va la función de tuprograma llamada tuprog (puedes cambiar el nombre)
        #Tomo como argumento la lista L que contiene los datos que te interesen
        tt.iniciarSimulacion(L)
    else:
        btInicioOParada.configure(text="Iniciar")
        tt.bParada=True
        tt.bPause=False;
        L=leeDatosFormulario()
        iLa,iNia,iWpa,iNpCella,iModoa,fDx0a,iQm1a,iV1a,iQm2a,iV2a,fDta,fTola,iFpsa,iSubita,bFase,bRho,bPhi=L

def SalirClicked():
    sys.exit()
    
def GuardarClicked():
    tt.bSave=True
    sTexto=btGuardar.cget('text');
    btGuardar.configure(text="Guardado")
    L=leeDatosFormulario()
   

def PausarClicked():
    sTexto=btPausar.cget('text');
    if sTexto=="Pausar":
        btPausar.configure(text="Continuar")
        tt.bPause=True
        L=leeDatosFormulario()
    else:
        btPausar.configure(text="Pausar")
        tt.bPause=False
        L=leeDatosFormulario()        

def FaseClicked():
    tuprog.bFase=not tuprog.bFase

def PhiClicked():
    tuprog.bPhi=not tuprog.bPhi

def RhoClicked():
    tuprog.bRho=not tuprog.bRho    

   

window = tk.Tk()
#Tamaño ventana
window.geometry('850x220')
chk_parada = tk.BooleanVar()

#Titulo ventana
window.title("Welcome to LikeGeeks app")
 
#Dominio
Dominio = tk.Label(window, text="Dominio:", font=("Arial Bold", 15))
Dominio.grid(column=0, row=1)

lbLpi = tk.Label(window, text="L/pi:", font=("Arial Bold", 15))
lbLpi.grid(column=1, row=1)
sL=tk.StringVar()
enLpi = tk.Entry(window,width=15,textvariable=sL)
enLpi.grid(column=2,row=1)
sL.set("2")


lbNodos = tk.Label(window, text="Nodos:", font=("Arial Bold", 15))
lbNodos.grid(column=3, row=1)
sNi=tk.StringVar()
enNodos = tk.Entry(window,width=15,textvariable=sNi)
enNodos.grid(column=4,row=1)
sNi.set("64")



lbWp = tk.Label(window, text="Wp:", font=("Arial Bold", 15))
lbWp.grid(column=5, row=1)
sWp=tk.StringVar()
enWp = tk.Entry(window,width=15,textvariable=sWp)
enWp.grid(column=6,row=1)
sWp.set("1")


#Carga
Carga = tk.Label(window, text="Carga:", font=("Arial Bold", 15))
Carga.grid(column=0, row=2)


lbNpCell = tk.Label(window, text="npCell:", font=("Arial Bold", 15))
lbNpCell.grid(column=1,row=2)
senNpCell=tk.StringVar()
enNpCell = tk.Entry(window,width=15,textvariable=senNpCell)
enNpCell.grid(column=2,row=2)
senNpCell.set("20")

lbModo = tk.Label(window, text="Modo:", font=("Arial Bold", 15))
lbModo.grid(column=3, row=2)
sModo=tk.StringVar()
enModo = tk.Entry(window,width=15,textvariable=sModo)
enModo.grid(column=4,row=2)
sModo.set("1")

lbDx0 = tk.Label(window, text="dx0:", font=("Arial Bold", 15))
lbDx0.grid(column=5, row=2)
sDx0=tk.StringVar()
enDx0 = tk.Entry(window,width=15,textvariable=sDx0)
enDx0.grid(column=6,row=2)
sDx0.set("0.0001")

#Especies
Carga = tk.Label(window, text="Especies:", font=("Arial Bold", 15))
Carga.grid(column=0, row=3)

lbQpm1 = tk.Label(window, text="qm1:", font=("Arial Bold", 15))
lbQpm1.grid(column=1,row=3)
sQpm1=tk.StringVar()
enQpm1 = tk.Entry(window,width=15,textvariable=sQpm1)
enQpm1.grid(column=2,row=3)
sQpm1.set("-1")


lbV1 = tk.Label(window, text="v1:", font=("Arial Bold", 15))
lbV1.grid(column=3, row=3)
sV1=tk.StringVar()
enV1 = tk.Entry(window,width=15,textvariable=sV1)
enV1.grid(column=4,row=3)
sV1.set("1")

lbQm2 = tk.Label(window, text="qm2:", font=("Arial Bold", 15))
lbQm2.grid(column=5, row=3)
sQm2=tk.StringVar()
enQm2 = tk.Entry(window,width=15,textvariable=sQm2)
enQm2.grid(column=6,row=3)
sQm2.set("-1")



lbV2 = tk.Label(window, text="v2:", font=("Arial Bold", 15))
lbV2.grid(column=7, row=3)
sV2=tk.StringVar()
enV2 = tk.Entry(window,width=15,textvariable=sV2)
enV2.grid(column=8,row=3)
sV2.set("-1")



#Solver
Solver = tk.Label(window, text="Solucionador:", font=("Arial Bold", 15))
Solver.grid(column=0, row=4)


lbDt = tk.Label(window, text="dt:", font=("Arial Bold", 15))
lbDt.grid(column=1,row=4)
sDt=tk.StringVar()
enDt = tk.Entry(window,width=15,textvariable=sDt)
enDt.grid(column=2,row=4)
sDt.set("0.1")


lbTol = tk.Label(window, text="Tolerancia:", font=("Arial Bold", 15))
lbTol.grid(column=3, row=4)
sTol=tk.StringVar()
enTol = tk.Entry(window,width=15,textvariable=sTol)
enTol.grid(column=4,row=4)
sTol.set("0.000001")



lbFps = tk.Label(window, text="fps:", font=("Arial Bold", 15))
lbFps.grid(column=5, row=4)
sFps=tk.StringVar()
enFps = tk.Entry(window,width=15,textvariable=sFps)
enFps.grid(column=6,row=4)
sFps.set("10")



lbSubit = tk.Label(window, text="Sub it:", font=("Arial Bold", 15))
lbSubit.grid(column=7, row=4)
sSubit=tk.StringVar()
enSubit = tk.Entry(window,width=15,textvariable=sSubit)
enSubit.grid(column=8,row=4)
sSubit.set("1")

#Gráficos
Graficos = tk.Label(window, text="Gráficos:", font=("Arial Bold", 15))
Graficos.grid(column=0, row=5)

chk_fase = tk.BooleanVar()
chk_fase.set(True)
cbFase = tk.Checkbutton(window, text="xvFase:", font=("Arial Bold", 15),var=chk_fase,command=FaseClicked)
cbFase.grid(column=1,row=5)


chk_Rho = tk.BooleanVar()
chk_Rho.set(False)
cbRho = tk.Checkbutton(window, text="Rho:", font=("Arial Bold", 15),var=chk_Rho,command=RhoClicked)
cbRho.grid(column=2,row=5)

chk_Phi = tk.BooleanVar()
chk_Phi.set(False)
cbPhi = tk.Checkbutton(window, text="Phi:", font=("Arial Bold", 15),var=chk_Phi,command=PhiClicked)
cbPhi.grid(column=3,row=5)


btInicioOParada = tk.Button(window, text="Iniciar",bg="orange", fg="red",font=("Arial Bold", 15),command=InicioClicked) 
btInicioOParada.grid(column=0, row=6)

btPausar = tk.Button(window, text="Pausar",bg="orange", fg="red",font=("Arial Bold", 15),command=PausarClicked) 
btPausar.grid(column=1, row=6)

#btSalir = tk.Button(window, text="Fin",bg="orange", fg="red",font=("Arial Bold", 15),command=SalirClicked) 
#btSalir.grid(column=2, row=6)

#btGuardar = tk.Button(window, text="Guardar imagen",bg="orange", fg="red",font=("Arial Bold", 15),command=GuardarClicked) 
#btGuardar.grid(column=2, row=6)

leeDatosFormulario()

 
window.mainloop()

