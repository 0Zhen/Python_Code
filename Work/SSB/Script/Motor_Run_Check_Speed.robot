*** Settings ***
Documentation    SSB motor check speed

Resource    ../Resource/Common.robot

*** Variables ***

*** Test Cases ***

Check Speed
    [Documentation]                         Test for speed check
    Open COM
    Start Dongle
    Run Motor at Low Speed
    sleep    2
    RUN KEYWORD AND IGNORE ERROR     Check Motor Speed
    sleep    5
    Stop Motor
    sleep    2


    sleep                                           2
    LOG                                           End the Test




#Run the Script
#robot -d results test/test.robot




