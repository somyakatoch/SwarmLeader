cmake_minimum_required(VERSION 3.5)
project(leader_follower_swarm)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)

install(DIRECTORY scripts DESTINATION lib/${Swarm Robots})

ament_package()
