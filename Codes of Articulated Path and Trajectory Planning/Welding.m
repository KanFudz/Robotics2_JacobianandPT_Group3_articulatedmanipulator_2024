% Link lengths
a1 = 3.5; % Link 1 length (m)
a2 = 2.5; % Link 2 length (m)
a3 = 1.5; % Link 3 length (m)

% DH parameters for the robot
dh_params = [
    0, 0, a1, pi/2;
    0, a2, 0, 0;
    0, a3, 0, 0
];

% Define the robot using DH parameters
robot = SerialLink([Revolute('d', dh_params(1, 1), 'a', dh_params(1, 2), 'alpha', dh_params(1, 4)), ...
                    Revolute('d', dh_params(2, 1), 'a', dh_params(2, 2), 'alpha', dh_params(2, 4)), ...
                    Revolute('d', dh_params(3, 1), 'a', dh_params(3, 2), 'alpha', dh_params(3, 4))], ...
                    'name', 'Welding');

% Define welding sequence for spot welding
q0 = [0, 0, 0]; % Home position
q_spot1 = [pi / 8, -pi / 6, pi / 4]; % First spot position

% Define waypoints for the full weld path (modify these as needed for your weld seam)
full_weld_path = [q_spot1;
                  [pi / 8, -pi / 4, pi / 3];
                  [pi / 8, -pi / 3, pi / 2];
                  [pi / 8, -pi / 4, 5 * pi / 12]];  % Adjusted fourth spot

% Define pause duration between spot welds (in seconds)
pause_duration = 1;

% Generate trajectory for spot welding positions
traj_spot1 = jtraj(q0, q_spot1, linspace(0, 1, 50));

% Generate full weld path trajectory (using loop for each waypoint)
full_weld_traj = [];
for i = 1:size(full_weld_path, 1) - 1
    start_point = full_weld_path(i, :);
    end_point = full_weld_path(i + 1, :);
    traj_segment = jtraj(start_point, end_point, linspace(0, 1, 200));  % Adjusting time vector for slower speed
    full_weld_traj = [full_weld_traj; traj_segment];
end

% Generate trajectories with pauses between spot welds
spot_trajectories = [];
for i = 2:size(full_weld_path, 1)
    spot_traj = jtraj(full_weld_path(i - 1, :), full_weld_path(i, :), linspace(0, 1, 50));
    spot_trajectories = [spot_trajectories; spot_traj];
end

% Generate slow trace back trajectory (adjust time vector for slower speed)
trace_back_time = linspace(0, 1, 200);  % Increased time points for slower motion
traj_trace_back = jtraj(full_weld_path(end, :), q0, trace_back_time);

% Generate trajectory from spot weld position 4 to position 1
spot4_to_spot1_traj = jtraj(full_weld_path(end, :), full_weld_path(1, :), linspace(0, 1, 50));

% Concatenate all trajectories
all_trajectories = [traj_spot1; spot_trajectories; spot4_to_spot1_traj; full_weld_traj; traj_trace_back];

% Concatenate all joint configurations into a single array
all_q = all_trajectories;

% Define plot limits (adjust these values as needed)
plot_limits = [-3.5, 3.5, -4, 4, -4, 4];

% Plot the combined trajectory with specified limits
robot.plot(all_q, 'trail', 'r-', 'jointdiam', 1, 'nowrist', 'nobase', 'noshadow', 'workspace', plot_limits);
