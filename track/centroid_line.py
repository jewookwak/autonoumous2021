#!/usr/bin/env python
import numpy
import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseArray
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray



def callback(pose_array):
    pub_msgs = Twist()
    
    marker_ests = MarkerArray()
    marker_ests.markers = []
    
    center_x = 0.0
    centroid_x = 0.0
    center_y = 0.0
    centroid_y = 0.0
    center_z = 0.0
    centroid_z = 0.0
    
    marker_est = Marker()
    marker_est.header.frame_id = "/velodyne"
    marker_est.ns = "marker"
    #marker_est.id = 42+i
    marker_est.type = Marker.CUBE
    marker_est.action = Marker.ADD

    while(1):
        if (len(pose_array.poses)==4):
            
            center_x = center_x + pose_array.poses[0].position.x + pose_array.poses[1].position.x + pose_array.poses[2].position.x + pose_array.poses[3].position.x
            center_y = center_y + pose_array.poses[0].position.y + pose_array.poses[1].position.y + pose_array.poses[2].position.y + pose_array.poses[3].position.y

            centroid_x = center_x / len(pose_array.poses)
            centroid_y = center_y / len(pose_array.poses)

            pub_msgs.linear.x = centroid_x
            pub_msgs.linear.y = centroid_y
            pub_msgs.linear.z = centroid_z

            marker_est.pose.position.x = pub_msgs.linear.x
            marker_est.pose.position.y = pub_msgs.linear.y
            marker_est.pose.position.z = pub_msgs.linear.z
            marker_est.pose.orientation.w = 1
            marker_est.color.r, marker_est.color.g, marker_est.color.b = (0, 255, 0)
            marker_est.color.a = 0.5
            marker_est.scale.x, marker_est.scale.y, marker_est.scale.z = (0.06, 0.06, 0.06)

            marker_ests.markers.append(marker_est)

            return center_line.publish(pub_msgs) , center_markers.publish(marker_ests)

        elif (len(pose_array.poses)==3) :
            
            center_x = center_x + pose_array.poses[0].position.x + pose_array.poses[1].position.x + pose_array.poses[2].position.x
            center_y = center_y + pose_array.poses[0].position.y + pose_array.poses[1].position.y + pose_array.poses[2].position.y

            centroid_x = center_x / len(pose_array.poses)
            centroid_y = center_y / len(pose_array.poses)

            pub_msgs.linear.x = centroid_x
            pub_msgs.linear.y = centroid_y
            pub_msgs.linear.z = centroid_z

            marker_est.pose.position.x = pub_msgs.linear.x
            marker_est.pose.position.y = pub_msgs.linear.y
            marker_est.pose.position.z = pub_msgs.linear.z
            marker_est.pose.orientation.w = 1
            marker_est.color.r, marker_est.color.g, marker_est.color.b = (0, 255, 0)
            marker_est.color.a = 0.5
            marker_est.scale.x, marker_est.scale.y, marker_est.scale.z = (0.06, 0.06, 0.06)

            marker_ests.markers.append(marker_est)

            return center_line.publish(pub_msgs) , center_markers.publish(marker_ests)
        elif (len(pose_array.poses)==2):
            
            center_x = center_x + pose_array.poses[0].position.x + pose_array.poses[1].position.x
            center_y = center_y + pose_array.poses[0].position.y + pose_array.poses[1].position.y

            centroid_x = center_x / len(pose_array.poses)
            centroid_y = center_y / len(pose_array.poses)

            pub_msgs.linear.x = centroid_x
            pub_msgs.linear.y = centroid_y
            pub_msgs.linear.z = centroid_z

            marker_est.pose.position.x = pub_msgs.linear.x
            marker_est.pose.position.y = pub_msgs.linear.y
            marker_est.pose.position.z = pub_msgs.linear.z
            marker_est.pose.orientation.w = 1
            marker_est.color.r, marker_est.color.g, marker_est.color.b = (0, 255, 0)
            marker_est.color.a = 0.5
            marker_est.scale.x, marker_est.scale.y, marker_est.scale.z = (0.06, 0.06, 0.06)

            marker_ests.markers.append(marker_est)

            return center_line.publish(pub_msgs) , center_markers.publish(marker_ests)

        else :

            pub_msgs.linear.x = centroid_x + 1.5
            pub_msgs.linear.y = centroid_y 
            pub_msgs.linear.z = centroid_z

            marker_est.pose.position.x = pub_msgs.linear.x
            marker_est.pose.position.y = pub_msgs.linear.y
            marker_est.pose.position.z = pub_msgs.linear.z
            marker_est.pose.orientation.w = 1
            marker_est.color.r, marker_est.color.g, marker_est.color.b = (0, 255, 0)
            marker_est.color.a = 0.5
            marker_est.scale.x, marker_est.scale.y, marker_est.scale.z = (0.06, 0.06, 0.06)

            marker_ests.markers.append(marker_est)

            return center_line.publish(pub_msgs) , center_markers.publish(marker_ests)

    print('end')
    


    
        
if __name__=='__main__':
    # Init ROS
    rospy.init_node('centroid_line', anonymous=True)
    # Subscribers
    
    rospy.Subscriber('/adaptive_clustering/poses', PoseArray, callback)
    
    # Publishers
    center_line = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    center_markers = rospy.Publisher('/center_point', MarkerArray, queue_size=1)
    # Spin
    rospy.spin()
   