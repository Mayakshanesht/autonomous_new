#!/usr/bin/env python3
#import all the library
import rospy
from std_msgs.msg import String
class publisher:
    def __init__(self):
        self.rossetup()
        self.action_loop()
        self.loop()
    def rossetup(self):
        rospy.init_node('publisher',anonymous=True)
        self.pub=rospy.Publisher('/chatter', String,queue_size=10)
        self.rate=rospy.Rate(10)
    def action_loop(self):
        """
        basic implementation of your algorithm would go inside this function

        """
    def loop(self):
        while not rospy.is_shutdown():
            data="hello ros%s" %rospy.get_time()
            rospy.loginfo(data)
            self.pub.publish(data)
            self.rate.sleep()
if __name__=='__main__':
    try:
        node1=publisher()
        node1.rossetup()
        node1.loop()
    except rospy.ROSInterruptException:
        pass

        

        
