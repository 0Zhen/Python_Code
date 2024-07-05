*** Settings ***
Documentation    SSB motor Check Current

Resource    ../Resource/Common.robot


*** Variables ***

*** Test Cases ***

Check Current
    [Documentation]                         Test for current check
    Open COM
    Start Dongle
    Run Motor at Low Speed
    sleep    2
    RUN KEYWORD AND IGNORE ERROR     Check Motor Current
    sleep    5
    Stop Motor
    sleep    2


    sleep                                           2
    LOG                                           End the Test




#Run the Script
#robot -d results test/test.robot

