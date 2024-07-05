*** Settings ***
Documentation    SSB Power On

Resource    ../Resource/Common.robot

*** Variables ***

*** Test Cases ***

Power On
    [Documentation]                         Test for power on
    Open COM
    Start Dongle
    Push Button Power for 3 Second
    Release All Button for 1 Second
    sleep    3
    Start Test
    LOG                                           End the Test




#Run the Script
#robot -d results test/test.robot
