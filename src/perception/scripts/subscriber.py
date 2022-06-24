#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
class subscriber:
    def __init__(self):
        self.rossetup()      
        
    def rossetup(self):
        rospy.init_node('subscriber',anonymous=True)
        rospy.Subscriber('/chatter',String,self.callback,queue_size=10)
        
    def callback(self,data):
        rospy.loginfo("publish data%s", data)
        
if __name__=='__main__':
    subscriber()
    rospy.spin()