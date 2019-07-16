import math
import matplotlib.pyplot as plt
import tkinter as tk

bParada=False
bSave=False
bFase=True
bPhi=False
bRho=False
bPause=False

#### ESTE PROGRAMA FUNCIONA A PARTIR DE EL PROGRAMA FORMULARIO.PY
def part(x,v,tag,q,m):
    return (x,v,tag,q,m,q/m)

	#sets scaling
def setRange(x0,x1,y0,y1):
    return (x0,x1-x0,y0,y1-y0)

#plotting function
def plots(parts,ni,rho,phi,L,vmag0,ax):
    np=len(parts)
    KE=0
    PE=0
    for p in range(0,np):
        P = parts[p]
        x,v,tag,q,m,qm=P
        KE=KE+m*v*v
    KE=KE*0.5
    #print('KE=',KE)

    for i in range(0,ni):
        PE =PE+rho[i]*phi[i]
    PE=PE*0.5

    phi_min=phi[0]
    phi_max=phi[0]
    for i in range(0,ni):
        if phi[i]<phi_min:
            phi_min=phi[i]
        if phi[i]>phi_max:
            phi_max=phi[i]
    plt.xlim(0,L)
    plt.ylim(-3*vmag0,3*vmag0)
    EXB=[]
    EVB=[]
    EXR=[]
    EVR=[]
    for p in range(0,np):
        P = parts[p]
        x,v,tag,q,m,qm=P
        if tag==0:
            EXR.append(x)
            EVR.append(v)
        else:
            EXB.append(x)
            EVB.append(v)        
        
                
            
    #dibuja gráfico naranja
    ax.scatter(EXR,EVR)
    #dibuja gráfico azul
    ax.scatter(EXB,EVB)


def step(ni,rho,phi,ef,dt,n_sub_it,tol,dh,parts,fps,int_id,q0,EPS0,L,it):

    np=len(parts)
    for sub_it in range(0,n_sub_it):
        #clear rho
        for i in range(0,ni):
            rho[i] = 0
        #scatter particles to grid

        for p in range(0,np):
  
            #get particle logical coordinate*/
            P=parts[p]
            x,v,tag,q,m,qm=P            
            lc = x/dh

            i = math.floor(lc)
            d = lc-i

            rho[i]=rho[i]+q*(1-d)
            rho[i+1]=rho[i+1]+q*d

        
        #add stationary background charges,ni-1 because last and first node are the same*
        for i in range(0,ni-1):
            rho[i] = rho[i]+q0*(np/(ni-1))          

        rho[ni-1]=rho[ni-1]+rho[0]
        rho[0]=rho[ni-1]

	#divide by cell size to get charge density
        for i in range(0,ni):
            rho[i]=rho[i]/dh
          
        #remove noise
        for i in range(0,ni):
            if (math.fabs(rho[i])<1e-10):
                rho[i]=0

      #Solución del Potencial Gauss Seidel
        phi[0]=0
        for j in range(0,ni):
            phi[j]=0

        for solver_it in range(0,20000):
            for i in range(0,ni-1):
                im = i-1
                if im<0:
                    im=ni-2
                ip=i+1
                if ip==ni-1:
                    ip=0
                g = 0.5*((rho[i]/EPS0)*dh*dh+phi[im]+phi[ip])
                phi[i] = phi[i]+1.4*(g-phi[i])
   
            #Verifica convergencia
            if solver_it%25==0:
                sum=0
                for i in range(1,ni-1):
                    ip = i+1
                    if (ip==ni-1):
                        ip=0
                    res=rho[i]/EPS0+(phi[i-1]-2*phi[i]+phi[ip])/(dh*dh)
                    sum = sum+res*res
                l2=math.sqrt(sum/ni)
                if l2<tol:
                    #print('RUPTURA it', it, 'solver_it', solver_it)
                    print ("Tolerancia:",l2)
                    break;
        phi[ni-1]=phi[0]

        #electric field
        for i in range(0,ni):
            im=i-1
            ip=i+1
            if im<0:
                im=ni-2
            if ip>ni-1:
                ip=1
            ef[i]=(phi[im]-phi[ip])/(2*dh)
        #update positions
        for p in range(0,np):
            P=parts[p]
            x,v,tag,q,m,qm=P
            #interpolate EF to particle position
            lc =x/dh
            i=math.floor(lc)
            d=lc-i
            ef_p=ef[i]*(1-d)+ef[i+1]*d
            #first time rewind velocity 0.5dt
            #if it==0:
            #    v=v-0.5*ef_p*qm*dt
            #update velocity
            v=v+ef_p*qm*dt
            #update position
            x =x+v*dt
            #periodic boundary for particles
            if x<0:
                x=x+L
            if x>=L:
                x =x-L
            parts[p]=x,v,tag,q,m,qm  #Retorna los valores cambiados en STEP
                    
			

def iniciarSimulacion(listaDatos):
    bFase,bRho,bPhi=True,False,False #No se están usando estos sino los del formulario
    L,num_cells,wp,np_cell,mode,dx0,qm1,vmag1,qm2,vmag2,dt,tol,fps,n_sub_it,bFase,bRho,bPhi=listaDatos
    print(listaDatos)
    delay=0
    sc_plotvisible=True #Para señalar que si se muestra gráfico
    hist_plotvisible=False  #Para señalar que no se mostrará histograma
    phi_plotvisible=False  #Para señalar que no se mostrará phi

    ni=num_cells+1

    dt=0.1 #de formulario
    np = (num_cells)*np_cell
    L= L*math.pi
    print("L=",L)

      
    #Conjunto promedio de los vmag para las gráficas
    vmag0 = 0.5*(abs(vmag1)+abs(vmag2))

            
    # Cargas desde la frecuencia del plasma.
    EPS0=1
    q1 = wp*wp*(1/qm1)*EPS0*L/(0.5*np)
    q2 = wp*wp*(1/qm2)*EPS0*L/(0.5*np)
                    
    #charge of the neutralizing background
    q0 = -0.5*(q1+q2)
                    
    #masses, only used for energy
    m1 = q1/qm1
    m2 = q2/qm2  
    parts = []  #vector vacío

    delta_x = L/np
    print(np)

    for p in range(0, np):
        x0 = (p+0.5)*delta_x
        #perturb positions
        theta = 2*math.pi*mode*x0/L
        dx = dx0*math.cos(theta)
        x1 = x0+dx
        x2 = x0-dx
        if x1<0:
            x1=x1+L
        if x2<0:
            x2=x2+L
        if x1>=L:
            x1=x1-L
        if x2>=L:
            x2=x2-L
        parts.append(part(x1,vmag1,0,q1,m1))   
        parts.append(part(x2,vmag2,1,q2,m2))
    dh = L/(ni-1)	#cell spacing

    #reset fields
    l2 = 0
    phi = []
    ef = []
    rho = []
    x = []
    for i in range(0, ni):
        phi.append(0)
        ef.append(0)
        rho.append(0)
        x.append(i*dh)
    time = 0
    it = 0
    int_id=2  #no se va a usar pero se coloca
    it=0
    bSave=False
    plt.ion()
    bGuardo=False
    while True:
        if bSave:
            plt.pause(0.001)
            ax1.savefig('DensidadCarga{0}.png'.format(it))
            print("SALVANDO IMAGEN")
            break
 
        if bPause:
            plt.pause(0.001)
            if not bGuardo:
                sNombreArchivo='DensidadCarga{0}.png'.format(it)
                plt.savefig(sNombreArchivo)
                print("SALVANDO IMAGEN ",sNombreArchivo)
                bGuardo=True
            continue        
        if bParada:
             break

        bGuardo=False    
        print('Paso:',it)
        print(bParada,bPause) 
        step(ni,rho,phi,ef,dt,n_sub_it,tol,dh,parts,fps,int_id,q0,EPS0,L,it)
        it=it+1

        if it%2==0 and it>0:
            plt.clf()            
            ax1=plt.subplot2grid((2,2),(0,0),colspan=1,rowspan=1)
            ax2=plt.subplot2grid((2,2),(1,0),colspan=1,rowspan=1)
            ax3=plt.subplot2grid((2,2),(1,1),colspan=1,rowspan=1)
            if bFase:
                plots(parts,ni,rho,phi,L,vmag0,ax1)
            #plt.subplot2grid((2,2),(0,1),colspan=2,rowspan=1)
            #Aquí se grafica el potencial eléctrico
            if bRho:
                ax2.plot(x,phi)
            #plt.subplot2grid((2,2),(1,0),colspan=1,rowspan=1)
            #Aquí se grafica la densidad de carga
            if bPhi:
                ax3.plot(x,rho)
            plt.pause(0.0001)









    
    









    





