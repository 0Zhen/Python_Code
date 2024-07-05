*** Settings ***
Documentation    SSB turn light on

Resource    ../Resource/Common.robot


*** Variables ***

*** Test Cases ***

Turn Light ON
    [Documentation]                         Test for turn light on
    Open COM
    Start Dongle
    Push Button Up for 0.35 Second
    Release All Button for 1 Second

    Start Test
    sleep    5

    LOG                                           End the Test




#Run the Script
#robot -d results test/test.robot
