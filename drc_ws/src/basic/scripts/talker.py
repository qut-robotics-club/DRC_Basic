#!/usr/bin/env python
import rospy
#from std_msgs.msg import String
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist



def image_callback(msg):
    movementMsg = Twist()
    movementMsg.linear.x = 0.1 
    movementMsg.angular.z = 0.5
    #movementMsg.angular.y = 0.5
    #movementMsg.angular.z = 0.5
    pub.publish(movementMsg)
  


if __name__ == '__main__':
    rospy.init_node('image_listener')
    rospy.Subscriber("/mybot/camera1/image_raw",Image,image_callback)
    
    pub = rospy.Publisher("/cmd_vel",Twist,queue_size=1);
    
    rospy.spin()
