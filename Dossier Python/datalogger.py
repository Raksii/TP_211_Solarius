#!/usr/bin/python3
#  -*- coding: utf-8 -*-

# Date: Mon 14 may 2021 17:46:52 CEST
# Author: Hugo Lux
# Last updated by: Hugo Lux
# Last updated date: Wen 16 may 2021 15:38:42 CEST
# Description: datalogger

#include <Servo.h>

Servo servo.rotate;
Servo servo.incline; 

int pos.rorate;
int pos.incline;

void setup() {
  servo.rotate.attach();
  servo.incline.attach();
  pinMode(A0,INPUT_PULLUP); // capteur 1
  pinMode(A1,INPUT_PULLUP); // capteur 2
  pinMode(A2,INPUT_PULLUP); // capteur 3
  pinMode(A3,INPUT_PULLUP); // capteur 4
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:

}
