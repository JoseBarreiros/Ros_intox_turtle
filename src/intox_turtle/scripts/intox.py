#!/usr/bin/env python
# created by Jose Barreiros / Human Robot Interaction - Cornell University. 2017
# Under license MIT.
#Python 2.7.12
from __future__ import division
import rospy
import random
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from std_msgs.msg import String


def talker():
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('intox_a_turtle', anonymous=True)
    rate = rospy.Rate(5) # 10hz
    shift=1
    t=random.randint(0,100)
    c=0
    while not rospy.is_shutdown():
        lx=1*random.uniform(0,1.3)    #randomly generate Linear X
#	lx=random.uniform(-1,1)
#	ly=shift*lx
#	lz=-1*shift*ly
#	lx=-1
	ly=0
	lz=0
	ax=0
	ay=0
#	az=2	
      	az=shift*random.random() #randomly generate Angular Z.  Shift change the direction of the motion every t(randomly generated) iterations
#	ax=random.uniform(-1,1)
#	ay=-1*shift*ax
#	az=shift*ay
#        t=random.random()
        print t
        c=c+1
        if(c>t):   #if c count> random generated number then shift direction of motion
		shift=shift*-1
                c=0
                t=random.randint(0,100)
#	else:
#		shift=1
  		
        pub.publish(Twist(Vector3(lx,ly,lz),Vector3(ax,ay,az)))  #publish in Msgs Twist format
        #hello_str = "hello world %s" % rospy.get_time()
        #rospy.loginfo(hello_str)
        #pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
