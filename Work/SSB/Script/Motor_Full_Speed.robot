*** Settings ***
Documentation    SSB motor full speed

Resource    ../Resource/Common.robot

*** Variables ***

*** Test Cases ***

Full Speed
    [Documentation]                         Test for full speed
    Open COM
    Start Dongle
    Run Motor at Full Speed
    sleep    5
    Stop Motor
    sleep                                           2
    LOG                                           End the Test




#Run the Script
#robot -d results test/test.robot

