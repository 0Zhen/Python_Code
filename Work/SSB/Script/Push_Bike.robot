*** Settings ***
Documentation    SSB push bike

Resource    ../Resource/Common.robot

*** Variables ***

*** Test Cases ***

Push Bike
    [Documentation]                         Test for push bike
    Open COM
    Start Dongle
    Push assist for 4.5 Second
    Release All Button for 0.1 Second
    Push Button Up for 0.2 Second
    Release All Button for 0.1 Second
    Start Test
    sleep           15
    LOG                                           End the Test




#Run the Script
#robot -d results test/test.robot
