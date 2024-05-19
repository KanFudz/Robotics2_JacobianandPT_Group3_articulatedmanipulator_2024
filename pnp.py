from tkinter import *
import numpy as np
import roboticstoolbox as rtb
from roboticstoolbox import DHRobot, RevoluteDH
import matplotlib.pyplot as plt

# Create GUI Window with title
root = Tk()
root.title('Arti PnP')
root.resizable(False, False)
root.configure(bg='black')

# Create a frame to contain all the elements
frame = Frame(root, bg='black')
frame.grid(row=0, column=0, padx=20, pady=20)

# Predetermined link lengths
a1_value = StringVar(root, value="30")
a2_value = StringVar(root, value="20")
a3_value = StringVar(root, value="15")

# Display link lengths
# Create labels for link lengths with predetermined values
a1_label = Label(frame, text="a1:", padx=10, pady=10, bg='#012228', fg='white', font=('Arial', 14))
a1_label.grid(row=1, column=0, sticky=W)

a1_value_label = Label(frame, textvariable=a1_value, padx=10, pady=10, bg='#012228', fg='white', font=('Arial', 14))
a1_value_label.grid(row=1, column=1, sticky=W)

a1_unit = Label(frame, text="cm", padx=10, pady=10, bg='#012228', fg='white', font=('Arial', 14))
a1_unit.grid(row=1, column=2, sticky=W)

a2_label = Label(frame, text="a2:", padx=10, pady=10, bg='#032b28', fg='white', font=('Arial', 14))
a2_label.grid(row=2, column=0, sticky=W)

a2_value_label = Label(frame, textvariable=a2_value, padx=10, pady=10, bg='#032b28', fg='white', font=('Arial', 14))
a2_value_label.grid(row=2, column=1, sticky=W)

a2_unit = Label(frame, text="cm", padx=10, pady=10, bg='#032b28', fg='white', font=('Arial', 14))
a2_unit.grid(row=2, column=2, sticky=W)

a3_label = Label(frame, text="a3:", padx=10, pady=10, bg='#0d3f2e', fg='white', font=('Arial', 14))
a3_label.grid(row=3, column=0, sticky=W)

a3_value_label = Label(frame, textvariable=a3_value, padx=10, pady=10, bg='#0d3f2e', fg='white', font=('Arial', 14))
a3_value_label.grid(row=3, column=1, sticky=W)

a3_unit = Label(frame, text="cm", padx=10, pady=10, bg='#0d3f2e', fg='white', font=('Arial', 14))
a3_unit.grid(row=3, column=2, sticky=W)


def start_simulation():
    # Specific link lengths
    a1 = float(a1_value.get())
    a2 = float(a2_value.get())
    a3 = float(a3_value.get())

    # Create the robot using DH parameters
    Articulated_Calculator = DHRobot([
        RevoluteDH(a1, 0, (90.0 / 180.0) * np.pi, (0.0 / 180.0) * np.pi, qlim=[-np.pi / 2, np.pi / 2]),
        RevoluteDH(0, a2, (0.0 / 180.0) * np.pi, (0.0 / 180.0) * np.pi, qlim=[-np.pi / 2, np.pi / 2]),
        RevoluteDH(0, a3, (0.0 / 180.0) * np.pi, (0.0 / 180.0) * np.pi, qlim=[-np.pi / 2, np.pi / 2])
    ], name='Articulated')

    # Initial and target joint angles for pick and place
    q0 = np.array([0, 0, 0])  # Home position
    q_pick1 = np.array([np.pi / 4, -np.pi / 6, np.pi / 4])  # First pick position for door
    q_pick2 = np.array([np.pi / 4, -np.pi / 4, np.pi / 3])  # Second pick position for door
    q_pick3 = np.array([np.pi / 4, -np.pi / 3, np.pi / 3])  # Pick position for hood
    q_place = np.array([0, np.pi / 3, -np.pi / 3])  # Place position on car body

    # Trajectory planning with direct time vectors for each trajectory
    traj1 = rtb.jtraj(q0, q_pick1, np.linspace(0, 1, 100))  # From home to first pick (door)
    traj2 = rtb.jtraj(q_pick1, q_place, np.linspace(0, 1, 100))  # From first pick to place (door)
    traj3 = rtb.jtraj(q_place, q_pick2, np.linspace(0, 1, 100))  # From place to second pick (door)
    traj4 = rtb.jtraj(q_pick2, q_place, np.linspace(0, 1, 100))  # From second pick to place (door)
    traj5 = rtb.jtraj(q_place, q_pick3, np.linspace(0, 1, 100))  # From place to pick (hood)
    traj6 = rtb.jtraj(q_pick3, q_place, np.linspace(0, 1, 100))  # From pick to place (hood)
    traj7 = rtb.jtraj(q_place, q0, np.linspace(0, 1, 100))  # From place to home

    # Combined trajectory for looping
    trajectories = [traj1, traj2, traj3, traj4, traj5, traj6, traj7]

    # Concatenate all joint configurations into a single array
    all_q = np.concatenate([traj.q for traj in trajectories])

    # Define plot limits
    plot_limits = [-30, 30, -30, 30, -30, 30]  # Adjust these values as needed

    # Plot the combined trajectory with specified limits
    Articulated_Calculator.plot(all_q, block=True, limits=plot_limits)


# Create start button
start_button = Button(root, text="Start Pick n' Place", command=start_simulation, font=('Arial', 14))
start_button.grid(row=4, column=0, columnspan=3, pady=20)

# Run the
root.mainloop()
