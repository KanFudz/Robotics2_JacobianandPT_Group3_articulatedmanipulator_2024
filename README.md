# Robotics2_JacobianandPT_Group3_articulatedmanipulator_2024
<div align="center">
 
# **JACOBIAN MATRIX AND PATH & TRAJECTORY PLANNING**
    
</div>
     
## Project Course Portfolio</h2>
    
[I. Abstract of the Project](#abstract)
<br>
[II. Introduction of the Project](#introduction)
<br>
[III. Jacobian Matrix of Articulated Manipulator](#jacobianmatrix)
<br>
[IV. Differential Equation of Articulated Manipulator](#differentialequation)
<br>
[V. Path and Trajectory Planning of Articulated Manipulator](#pathandtrajectory)
<br>							
[VI. References](#references)
<br>
[VII. Group Members](#group-members)
<br>
    
<div align="justify">
    
## I. Abstract of the Project<a name="abstract"></a>
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This project explores the utilization of the Jacobian matrix for path and trajectory planning of articulated manipulators. The Jacobian matrix, pivotal in robotic kinematics, facilitates the translation of joint space movements to Cartesian space motions, thereby linking joint velocities to end-effector velocities. Our research focuses on harnessing this mathematical tool to enhance the precision and efficiency of motion planning for articulated robotic arms.
<br>
    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We employ the Jacobian matrix in both forward and inverse kinematics to enable precise control over the manipulator's movements. This involves generating optimal paths and trajectories that navigate from an initial position to a target, while considering constraints such as joint limits, obstacles, and collision avoidance. Our approach integrates real-time adjustments to dynamic environmental changes, ensuring robustness and adaptability in various operational scenarios. 
<br>
    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Advanced computational algorithms are developed to solve the inverse kinematics problem, providing feasible joint configurations for desired end-effector positions. Furthermore, we incorporate trajectory optimization techniques to achieve smooth and energy-efficient motions, enhancing the manipulator's operational performance.
<br>
    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The project includes extensive simulations and experimental validations on multiple articulated manipulator models. Results demonstrate the effectiveness of our Jacobian-based methods in achieving accurate, efficient, and reliable path and trajectory planning.
<br>
    
    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Our findings have significant implications for the field of robotics, particularly in applications requiring high precision and adaptability, such as industrial automation, medical robotics, and autonomous systems. By advancing the capabilities of articulated manipulators, this research contributes to the development of more sophisticated and versatile robotic solutions.
<br>
    
</div>
    
## II. Introduction of the Project<a name="introduction">
<div align="justify">
 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
In the realm of advanced robotics, the articulated manipulator stands as a cornerstone for automation, precision, and versatility across diverse industrial applications. This project delves into two critical aspects that enhance the performance and functionality of articulated manipulators: the Jacobian matrix and path & trajectory planning.
<br>

<div align="justify">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The Jacobian matrix is a fundamental concept in the kinematic analysis of robotic manipulators. It encapsulates the relationship between joint velocities and end-effector velocities, providing a mathematical framework for understanding and controlling the motion of the manipulator. This project aims to develop a comprehensive understanding of the Jacobian matrix, exploring its derivation, properties, and applications in real-time control and optimization of robotic movements.
<br>
</div>  

<div align="justify">
 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Complementing the kinematic insights provided by the Jacobian matrix, effective path and trajectory planning is pivotal for ensuring that the manipulator performs tasks with precision and efficiency. Path planning focuses on determining a collision-free route from the start to the end position, while trajectory planning involves the timing and smooth execution of this path. This project will investigate various algorithms and techniques for both path and trajectory planning, emphasizing their integration with the Jacobian matrix to achieve seamless and adaptive manipulator control.  
<br>
</div>

<div align="justify">    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Through a systematic exploration of these elements, this project aspires to contribute to the development of more intelligent, responsive, and capable robotic systems. By enhancing our understanding and application of the Jacobian matrix and optimizing path and trajectory planning, we can push the boundaries of what articulated manipulators can achieve, paving the way for innovations in automation and robotics.
<br>
</div>

### Purpose and Use

<div align="justify">   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Purpose and Use of the Jacobian Matrix and Path & Trajectory Planning in Mechanical Manipulators
<br>
</div>

<div align="justify">  
 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The Jacobian matrix and path & trajectory planning are pivotal components in the design and control of mechanical manipulators, each serving distinct yet complementary roles that enhance the manipulator's functionality and efficiency.
<br>
</div>

<div align="justify">  

 **Jacobian Matrix**
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The Jacobian matrix is a critical tool in the kinematic and dynamic analysis of mechanical manipulators. Its primary purposes and uses include:
<br>
</div>

- **Velocity Mapping:**  The Jacobian matrix provides a direct relationship between the velocities of the manipulator's joints and the velocity of the end-effector. This mapping is essential for understanding how movements in joint space translate to movements in Cartesian space, enabling precise control over the end-effector's position and orientation.
    
- **Singularity Analysis:** By examining the Jacobian matrix, engineers can identify singular configurations where the manipulator loses certain degrees of freedom. This analysis is crucial for avoiding positions that could lead to control difficulties or mechanical failures.
    
- **Force Transmission:** The Jacobian matrix also relates joint torques to forces and moments at the end-effector. This relationship is used to ensure that the manipulator can apply the necessary forces to perform tasks such as gripping or manipulating objects.
    
- **Inverse Kinematics:** Inverse kinematic solutions often rely on the Jacobian matrix to iteratively compute the required joint angles to achieve a desired end-effector position, particularly in redundant or complex manipulator systems.
    
**Path and Trajectory Planning**

<div align="justify">
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Path and trajectory planning are essential for ensuring that a mechanical manipulator moves efficiently and accurately within its operational environment. The purposes and uses of these processes include:
<br>
    
 - **Collision Avoidance:** Path planning algorithms are employed to determine a collision-free route for the manipulator from a start position to an end position. This is critical for operating in environments with obstacles or in multi-robot systems where coordination is required.
    
 - **Optimized Movement:** Trajectory planning focuses on the timing and execution of the planned path. It ensures that the manipulator moves smoothly and efficiently, optimizing parameters such as speed, acceleration, and jerk to minimize wear and energy consumption.
    
 - **Task Precision:** Accurate trajectory planning ensures that the manipulator performs tasks with high precision, following the desired path closely. This is particularly important in applications requiring fine manipulation or high accuracy, such as assembly or surgical robotics.
    
 - **Real-Time Adaptability:** Advanced path and trajectory planning algorithms allow for real-time adjustments to the manipulator's movements. This adaptability is essential in dynamic environments where conditions may change rapidly, requiring the manipulator to react promptly to maintain performance and safety.
    
<div align="justify">
     
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; In summary, the Jacobian matrix and path & trajectory planning are indispensable for the effective operation of mechanical manipulators. The Jacobian matrix facilitates precise control and analysis of the manipulator's kinematics and dynamics, while path and trajectory planning ensure that movements are efficient, accurate, and adaptable. Together, these components enable the development of sophisticated robotic systems capable of performing complex tasks in a variety of settings.
<br>
</div>
    

## III. Jacobian Matrix of Articulated Manipulator<a name="jacobianmatrix"> </a>

<div align="justify">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; In general, Jacobian Matrix is a matrix that relates the end-effector velocities to joint velocities. It is also the partial derivatives of the Forward Kinematics equation.
</div>

- **Constant Velocity** Displacement over time (t)
- **Average Velocity** Change in displacement over change in time (t).
- **Instantaneous Velocity** The rate of change in displacement with respect to time (t).
<br>
<div align="center">
 
![JACOBIAN MATRIX ARTICULATED](https://github.com/KanFudz/Robotics2_JacobianandPT_Group3_articulatedmanipulator_2024/assets/157782959/0a0eda2d-cc06-467b-8adb-a0d2916840a0)

</div>

<div align="center">
 
### **Jacobian Matrix of Articulated Manipulator**


[![Screenshot 2024-05-21 124026](https://github.com/KanFudz/Robotics2_JacobianandPT_Group3_articulatedmanipulator_2024/assets/157782959/1bb3548b-697f-47d6-8107-e806cc369d4b)](https://youtu.be/-NZXbrpljoQ?si=uKV7DF5lNiU6A5j9)



_Click on the image above to watch the video._
</div>

<br>


 
    
## IV. Differential Equation of Articulated Manipulator<a name="differentialequation"></a>

<div align="justify">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The dynamic behavior of an articulated manipulator can be described by a set of differential equations derived from the principles of rigid body dynamics and control theory. These equations are essential for understanding and controlling the motion of the manipulator's joints and end-effector. 
<br>
</div>
<div align="center">
 
![DE ARTICULATED](https://github.com/KanFudz/Robotics2_JacobianandPT_Group3_articulatedmanipulator_2024/assets/157782959/6454d0c4-2d5a-4d31-aef8-674e9d5f0f21)
 
</div>

<div align="center">
 
### **Differential Equation of Articulated Manipulator**

**PLACEHOLDER LANG**

[![Step-by-step process of solving the Degrees of Freedom of Articulated manipulator](https://img.youtube.com/vi/g7lCQ4IBkvA/0.jpg)](https://www.youtube.com/watch?v=g7lCQ4IBkvA)

_Click on the image above to watch the video._
</div>

<br>

<div align="center">
 
### **Singularity of Articulated Manipulator**


[![Screenshot 2024-05-21 123947](https://github.com/KanFudz/Robotics2_JacobianandPT_Group3_articulatedmanipulator_2024/assets/157782959/ee12fc9f-2117-4583-be2a-63f5160fd9a6)](https://youtu.be/Jv6aY7FHy8w?si=CZwPOIfWFVowmg2i)

_Click on the image above to watch the video._
</div>

<br>
    
## V. Path and Trajerctory Planning of Articulated Manipulator<a name="pathandtrajectory"></a>

<div align="justify">
 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Path and trajectory planning are crucial processes in the control and operation of articulated manipulators, ensuring that the robot moves from one point to another efficiently, accurately, and safely. These processes involve determining the sequence of movements (path) and the timing of these movements (trajectory) to achieve a desired task.
    
### Path Planning
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Path planning refers to the process of defining a collision-free route that the manipulator’s end-effector or joints must follow to move from a start position to a goal position. Key aspects of path planning include:
    
- **Collision Avoidance:** Ensuring the manipulator does not collide with obstacles in its environment, including itself and other robots.
- **Optimality:** Finding the shortest, most efficient, or least energy-consuming path, depending on the criteria set by the specific application.
- **Feasibility:** Ensuring that the planned path is within the manipulator's kinematic and dynamic capabilities, considering factors such as joint limits and workspace constraints.
  
    Redundancy Resolution: For manipulators with more degrees of freedom than necessary to complete a task (redundant manipulators), path planning also involves choosing among the infinite possible configurations.
    
### Trajectory Planning
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Trajectory planning takes the path generated by path planning and determines how the manipulator should move along this path over time. This involves specifying the position, velocity, and acceleration of each joint at each time step. Key aspects of trajectory planning include:
  
- **Time Parameterization:** Assigning time stamps to each point on the path to ensure smooth and continuous motion.
- **Kinematic Constraints:** Respecting the maximum velocities and accelerations of the manipulator's joints to avoid excessive wear and ensure safety.
- **Dynamic Constraints:** Ensuring that the planned trajectories are within the force and torque capabilities of the manipulator.
- **Smoothness:** Ensuring that the trajectory is smooth to avoid jerky movements, which can lead to mechanical stress and reduced precision.
    
### Integration and Implementation

<div align="justify">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The integration of path and trajectory planning ensures that the manipulator can perform complex tasks in dynamic environments. The implementation typically involves the following steps:
 
</div>
<br>

- **Environment Mapping:** Creating a detailed map of the manipulator’s environment, including all obstacles and constraints.
  
- **Path Generation:** Using a suitable path planning algorithm to generate a collision-free path.
  
- **Trajectory Generation:** Applying trajectory planning techniques to time-parameterize the path.
  
- **Real-time Adaptation:** Incorporating sensors and feedback mechanisms to adjust the path and trajectory in real time in response to changes in the environment or task requirements.
    
<div align="justify">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Path and trajectory planning are fundamental to the effective operation of articulated manipulators, ensuring that movements are both efficient and precise. Path planning focuses on determining a feasible and optimal route, while trajectory planning ensures that the manipulator moves along this path smoothly and within its operational limits. Together, these processes enable the manipulator to perform a wide range of tasks, from simple pick-and-place operations to complex assembly and interaction in dynamic environments.
</div>

    
<br>

<div align="center">
 
### **Path and Trajectory of Articulated Manipulator in Python and MATLAB**


[![PNP](https://github.com/KanFudz/Robotics2_JacobianandPT_Group3_articulatedmanipulator_2024/assets/157782959/c40af7c4-5437-430e-9a40-6b00d930567c)] (dito sa loob ng parenthesis yung link ng yt vid.)

_Click on the image above to watch the video._
</div>

<br>

<div align="center">
 
### **Path and Trajectory of Articulated Manipulator GUI calculator**


[![GUI](https://github.com/KanFudz/Robotics2_JacobianandPT_Group3_articulatedmanipulator_2024/assets/157782959/39c3a417-8a9b-4440-a741-0dbd7f45ac65)](dito sa loob ng parenthesis yung link ng yt vid.)

_Click on the image above to watch the video._
</div>

<br>
     
    
## VI. References<a name="references"></a>
https://www.youtube.com/watch?v=4xIkUo0M1R8&list=PLUgsbeZHs9qMFXTIQPW0clLoRkf_oiBoX&index=14 

https://www.youtube.com/watch?v=gR08ESR9gUg&list=PLUgsbeZHs9qMFXTIQPW0clLoRkf_oiBoX&index=16

https://www.youtube.com/watch?v=fC9lMgB8l84&list=PLUgsbeZHs9qMFXTIQPW0clLoRkf_oiBoX&index=17&t=458s


## VII. Group Members<a name="group-members"></a>
    
1. Comia, Alexandria B. (21-07197)
2. Hernandez, Lelanie Lorraine C. (21-02123)
3. Malabanan, Angelo Louis D. (21-04184)
4. Malata, John Rei R. (21-08864)
5. Medrano, Russel I. (19-06602)

