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
                    'name', 'Articulated');

% Initial and target joint angles for pick and place
q0 = [0, 0, 0]; % Home position
q_pick1 = [pi/4, -pi/6, pi/4]; % First pick position for door
q_pick2 = [pi/4, -pi/4, pi/3]; % Second pick position for door
q_pick3 = [pi/4, -pi/3, pi/3]; % Pick position for hood
q_place = [0, pi/3, -pi/3]; % Place position on car body

% Plot the robot
robot.teach();

% Set movement duration (in seconds)
move_duration = 0.5; % Shorter duration for faster movement

% Define time vector for the trajectory (1 second with 100 steps)
t = linspace(0, move_duration, 100);

% Generate joint trajectories for all movements
q_pick1_traj = jtraj(q0, q_pick1, t);
q_pick2_traj = jtraj(q_place, q_pick2, t);
q_pick3_traj = jtraj(q_place, q_pick3, t);
q_place_traj = jtraj(q_pick1, q_place, t);

% Perform pick and place tasks automatically with faster movement
disp('Moving to pick position 1...');
for i = 1:size(q_pick1_traj, 1)
    robot.animate(q_pick1_traj(i, :));
    pause(move_duration / numel(q_pick1_traj)); % Adjust speed here
end

disp('Moving to placing position...');
for i = 1:size(q_place_traj, 1)
    robot.animate(q_place_traj(i, :));
    pause(move_duration / numel(q_place_traj)); % Adjust speed here
end

disp('Moving to pick position 2...');
for i = 1:size(q_pick2_traj, 1)
    robot.animate(q_pick2_traj(i, :));
    pause(move_duration / numel(q_pick2_traj)); % Adjust speed here
end

disp('Moving to placing position...');
for i = 1:size(q_place_traj, 1)
    robot.animate(q_place_traj(i, :));
    pause(move_duration / numel(q_place_traj)); % Adjust speed here
end

disp('Moving to pick position 3...');
for i = 1:size(q_pick3_traj, 1)
    robot.animate(q_pick3_traj(i, :));
    pause(move_duration / numel(q_pick3_traj)); % Adjust speed here
end

disp('Moving to placing position...');
for i = 1:size(q_place_traj, 1)
    robot.animate(q_place_traj(i, :));
    pause(move_duration / numel(q_place_traj)); % Adjust speed here
end

disp('Back to starting position.');
robot.animate(q0);
