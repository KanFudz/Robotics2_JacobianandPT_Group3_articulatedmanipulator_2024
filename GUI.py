from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
import roboticstoolbox as rtb
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH
import sympy as sp


# Create GUI Window with title
root = Tk()
root.title('Articulated Calculator')
root.resizable(False, False)
root.geometry("600x400")
pc = PhotoImage(file="/home/john/Rob2_3202/bgrobo.png")  #Make sure to change the file address to where the bgrobo is located in your files after downloading the photo.
#Also check the filename if it's correct.  Make sure that it is in png image type.
blabel=Label(root,image=pc)
blabel.place(x=0,y=0, relwidth=1, relheight=1)


def Forward_Kinematics():
    global a1_entry, a2_entry, a3_entry, T1_entry, T2_entry, T3_entry, X_output, Y_output, Z_output

    # Create entry fields for link lengths
    a1_label = Label(root, text="a1:", padx=5, pady=5, bg='#012228', fg='white')
    a1_label.grid(row=1, column=0, sticky=W)
    a1_entry = Entry(root, width=10)
    a1_entry.grid(row=1, column=1, padx=5, pady=5)
    a1_label =  Label(root,text=('cm'), padx=5, pady=5, bg='#012228', fg='white')
    a1_label.grid(row=1, column=2, sticky=W)


    a2_label = Label(root, text="a2:", padx=5, pady=5, bg='#032b28', fg='white')
    a2_label.grid(row=2, column=0, sticky=W)
    a2_entry = Entry(root, width=10)
    a2_entry.grid(row=2, column=1, padx=5, pady=5)
    a2_label =  Label(root,text=('cm'), padx=5, pady=5, bg='#032b28', fg='white')
    a2_label.grid(row=2, column=2, sticky=W)



    a3_label = Label(root, text="a3:", padx=5, pady=5, bg='#0d3f2e', fg='white')
    a3_label.grid(row=3, column=0, sticky=W)
    a3_entry = Entry(root, width=10)
    a3_entry.grid(row=3, column=1, padx=5, pady=5)
    a3_label = Label(root, text="cm", padx=5, pady=5, bg='#0d3f2e', fg='white')
    a3_label.grid(row=3, column=2, sticky=W)

    # Create entry fields for joint variables
    T1_label = Label(root, text="T1:", padx=5, pady=5, bg='#1f563e', fg='white')
    T1_label.grid(row=4, column=0, sticky=W)
    T1_entry = Entry(root, width=10)
    T1_entry.grid(row=4, column=1, padx=5, pady=5)
    T1_label = Label(root, text="°", padx=5, pady=5, bg='#1f563e', fg='white')
    T1_label.grid(row=4, column=2, sticky=W)


    T2_label = Label(root, text="T2:", padx=5, pady=5, bg='#136345', fg='white')
    T2_label.grid(row=5, column=0, sticky=W)
    T2_entry = Entry(root, width=10)
    T2_entry.grid(row=5, column=1, padx=5, pady=5)
    T2_label = Label(root, text="°", padx=5, pady=5, bg='#136345', fg='white')
    T2_label.grid(row=5, column=2, sticky=W)


    T3_label = Label(root, text="T3:", padx=5, pady=5, bg='#117955', fg='white')
    T3_label.grid(row=6, column=0, sticky=W)
    T3_entry = Entry(root, width=10)
    T3_entry.grid(row=6, column=1, padx=5, pady=5)
    T3_label = Label(root, text="°", padx=5, pady=5, bg='#117955', fg='white')
    T3_label.grid(row=6, column=2, sticky=W)

    # Create output fields for position vector components
    X_label = Label(root, text="X:", padx=5, pady=5, bg='#3e8e6f')
    X_label.grid(row=7, column=0, sticky=W)
    X_output = Entry(root, width=10, state='readonly')
    X_output.grid(row=7, column=1, padx=5, pady=5)
    X_label = Label(root, text="cm", padx=5, pady=5, bg='#3e8e6f')
    X_label.grid(row=7, column=2, sticky=W)

    Y_label = Label(root, text="Y:", padx=5, pady=5, bg='#539d85')
    Y_label.grid(row=8, column=0, sticky=W)
    Y_output = Entry(root, width=10, state='readonly')
    Y_output.grid(row=8, column=1, padx=5, pady=5)
    Y_label = Label(root, text="cm", padx=5, pady=5, bg='#539d85')
    Y_label.grid(row=8, column=2, sticky=W)

    Z_label = Label(root, text="Z:", padx=5, pady=5, bg='#65ae91')
    Z_label.grid(row=9, column=0, sticky=W)
    Z_output = Entry(root, width=10, state='readonly')
    Z_output.grid(row=9, column=1, padx=5, pady=5)
    Z_label = Label(root, text="cm", padx=5, pady=5, bg='#65ae91')
    Z_label.grid(row=9, column=2, sticky=W)

    # Create two buttons
    calculate_btn = Button(root, text="Calculate", command=calculate_forward)
    calculate_btn.grid(row=10, column=0, padx=5, pady=5)

    reset_btn = Button(root, text="Reset", bg='#AE2012', command=reset_field1)
    reset_btn.grid(row=10, column=1, padx=5, pady=5)


def Inverse_Kinematics():
    global a1_entry_inv, a2_entry_inv, a3_entry_inv, X_entry, Y_entry, Z_entry, T1_output, T2_output, T3_output

    # Create entry fields for link lengths
    a1_label_inv = Label(root, text="a1:", padx=5, pady=5, bg='#220203', fg='white')
    a1_label_inv.grid(row=1, column=4, sticky=W)
    a1_entry_inv = Entry(root, width=10)
    a1_entry_inv.grid(row=1, column=5, padx=5, pady=5)
    a1_label_inv = Label(root, text="cm", padx=5, pady=5, bg='#220203', fg='white')
    a1_label_inv.grid(row=1, column=6, sticky=W)


    a2_label_inv = Label(root, text="a2:", padx=5, pady=5, bg='#380506', fg='white')
    a2_label_inv.grid(row=2, column=4, sticky=W)
    a2_entry_inv = Entry(root, width=10)
    a2_entry_inv.grid(row=2, column=5, padx=5, pady=5)
    a2_label_inv = Label(root, text="cm", padx=5, pady=5, bg='#380506', fg='white')
    a2_label_inv.grid(row=2, column=6, sticky=W)

    a3_label_inv = Label(root, text="a3:", padx=5, pady=5, bg='#540f0d', fg='white')
    a3_label_inv.grid(row=3, column=4, sticky=W)
    a3_entry_inv = Entry(root, width=10)
    a3_entry_inv.grid(row=3, column=5, padx=5, pady=5)
    a3_label_inv = Label(root, text="cm", padx=5, pady=5, bg='#540f0d', fg='white')
    a3_label_inv.grid(row=3, column=6, sticky=W)

    # Create entry fields for position vector components
    X_label = Label(root, text="X:", padx=5, pady=5, bg='#6b0500', fg='white')
    X_label.grid(row=4, column=4, sticky=W)
    X_entry = Entry(root, width=10)
    X_entry.grid(row=4, column=5, padx=5, pady=5)
    X_label = Label(root, text="cm", padx=5, pady=5, bg='#6b0500', fg='white')
    X_label.grid(row=4, column=6, sticky=W)

    Y_label = Label(root, text="Y:", padx=5, pady=5, bg='#87080a', fg='white')
    Y_label.grid(row=5, column=4, sticky=W)
    Y_entry = Entry(root, width=10)
    Y_entry.grid(row=5, column=5, padx=5, pady=5)
    Y_label = Label(root, text="cm", padx=5, pady=5, bg='#87080a', fg='white')
    Y_label.grid(row=5, column=6, sticky=W)

    Z_label = Label(root, text="Z:", padx=5, pady=5, bg='#980b06', fg='white')
    Z_label.grid(row=6, column=4, sticky=W)
    Z_entry = Entry(root, width=10)
    Z_entry.grid(row=6, column=5, padx=5, pady=5)
    Z_label = Label(root, text="cm", padx=5, pady=5, bg='#980b06', fg='white')
    Z_label.grid(row=6, column=6, sticky=W)

    # Create output fields for joint variables
    T1_label = Label(root, text="T1:", padx=5, pady=5, bg='#ae120a')
    T1_label.grid(row=7, column=4, sticky=W)
    T1_output = Entry(root, width=10, state='readonly')
    T1_output.grid(row=7, column=5, padx=5, pady=5)
    T1_label = Label(root, text="°", padx=5, pady=5, bg='#ae120a')
    T1_label.grid(row=7, column=6, sticky=W)

    T2_label = Label(root, text="T2:", padx=5, pady=5, bg='#c02a2a')
    T2_label.grid(row=8, column=4, sticky=W)
    T2_output = Entry(root, width=10, state='readonly')
    T2_output.grid(row=8, column=5, padx=5, pady=5)
    T2_label = Label(root, text="°", padx=5, pady=5, bg='#c02a2a')
    T2_label.grid(row=8, column=6, sticky=W)

    T3_label = Label(root, text="T3:", padx=5, pady=5, bg='#d04346')
    T3_label.grid(row=9, column=4, sticky=W)
    T3_output = Entry(root, width=10, state='readonly')
    T3_output.grid(row=9, column=5, padx=5, pady=5)
    T3_label = Label(root, text="°", padx=5, pady=5, bg='#d04346')
    T3_label.grid(row=9, column=6, sticky=W)

    # Create two buttons
    calculate_btn_inv = Button(root, text="Calculate", command=calculate_inverse)
    calculate_btn_inv.grid(row=10, column=4, padx=5, pady=5)

    reset_btn_inv = Button(root, text="Reset", bg='#AE2012', command=reset_field2)
    reset_btn_inv.grid(row=10, column=5, padx=5, pady=5)


def calculate_forward():
    try:
        # Get values from entry fields
        a1 = float(a1_entry.get())/100
        a2 = float(a2_entry.get())/100
        a3 = float(a3_entry.get())/100
        T1 = float(T1_entry.get())
        T2 = float(T2_entry.get())
        T3 = float(T3_entry.get())

        # Convert joint angles to radians
        T1 = (T1 / 180.0) * np.pi
        T2 = (T2 / 180.0) * np.pi
        T3 = (T3 / 180.0) * np.pi

        # Perform forward kinematics calculations
        # Parametric Table (theta, alpha, r, d)
        PT = [[T1, (90.0 / 180.0) * np.pi, 0, a1],
              [T2, (0.0 / 180.0) * np.pi, a2, 0],
              [T3, (0.0 / 180.0) * np.pi, a3, 0]]

        # Homogeneous Transformation Matrices (HTM)
        i = 0
        H0_1 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
            [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
            [0,np.sin(PT[i][1]), np.cos(PT[i][1]),PT[i][3]],
            [0,0,0,1]]

        i = 1
        H1_2 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
            [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
            [0,np.sin(PT[i][1]), np.cos(PT[i][1]),PT[i][3]],
            [0,0,0,1]]

        i = 2
        H2_3 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
            [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
            [0,np.sin(PT[i][1]), np.cos(PT[i][1]),PT[i][3]],
            [0,0,0,1]]

        H0_1 = np.matrix (H0_1)
        H1_2 = np.matrix (H1_2)
        H2_3 = np.matrix (H2_3)

        H0_2 = np.dot(H0_1,H1_2)
        H0_3 = np.dot(H0_2,H2_3)

        X0_3 = H0_3[0, 3]
        Y0_3 = H0_3[1, 3]
        Z0_3 = H0_3[2, 3]

        # Display the results in the output fields
        X_output.config(state='normal')
        X_output.delete(0, END)
        X_output.insert(0, np.around(X0_3*100,3))
        X_output.config(state='readonly')

        Y_output.config(state='normal')
        Y_output.delete(0, END)
        Y_output.insert(0, np.around(Y0_3*100,3))
        Y_output.config(state='readonly')

        Z_output.config(state='normal')
        Z_output.delete(0, END)
        Z_output.insert(0, np.around(Z0_3*100,3))
        Z_output.config(state='readonly')

        ## Jacobian Matrix
        #Jacobian Window
        J_sw = Toplevel()
        J_sw.title("Velocity Calculator")
        J_sw.resizable(False,False)
        J_sw.config(bg='#000000')
    
             #1. Linear/Translation Vectors
        Z_1 = [[0],[0],[1]] #The [0,0,1] vector

        #Row 1 to 3, Column 1
        J1a = [[1,0,0],
               [0,1,0],
               [0,0,1]] #R0_0
        J1a = np.dot(J1a,Z_1)

        J1b_1 = H0_3[0:3,3]
        J1b_1 = np.array (J1b_1)

        J1b_2 = [[0],[0],[0]]
        J1b_2 = np.array (J1b_2)

        J1b = J1b_1 - J1b_2

        J1 = [[(J1a[1,0]*J1b[2,0])-(J1a[2,0]*J1b[1,0])],
              [(J1a[2,0]*J1b[0,0])-(J1a[0,0]*J1b[2,0])],
              [(J1a[0,0]*J1b[1,0])-(J1a[1,0]*J1b[0,0])]]
        
        J1 = np.array(J1)
        
        #Row 1 to 3, column 2
        J2a = H0_1[0:3,0:3] 
        J2a = np.dot(J2a,Z_1)

        J2b_1 = H0_3[0:3,3:] #d0_3
        J2b_1 = np.array(J2b_1)

        J2b_2 = H0_1[0:3,3:] #d0_1
        J2b_2 = np.array(J2b_2)

        J2b = J2b_1 - J2b_2

        J2 = [[J2a[1,0]*J2b[2,0] - J2a[2,0]*J2b[1,0]],
            [J2a[2,0]*J2b[0,0] - J2a[0,0]*J2b[2,0]],
            [J2a[0,0]*J2b[1,0] - J2a[1,0]*J2b[0,0]]]

        J2 = np.array(J2)

        #Row 1 to 3, column 3
        J3a = H0_2[0:3,0:3] 
        J3a = np.dot(J3a,Z_1)

        J3b_1 = H0_3[0:3,3:] #d0_3
        J3b_1 = np.array(J3b_1)

        J3b_2 = H0_2[0:3,3:] #d0_2
        J3b_2 = np.array(J3b_2)

        J3b = J3b_1 - J3b_2

        J3 = [[J3a[1,0]*J3b[2,0] - J3a[2,0]*J3b[1,0]],
            [J3a[2,0]*J3b[0,0] - J3a[0,0]*J3b[2,0]],
            [J3a[0,0]*J3b[1,0] - J3a[1,0]*J3b[0,0]]]

        J3 = np.array(J3)

        #2. Rotation / Orientation Vectors
        #Row 4 to 6, Column 1
        J4 = [[0],[0],[1]]
        J4 = np.array(J4)

        #Row 4 to 6, Column 2
        J5 = J2a
        J5 = np.array(J5)

        #Row 4 to 6, Column 3
        J6 = J3a
        J6 = np.array(J6)

        #3. Concatenated Jacobian Matrix
        JM1 = np.concatenate((J1,J2,J3),1)
        JM2 = np.concatenate((J4,J5,J6),1)

        J = np.concatenate((JM1,JM2),0)
        J = np.matrix(J)

        def update_velo():
            T1p = T1_slider.get()
            T2p = T2_slider.get()
            T3p = T3_slider.get()

            q = np.array([[T1p],[T2p],[T3p]])
            E = np.dot(J,q)

            xp_e = E[0,0]
            x_entry.config(state='normal')
            x_entry.delete(0, END)
            x_entry.insert(0, np.around(xp_e,3))
            x_entry.config(state='readonly')

            yp_e = E[1,0]
            y_entry.config(state='normal')
            y_entry.delete(0, END)
            y_entry.insert(0, np.around(yp_e,3))
            y_entry.config(state='readonly')


            zp_e = E[2,0]
            z_entry.config(state='normal')
            z_entry.delete(0, END)
            z_entry.insert(0, np.around(zp_e,3))
            z_entry.config(state='readonly')

            ωx_e = E[3,0]
            ωx_entry.config(state='normal')
            ωx_entry.delete(0, END)
            ωx_entry.insert(0, np.around(ωx_e,3))
            ωx_entry.config(state='readonly')

            ωy_e = E[4,0]
            ωy_entry.config(state='normal')
            ωy_entry.delete(0, END)
            ωy_entry.insert(0, np.around(ωy_e,3))
            ωy_entry.config(state='readonly')

            ωz_e = E[5,0]
            ωz_entry.config(state='normal')
            ωz_entry.delete(0, END)
            ωz_entry.insert(0, np.around(ωz_e,3))
            ωz_entry.config(state='readonly')

        # Jacobian Sliders
        T1_velo = Label(J_sw,text=("θ1* = "),font=(5), bg='#010128', fg='white') 
        T1_slider = Scale(J_sw,from_=0,to_=3,orient=HORIZONTAL,length=100,sliderlength=10, bg="white")
        T1_unit = Label(J_sw,text=("rad/s"),font=(5), bg='#010128', fg='white')

        T2_velo = Label(J_sw,text=("θ2* = "),font=(5), bg='#06063C', fg='white') 
        T2_slider = Scale(J_sw,from_=0,to_=3,orient=HORIZONTAL,length=100,sliderlength=10, bg="white")
        T2_unit = Label(J_sw,text=("rad/s"),font=(5), bg='#06063C', fg='white')

        T3_velo = Label(J_sw,text=("θ3* = "),font=(5), bg='#0D075F', fg='white') 
        T3_slider = Scale(J_sw,from_=0,to_=3,orient=HORIZONTAL,length=100,sliderlength=10, bg="white")
        T3_unit = Label(J_sw,text=("rad/s"),font=(5), bg='#0D075F', fg='white')

        T1_velo.grid(row=0,column=0, padx=5, pady=5)
        T1_slider.grid(row=0,column=1, padx=5, pady=5)
        T1_unit.grid(row=0,column=2, padx=5, pady=5)

        T2_velo.grid(row=1,column=0, padx=5, pady=5)
        T2_slider.grid(row=1,column=1, padx=5, pady=5)
        T2_unit.grid(row=1,column=2, padx=5, pady=5)

        T3_velo.grid(row=2,column=0, padx=5, pady=5)
        T3_slider.grid(row=2,column=1, padx=5, pady=5)
        T3_unit.grid(row=2,column=2, padx=5, pady=5)

        # Jacobian Entries and Labels
        x_velo = Label(J_sw,text=("x* = "),font=(5), bg='#070774', fg='white')
        x_entry = Entry(J_sw,width=10,font=(10), state='readonly')
        x_unit = Label(J_sw,text=("cm/s"),font=(5), bg='#070774', fg='white')
        x_velo.grid(row=3,column=0, padx=5, pady=5)
        x_entry.grid(row=3,column=1, padx=5, pady=5)
        x_unit.grid(row=3,column=2, padx=5, pady=5)

        y_velo = Label(J_sw,text=("y* = "),font=(5), bg='#0F0F8E', fg='white') 
        y_entry = Entry(J_sw,width=10,font=(10), state='readonly')
        y_unit = Label(J_sw,text=("cm/s"),font=(5), bg='#0F0F8E', fg='white')
        y_velo.grid(row=4,column=0, padx=5, pady=5)
        y_entry.grid(row=4,column=1, padx=5, pady=5)
        y_unit.grid(row=4,column=2, padx=5, pady=5)

        z_velo = Label(J_sw,text=("z* = "),font=(5), bg='#2525A6', fg='white')
        z_entry = Entry(J_sw,width=10,font=(10), state='readonly')
        z_unit = Label(J_sw,text=("cm/s"),font=(5), bg='#2525A6', fg='white')
        z_velo.grid(row=5,column=0, padx=5, pady=5)
        z_entry.grid(row=5,column=1, padx=5, pady=5)
        z_unit.grid(row=5,column=2, padx=5, pady=5)

        ωx_velo = Label(J_sw,text=("ωx = "),font=(5), bg='#1C43A6', fg='white') 
        ωx_entry = Entry(J_sw,width=10,font=(10), state='readonly')
        ωx_unit = Label(J_sw,text=("rad/s"),font=(5), bg='#1C43A6', fg='white')
        ωx_velo.grid(row=6,column=0, padx=5, pady=5)
        ωx_entry.grid(row=6,column=1, padx=5, pady=5)
        ωx_unit.grid(row=6,column=2, padx=5, pady=5)

        ωy_velo = Label(J_sw,text=("ωy = "),font=(5),  bg='#1D6DB8', fg='white') 
        ωy_entry = Entry(J_sw,width=10,font=(10), state='readonly')
        ωy_unit = Label(J_sw,text=("rad/s"),font=(5),  bg='#1D6DB8', fg='white')
        ωy_velo.grid(row=7,column=0, padx=5, pady=5)
        ωy_entry.grid(row=7,column=1, padx=5, pady=5)
        ωy_unit.grid(row=7,column=2, padx=5, pady=5)

        ωz_velo = Label(J_sw,text=("ωz = "),font=(5), bg='#2E7FCA', fg='white') 
        ωz_entry = Entry(J_sw,width=10,font=(10), state='readonly')
        ωz_unit = Label(J_sw,text=("rad/s"),font=(5), bg='#2E7FCA', fg='white')
        ωz_velo.grid(row=8,column=0, padx=5, pady=5)
        ωz_entry.grid(row=8,column=1, padx=5, pady=5)
        ωz_unit.grid(row=8,column=2, padx=5, pady=5)

        # Update Button
        update_but = Button(J_sw,text="Update",bg="green",fg="white",command=update_velo)
        update_but.grid(row=16,column=0, padx=5, pady=5)

    except ValueError:
        # Handle error if invalid input is provided
        messagebox.showerror("Error", "Please enter valid numbers for all input fields.")

#Create links
#[robot_value]=DHRobot([RevoluteDH(d,r,alpha,offset)])

    Articulated_Calculator=DHRobot([
        RevoluteDH(a1,0,(90.0/180.0)*np.pi,(0.0/180.0)*np.pi,qlim=[-np.pi/2,np.pi/2]),
        RevoluteDH(0,a2,(0.0/180.0)*np.pi,(0.0/180.0)*np.pi,qlim=[-np.pi/2,np.pi/2]),
        RevoluteDH(0,a3,(0.0/180.0)*np.pi,(0.0/180.0)*np.pi,qlim=[-np.pi/2,np.pi/2])],name='Articulated')


    #Path and Trajectory Planning
    #q paths
    #Articulated Joint Variables (T1,T2,T3)

    #Path planning remove the thetas and put your own path you want the joint variables to move to
    q0 = np.array([0,0,0]) # originS

    q1 = np.array([T1,T2,T3])

    #Trajectory Commands
    traj1 = rtb.jtraj (q0,q1,10)
    traj2 = rtb.jtraj (q1,q0,10)

    #Plot Scale di sure kung susunod kaya may ganito
    x1 = -2
    x2 = 2
    y1 = -2
    y2 = 2
    z1 = -2
    z2 = 2

    #Plot command
    Articulated_Calculator.plot(traj1.q,limits=[x1,x2,y1,y2,z1,z2])
    Articulated_Calculator.plot(traj2.q,limits=[x1,x2,y1,y2,z1,z2],block=True)



def calculate_inverse():
    try:
        # Get values from entry fields
        a1 = float(a1_entry_inv.get())
        a2 = float(a2_entry_inv.get())
        a3 = float(a3_entry_inv.get())
        x0_3 = float(X_entry.get())
        y0_3 = float(Y_entry.get())
        z0_3 = float(Z_entry.get())

        # Perform inverse kinematics calculations
        if x0_3 == 0:
            theta1 = np.pi / 2 if y0_3 > 0 else -np.pi / 2
        else:
            theta1 = np.arctan(y0_3 / x0_3)  # Sol1

        r1 = np.sqrt(y0_3**2 + x0_3**2)  # Sol2
        r2 = z0_3 - a1  # Sol3

        if r1 == 0:
            phi1 = np.pi / 2 if r2 > 0 else - np.pi / 2
        else:
            phi1 = np.arctan(r2 / r1)  # Sol4

        r3 = np.sqrt(r2**2 + r1**2)  # Sol5

        phi2 = np.arccos(np.clip((a3**2 - a2**2 - r3**2) / (-2 * a2 * r3), -1, 1))  # Sol6

        theta2 = phi1 + phi2# Sol7

        phi3 = np.arccos(np.clip((r3**2 - a2**2 - a3**2) / (-2 * a2 * a3), -1, 1))  # Sol8

        theta3 = phi3 - np.pi# Sol9

        # Convert angles from radians to degrees
        theta1_deg = (np.around(theta1*180/np.pi,3))
        theta2_deg = (np.around(theta2*180/np.pi,3))
        theta3_deg = (np.around(theta3*180/np.pi,3))

        # Display the results in the output fields
        T1_output.config(state='normal')
        T1_output.delete(0, END)
        T1_output.insert(0, str(theta1_deg))
        T1_output.config(state='readonly')

        T2_output.config(state='normal')
        T2_output.delete(0, END)
        T2_output.insert(0, str(theta2_deg))
        T2_output.config(state='readonly')

        T3_output.config(state='normal')
        T3_output.delete(0, END)
        T3_output.insert(0, str(theta3_deg))
        T3_output.config(state='readonly')

    except ValueError:
        # Handle error if invalid input is provided
        messagebox.showerror("Error", "Please enter valid numbers for all input fields.")

#Create links
#[robot_value]=DHRobot([RevoluteDH(d,r,alpha,offset)])
        
    Articulated_Calculator=DHRobot([
        RevoluteDH(a1/100,0,(90.0/180.0)*np.pi,(0.0/180.0)*np.pi,qlim=[-np.pi/2,np.pi/2]),
        RevoluteDH(0,a2/100,(0.0/180.0)*np.pi,(0.0/180.0)*np.pi,qlim=[-np.pi/2,np.pi/2]),
        RevoluteDH(0,a3/100,(0.0/180.0)*np.pi,(0.0/180.0)*np.pi,qlim=[-np.pi/2,np.pi/2])],name='Articulated')

   #Path planning remove the thetas and put your own path you want the joint variables to move to
    q0 = np.array([0,0,0]) # originS
    q1 = np.array([theta1,theta2,theta3])

    #Trajectory Commands
    traj1 = rtb.jtraj (q0,q1,10)
    traj2 = rtb.jtraj (q1,q0,10)

    #Plot Scale di sure kung susunod kaya may ganito
    x1 = -2
    x2 = 2
    y1 = -2
    y2 = 2
    z1 = -2
    z2 = 2

    #Plot command
    Articulated_Calculator.plot(traj1.q,limits=[x1,x2,y1,y2,z1,z2])
    Articulated_Calculator.plot(traj2.q,limits=[x1,x2,y1,y2,z1,z2],block=True)


def reset_field1():
    # Clear all entry fields and output fields
    a1_entry.delete(0, END)
    a2_entry.delete(0, END)
    a3_entry.delete(0, END)
    T1_entry.delete(0, END)
    T2_entry.delete(0, END)
    T3_entry.delete(0, END)
    X_output.config(state='normal')
    X_output.delete(0, END)
    X_output.config(state='readonly')
    Y_output.config(state='normal')
    Y_output.delete(0, END)
    Y_output.config(state='readonly')
    Z_output.config(state='normal')
    Z_output.delete(0, END)
    Z_output.config(state='readonly')

def reset_field2():
    a1_entry_inv.delete(0, END)
    a2_entry_inv.delete(0, END)
    a3_entry_inv.delete(0, END)
    X_entry.delete(0, END)
    Y_entry.delete(0, END)
    Z_entry.delete(0, END)
    T1_output.config(state='normal')
    T1_output.delete(0, END)
    T1_output.config(state='readonly')
    T2_output.config(state='normal')
    T2_output.delete(0, END)
    T2_output.config(state='readonly')
    T3_output.config(state='normal')
    T3_output.delete(0, END)
    T3_output.config(state='readonly')

# Create buttons for Forward and Inverse Kinematics
forward_btn = Button(root, text="Forward Kinematics", bg='#0A9396', command=Forward_Kinematics)
forward_btn.grid(row=0, column=0, padx=5, pady=5)

inverse_btn = Button(root, text="Inverse Kinematics", bg='#9B2226',command=Inverse_Kinematics)
inverse_btn.grid(row=0, column=4, padx=5, pady=5)


# Run the main event loop
root.mainloop()
