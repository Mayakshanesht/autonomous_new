# autonomous_new
#Step 1 clone it on your system
git clone https://github.com/Mayakshanesht/autonomous_new.git
#step 2 then source it
source devel/setup.bash
#step 3 then run the master node
roscore
#step 4 open new terminal, go to to autonomous/src and source it 
source devel/setup.bash
#step 5 navigate to script directory
cd src/perception/scripts/
# step 6 run the publisher node
rosrun perception publisher.py
# repeat steps 4 and 5
rosrun perception subscriber.py
