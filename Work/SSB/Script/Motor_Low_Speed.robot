*** Settings ***
Documentation    SSB motor low speed

Resource    ../Resource/Common.robot

*** Variables ***

*** Test Cases ***

Low Speed
    [Documentation]                         Test for low speed
    Open COM
    Start Dongle
    Run Motor at Low Speed

    sleep    5
    Stop Motor
    sleep    2

    LOG                                           End the Test




#Run the Script
#robot -d results test/test.robot

