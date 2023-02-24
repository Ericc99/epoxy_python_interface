#include <ros.h>
#include <std_msgs/String.h>
#include <rosserial_arduino/Test.h>
#include <iostream>

ros::NodeHandle nh;

void messageCb( const std_msgs::String &msg)
{
  std::string opt(msg.data); // Extracting data from this std_msgs::String type thing
  if(opt.compare("H") == 0)
  {
    digitalWrite(1, HIGH);
  }
  else
  {
    digitalWrite(1, LOW);
  }
  // digitalWrite(1, HIGH-digitalRead(1));   // blink the led
}

ros::Subscriber<std_msgs::String> sub("toggle", &messageCb );

void setup()
{
  pinMode(1, OUTPUT);
  nh.initNode();
  nh.subscribe(sub);
}

void loop()
{
  nh.spinOnce();
  delay(1);
} 
