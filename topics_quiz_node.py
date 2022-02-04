#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def callback(msg):
    front_laser_reading = msg.ranges[360]
    left_laser_reading = msg.ranges[719]
    right_laser_reading = msg.ranges[0]
    print(f"front_laser: {front_laser_reading}, left_laser: {left_laser_reading}, right_laser: {right_laser_reading}")

    if front_laser_reading > 1 or front_laser_reading == 'inf':
        move.linear.x = 0.2
        move.angular.z = 0

    if front_laser_reading < 1:
        move.angular.z = 0.2

        if right_laser_reading < 1:
            move.linear.x = 0




rospy.init_node("topics_quiz_pub")
rate = rospy.Rate(1)

pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)

move = Twist()
move.linear.x = 0.2
move.angular.z = 0


while not rospy.is_shutdown():
    sub = rospy.Subscriber("/kobuki/laser/scan", LaserScan, callback)
    pub.publish(move)
    rate.sleep()
