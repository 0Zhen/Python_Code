*** Settings ***
Documentation    SSB auto testing

Library          ../Library/HTP_temp.py           COM17          115200

*** Variables ***

*** Test Cases ***

CAN Bus Test
    [Documentation]                         Test for CAN Bus communication
    HTP_temp.open_COM
    Start Dongle
    Push Button Up for 0.2 Second
    Release All Button for 1 Second
    Start Test
    sleep    5

    Push Button Up for 0.2 Second
    Release All Button for 1 Second
    Start Test
    sleep    5

    Push Button Down for 0.2 Second
    Release All Button for 1 Second
    Start Test
    sleep    5
    Push Button Down for 0.2 Second
    Release All Button for 1 Second
    Start Test

    LOG                                           End the Test




#Run the Script
#robot -d results test/test.robot


*** Keywords ***
Start Dongle
    HTP_temp.write    DG
    ${Return} =    HTP_temp.write    AT
    Should Be Equal  ${Return}    OK\r\n
    sleep    1

Push Button Power for 3 Second
    ${Return} =    HTP_temp.write      AT+LOADTEST=1000,8,1,[\\x08\\x00\\x00\\x00\\x00\\x00\\x00\\x00],0,3000
    Should Be Equal  ${Return}    OK\r\n


Release All Button for 1 Second
    ${Return} =    HTP_temp.write       AT+LOADTEST=1000,8,1,[\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00],1,1000
    Should Be Equal  ${Return}    OK\r\n

Push Button Up for 0.2 Second
    ${Return} =    HTP_temp.write       AT+LOADTEST=1000,8,1,[\\x02\\x00\\x00\\x00\\x00\\x00\\x00\\x00],2,200
    Should Be Equal  ${Return}    OK\r\n

Push Button Down for 0.2 Second
    ${Return} =    HTP_temp.write       AT+LOADTEST=1000,8,1,[\\x10\\x00\\x00\\x00\\x00\\x00\\x00\\x00],2,200
    Should Be Equal  ${Return}    OK\r\n

Run Motor at Low Speed
    ${Return} =    HTP_temp.write       DG+CANSEND=20010,1,[0288130000]
    should be equal  ${Return}    OK\r\n

Run Motor at Full Speed
    ${Return} =    HTP_temp.write       DG+CANSEND=20010,1,[02FFFF0000]
    should be equal   ${Return}   OK\r\n

Stop Motor
    ${Return} =    HTP_temp.write       DG+CANSEND=20010,1,[00FFFF0000]
    should be equal  ${Return}    OK\r\n

Start Test
    ${Return} =    HTP_temp.write       AT+TEST=1
    Should Be Equal  ${Return}    OK\r\n

Check Motor State
    ${Return} =    HTP_temp.write       AT+MOTOR?
    ${result} =    Convert To Number   ${Return}

    Should Be True  ${result} > 20
