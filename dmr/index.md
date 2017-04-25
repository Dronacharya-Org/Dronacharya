--- 
layout: template1 
---

<!-- Main component for a primary marketing message or call to action -->
<div class="jumbotron">
    <h2><u>Framework Demo</u></h2>
	<p> 
	In this video, we provide an overview of how the framework can be used for interacting with <a href="https://github.com/PX4/Firmware">PX4</a> firmware.
	We show how the programming language <a href="https://github.com/p-org/P">P</a> can be used to program a simple drone software stack and drive a drone in <a href = "https://pixhawk.org/dev/hil/jmavsim">jMavSim</a> simulator.
	The generated trace during simulation is visualized live in a state-machine visualization tool DGML.
	<br>
	For more details about the source code executed on the PX4 firmware please visit <a href="https://github.com/Drona-Org/Drona/wiki/Drona-Software-Stack">https://github.com/Drona-Org/Drona/wiki/Drona-Software-Stack</a>
	<br>
	</p>
	<iframe width="640" height="360" src="https://www.youtube.com/embed/ZzLoNbMGhg4" frameborder="4" allowfullscreen></iframe>
</div>

<div class="jumbotron">
    <h2><u>ROS Simulation Demos</u></h2>
    <p> 
    We present simulation videos for various configurations by varying the number of robots in the system and the grid size.
	The orange blocks in the workspace represent <font color="red">static obstacles</font> and green blocks represent
	potential goal locations for the robot. During simulation tasks represented as (taskId, goalLocation) are randomly generated and sent to the robot.
	Each robot on receiving a task request, dynamically computes the path using the multi-robot motion planner implemented in Drona.    
    The simulator uses 
	<a href="http://www.ros.org">ROS</a> 
    	and 
    	<a href="http://wiki.ros.org/rviz">Rviz</a>
    </p>
    <a class="btn btn-lg btn-info" href="https://github.com/Drona-Org/Drona/wiki/Running-ROS-simulation" role="button"> How to run these simulations? &raquo;</a>
<hr>
    <p>Demo of 8 Drones in a 16x16 grid (Watch in full screen mode) </p>
    <iframe width="640" height="360" src="https://www.youtube.com/embed/j8KnSNw-QM8" ></iframe><br/><br/>
<hr>
    <p>Demo of 32 Drones in a 32x32 grid (Watch in full screen mode) </p>
    <iframe width="640" height="360" src="https://www.youtube.com/embed/6v2eNu9JYhg" frameborder="0" allowfullscreen></iframe><br/><br/>
<hr>
    <p>Demo of 64 Drones in a 64x64 grid (Watch in full screen mode) </p>
    <iframe width="640" height="360" src="https://www.youtube.com/embed/BsTJUoMy7U0" frameborder="0" allowfullscreen></iframe><br/><br/>
<hr>
<hr>
    <h3><u>Demonstrate Effect of delta on path planning</u></h3>
    <p>
    In this simulation, there are two robots that are assigned a task to go to a particular green location. 
    The path on the left is shorter than the part on the right for both the robots.
    We conduct a series of experiments for different values of delta. (delta = 1, 2, 3).
    delta = 1 means that the drones must consider a time-step window of 1, delta = 2 means that the drones must keep a time-step window of 2.
    You could see that the drones keep sufficient distance among themselves and being conservative with respect to delta.
    <br>
    When delta = 3, the drone on right will have to wait/hower for a longer time which has an associated cost so it choose another path which turns out to be less costly.
    This demo demonstrate that our motion-planner considers time-synchronization error and in the presence of that computes the optimal path.
    </p>
    <iframe width="640" height="360" src="https://www.youtube.com/embed/ySn5uLh_ZLU" frameborder="0" allowfullscreen></iframe>
<hr>
<hr>
    <h3><u>Demonstrate that the motion planner can perform 3D planning (Watch in full screen mode)</u></h3>
    <p>Demo of 32 Drones in 32x32x4 grid</p>
    <iframe width="640" height="360" src="https://www.youtube.com/embed/dMV_vlcag9w?rel=0" frameborder="0" allowfullscreen></iframe> 
<hr>
<hr>
    <h3><u>Simple Drone Surveillance Mission on Astec Firefly</u></h3>
    <p>During this mission the drone is executing the generated code from drona framework. The task planner is continuously sending the next location in the grid to be surveyed and the drone visits that location and waits (may be takes an image :))
    When the mission-completed message is sent by the task-planner the drone dynamically computes path to the home location and returns.
    </p>
    <iframe width="640" height="360" src="https://www.youtube.com/embed/0c7lX6eB96Q" frameborder="0" allowfullscreen></iframe>
</div>

<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-58686046-1', 'auto');
  ga('send', 'pageview');

</script>