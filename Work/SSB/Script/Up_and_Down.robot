*** Settings ***
Documentation    Up and Down

Resource    ../Resource/Common.robot

*** Variables ***

*** Test Cases ***

Up and Down
    [Documentation]                         Test for Up and Down
    Open COM
    Start Dongle
    Push Button Up for 0.2 Second
    Release All Button for 1 Second
    Push Button Down for 0.2 Second
    Release All Button for 1 Second
    Push Button Up for 0.2 Second
    Release All Button for 1 Second
    Push Button Down for 0.2 Second
    Release All Button for 1 Second
    Push Button Up for 0.2 Second
    Release All Button for 1 Second
    Push Button Down for 0.2 Second
    Release All Button for 1 Second
    Push Button Up for 0.2 Second
    Release All Button for 1 Second
    Push Button Down for 0.2 Second
    Release All Button for 1 Second
    Start Test
    sleep    2
    LOG                                           End the Test




#Run the Script
#robot -d results test/test.robot

