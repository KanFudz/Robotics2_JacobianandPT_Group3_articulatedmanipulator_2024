import numpy as np
import roboticstoolbox as rtb
from roboticstoolbox import DHRobot, RevoluteDH
from tkinter import *

# Create GUI Window with title
root = Tk()
root.title('Automobile Chassis Welding')
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
a1_label = Label(frame, text="a1:", padx=10, pady=10, bg='#540f0d', fg='white', font=('Arial', 14))
a1_label.grid(row=1, column=0, sticky=W)

a1_value_label = Label(frame, textvariable=a1_value, padx=10, pady=10, bg='#540f0d', fg='white', font=('Arial', 14))
a1_value_label.grid(row=1, column=1, sticky=W)

a1_unit = Label(frame, text="cm", padx=10, pady=10, bg='#540f0d', fg='white', font=('Arial', 14))
a1_unit.grid(row=1, column=2, sticky=W)

a2_label = Label(frame, text="a2:", padx=10, pady=10, bg='#6b0500', fg='white', font=('Arial', 14))
a2_label.grid(row=2, column=0, sticky=W)

a2_value_label = Label(frame, textvariable=a2_value, padx=10, pady=10, bg='#6b0500', fg='white', font=('Arial', 14))
a2_value_label.grid(row=2, column=1, sticky=W)

a2_unit = Label(frame, text="cm", padx=10, pady=10, bg='#6b0500', fg='white', font=('Arial', 14))
a2_unit.grid(row=2, column=2, sticky=W)

a3_label = Label(frame, text="a3:", padx=10, pady=10, bg='#87080a', fg='white', font=('Arial', 14))
a3_label.grid(row=3, column=0, sticky=W)

a3_value_label = Label(frame, textvariable=a3_value, padx=10, pady=10, bg='#87080a', fg='white', font=('Arial', 14))
a3_value_label.grid(row=3, column=1, sticky=W)

a3_unit = Label(frame, text="cm", padx=10, pady=10, bg='#87080a', fg='white', font=('Arial', 14))
a3_unit.grid(row=3, column=2, sticky=W)

def start_welding():
    # Specific link lengths
    a1 = float(a1_value.get())
    a2 = float(a2_value.get())
    a3 = float(a3_value.get())

    # Create the robot using DH parameters
    Welding_Robot = DHRobot([
        RevoluteDH(a1, 0, (90.0 / 180.0) * np.pi, (0.0 / 180.0) * np.pi, qlim=[-np.pi / 2, np.pi / 2]),
        RevoluteDH(0, a2, (0.0 / 180.0) * np.pi, (0.0 / 180.0) * np.pi, qlim=[-np.pi / 2, np.pi / 2]),
        RevoluteDH(0, a3, (0.0 / 180.0) * np.pi, (0.0 / 180.0) * np.pi, qlim=[-np.pi / 2, np.pi / 2])
    ], name='Welding')

    # Define welding sequence for spot welding
    q0 = np.array([0, 0, 0])  # Home position
    q_spot1 = np.array([np.pi / 8, -np.pi / 6, np.pi / 4])  # First spot position

    # Define waypoints for the full weld path (modify these as needed for your weld seam)
    full_weld_path = [q_spot1,
                      np.array([np.pi / 8, -np.pi / 4, np.pi / 3]),
                      np.array([np.pi / 8, -np.pi / 3, np.pi / 2]),
                      np.array([np.pi / 8, -np.pi / 4, 5 * np.pi / 12]),  # Adjusted fourth spot
                      ]

    # Define pause duration between spot welds (in seconds)
    pause_duration = 1

    # Generate trajectory for spot welding positions
    traj_spot1 = rtb.jtraj(q0, q_spot1,    np.linspace(0, 1, 50))

    # Generate full weld path trajectory (using loop for each waypoint)
    full_weld_traj = []
    for i in range(len(full_weld_path) - 1):
        start_point = full_weld_path[i]
        end_point = full_weld_path[i + 1]
        traj_segment = rtb.jtraj(start_point, end_point, np.linspace(0, 1, 200))  # Adjusting time vector for slower speed
        full_weld_traj.append(traj_segment)

    # Generate trajectories with pauses between spot welds
    spot_trajectories = []
    for i in range(1, len(full_weld_path)):
        spot_traj = rtb.jtraj(full_weld_path[i - 1], full_weld_path[i], np.linspace(0, 1, 50))
        spot_trajectories.append(spot_traj)

    # Generate slow trace back trajectory (adjust time vector for slower speed)
    trace_back_time = np.linspace(0, 1, 200)  # Increased time points for slower motion
    traj_trace_back = rtb.jtraj(full_weld_path[-1], q0, trace_back_time)

    # Generate trajectory from spot weld position 4 to position 1
    spot4_to_spot1_traj = rtb.jtraj(full_weld_path[-1], full_weld_path[0], np.linspace(0, 1, 50))

    # Concatenate all trajectories
    all_trajectories = [traj_spot1] + spot_trajectories + [spot4_to_spot1_traj] + full_weld_traj + [traj_trace_back]

    # Concatenate all joint configurations into a single array
    all_q = np.concatenate([traj.q for traj in all_trajectories])

    # Define plot limits (adjust these values as needed)
    plot_limits = [-50, 50, -50, 50, -50, 50]

    # Plot the combined trajectory with specified limits
    Welding_Robot.plot(all_q, block=True, limits=plot_limits)

# Create a button to initiate welding
start_weld_button = Button(frame, text="Start Welding", padx=20, pady=10, command=start_welding, bg='#d3322a', fg='white', font=('Arial', 14))
start_weld_button.grid(row=4, columnspan=3, pady=20)

# Run the main loop
root.mainloop()
