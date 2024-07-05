*** Settings ***
Documentation    Common

Library          ../Library/HTP_temp.py           COM17          115200




#Run the Script
#robot -d results test/test.robot


*** Keywords ***
Open COM
    HTP_temp.open_COM

Start Dongle
    HTP_temp.write    DG
    ${Return} =    HTP_temp.write    AT
    Should Be Equal  ${Return}    OK\r\n
    sleep    1

Push Button Power for 3 Second
    ${Return} =    HTP_temp.write      AT+LOADTEST=1000,8,1,[\\x08\\x00\\x00\\x00\\x00\\x00\\x00\\x00],0,3000
    Should Be Equal  ${Return}    OK\r\n

Release All Button for 0.1 Second
    ${Return} =    HTP_temp.write       AT+LOADTEST=1000,8,1,[\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00],1,100
    Should Be Equal  ${Return}    OK\r\n

Release All Button for 1 Second
    ${Return} =    HTP_temp.write       AT+LOADTEST=1000,8,1,[\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00],1,1000
    Should Be Equal  ${Return}    OK\r\n

Push Button Up for 0.2 Second
    ${Return} =    HTP_temp.write       AT+LOADTEST=1000,8,1,[\\x02\\x00\\x00\\x00\\x00\\x00\\x00\\x00],2,200
    Should Be Equal  ${Return}    OK\r\n

Push assist for 4.5 Second
    ${Return} =    HTP_temp.write      AT+LOADTEST=1000,8,1,[\\x20\\x00\\x00\\x00\\x00\\x00\\x00\\x00],0,4500
    Should Be Equal  ${Return}    OK\r\n

Push Button Up for 0.35 Second
    ${Return} =    HTP_temp.write       AT+LOADTEST=1000,8,1,[\\x02\\x00\\x00\\x00\\x00\\x00\\x00\\x00],2,3500
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

Check Motor Current
    ${Return} =    HTP_temp.write       AT+MOTOR=1
    ${result} =    Convert To Number   ${Return}
    Should Be True  ${result} > 0.5

Check Motor Speed
    ${Return} =    HTP_temp.write       AT+MOTOR=0
    ${result} =    Convert To Number   ${Return}
    Should Be True  ${result} > 20