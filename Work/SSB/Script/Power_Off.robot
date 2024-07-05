*** Settings ***
Documentation    SSB Power Off

Resource    ../Resource/Common.robot

*** Variables ***

*** Test Cases ***

Power Off
    [Documentation]                         Test for power off
    Open COM
    Start Dongle
    Push Button Power for 3 Second
    Release All Button for 1 Second
    sleep    3
    Start Test
    LOG                                           End the Test




#Run the Script
#robot -d results test/test.robot
