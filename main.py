from mpi4py import MPI
import func
import T1, T2, T3, T4
import timeit
#-------------------------------
#Паралельне програмування
#ПКС2СП на мові Python
#MA= min (D)*MX*MR – (D*C)*(MZ*MD)
#Лаппо Максим
#групаІО-91
#12.12.21
#-------------------------------
start = timeit.default_timer()
comm=MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
N=2400
if rank == 0:
    print("Task", rank + 1, "start")
    e = func.oneVector(N)
    d = func.oneVector(N)
    md = func.oneMatr(N)
    t1 = T1.T1(d, e, md)
    #Передати в т2
    comm.send(t1.d, dest=1)
    comm.send(t1.e, dest=1)
    comm.send(t1.md, dest=1)
    # Передати в т4
    comm.send(t1.d, dest=3)
    comm.send(t1.e, dest=3)
    comm.send(t1.md, dest=3)
    #Прийняти з Т2
    data_mc1 = comm.recv(source=1)
    data_c1 = comm.recv(source=1)
    #прийняти з т4
    data_mr1 = comm.recv(source=3)
    data_mz1 = comm.recv(source=3)
    #Передати в т4
    comm.send(data_mc1, dest=3)
    comm.send(data_c1, dest=3)
    #Передати в т2
    comm.send(data_mr1, dest=1)
    comm.send(data_mz1, dest=1)
    #прийняти мін з т4
    data_min_k4 = comm.recv(source=3)
    #обчислити мін к14
    min_k14 = t1.minimal(e,data_min_k4)
    #передати к14 в т2
    comm.send(min_k14, dest=1)
    #прийняти к від т2
    data_min_k1 = comm.recv(source=1)
    #передати к в т4
    comm.send(data_min_k1, dest=3)
    #обчислити ма1
    min_k1 = t1.minVect(e)
    ma1 = t1.res1(t1.d, t1.md, min_k1, data_mc1,data_c1,data_mr1,data_mz1)
    #прийняти ма4 від т4
    data_ma4 = comm.recv(source=3)
    #обчислити ма14
    ma14 = t1.sum_ma14(ma1,data_ma4)
    #передати ма14 в т2
    comm.send(ma14, dest=1)

    # -----Отправляет ma1 в Т2---------
    print("Task", rank + 1, "end")

if rank == 1:
    print("Task", rank + 1, "start")
    mc = func.oneMatr(N)
    c = func.oneVector(N)
    t2 = T2.T2(mc,c)
    #прийняти з т1
    data_d2 = comm.recv(source=0)
    data_e2 = comm.recv(source=0)
    data_md2 = comm.recv(source=0)
    data_mr2 = comm.recv(source=0)
    data_mz2 = comm.recv(source=0)
    #передати в т3
    comm.send(data_d2, dest=2)
    comm.send(data_e2, dest=2)
    comm.send(data_md2, dest=2)
    comm.send(t2.mc, dest=2)
    comm.send(t2.c, dest=2)
    comm.send(t2.mc, dest=0)
    comm.send(t2.c, dest=0)
    #обчислити к2
    min_k2 = t2.minVect(data_e2)
    #прийняти від т1 к14
    data_min_k14 = comm.recv(source=0)
    # прийняти від т3 к3
    data_min_k3 = comm.recv(source=2)
    #обчислити к
    min_k = t2.minimal(min_k2,data_min_k3,data_min_k14)
    #передати в т1 т3 к
    comm.send(min_k,dest=1)
    comm.send(min_k,dest=0)
    #обчислити ма2
    ma2 = t2.res2(data_d2,data_md2,min_k2,t2.mc,t2.c,data_mr2,data_mz2)
    #прийняти ма14 від т1
    data_ma14 = comm.recv(source=0)
    #прийняти ма3 від т3
    data_ma3 = comm.recv(source=2)
    # обчислити ма
    ma = ma2 + data_ma14 + data_ma3
    print("Result Task", rank + 1, "=\n", ma)
    print("Task", rank + 1, "end")
if rank == 2:
    print("Task", rank + 1, "start")
    t3 = T3.T3()
    #прийняти від т2, т4
    data_d3 = comm.recv(source=1)
    data_e3 = comm.recv(source=1)
    data_md3 = comm.recv(source=1)
    data_mc3 = comm.recv(source=1)
    data_c3 = comm.recv(source=1)
    data_mr3 = comm.recv(source=3)
    data_mz3 = comm.recv(source=3)
    #передати в т4
    comm.send(data_mc3, dest=3)
    comm.send(data_c3, dest=3)
    #обчислити к3
    min_k3 = t3.minimal(data_e3)
    #передати к3 в т2
    comm.send(min_k3, dest=1)
    #прийняти к з т2
    data_min_k3 = comm.recv(source=1)
    #обчислити ма3
    ma3 = t3.res3(data_d3,data_md3,data_min_k3,data_mc3,data_c3,data_mr3,data_mz3)
    #передати ма3 в т2
    comm.send(ma3, dest=1)
    print("Task", rank + 1, "end")
if rank == 3:
    print("Task", rank + 1, "start")
    mr = func.oneMatr(N)
    mz = func.oneMatr(N)
    t4 = T4.T4(mr, mz)
    #передати в т1 т3
    comm.send(t4.mr, dest=0)
    comm.send(t4.mz, dest=0)
    comm.send(t4.mr, dest=2)
    comm.send(t4.mz, dest=2)
    # прийняти від т1
    data_d4 = comm.recv(source=0)
    data_e4 = comm.recv(source=0)
    data_md4 = comm.recv(source=0)
    #прийняти від т3
    data_mc4 = comm.recv(source=2)
    data_c4 = comm.recv(source=2)
    #обчислити k4
    min_k4 = t4.minimal(data_e4)
    #передати k4 в т1
    comm.send(min_k4, dest=0)
    #прийняти к з т1
    data_min_k4 = comm.recv(source=1)
    #обчислити ма4
    ma4 = t4.res4(data_d4,data_md4,min_k4,data_mc4,data_c4,t4.mr,t4.mz)
    #передати ма4 в т1
    comm.send(ma4, dest=0)

    print("Task", rank + 1, "end")

stop = timeit.default_timer()
print("The total elapsed time of the program is: ", stop-start)
