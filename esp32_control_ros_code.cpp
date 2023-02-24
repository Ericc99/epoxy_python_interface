#include <ros/ros.h>
#include <std_msgs/String.h>
#include <iostream>

int main(int argc, char *argv[])
{
    setlocale(LC_ALL,"");
    
    ros::init(argc,argv,"control");
    ros::NodeHandle nh;

    ros::Publisher pub = nh.advertise<std_msgs::String>("/toggle", 1000);

    std_msgs::String data;

    std::string input;

    ros::Rate r(10);
    
    while(ros::ok())
    {
        std::cout << "H for light up, G for light down, Q for quit:  " << std::endl;
        std::cin >> input;

        if(input == "Q")
        {
            break;
        }

        data.data = input;

        pub.publish(data);

        ros::spinOnce();
    }   

    return 0; 

}
