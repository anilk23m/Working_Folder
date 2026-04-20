*** Settings ***
Metadata     Anil Kumar
Test Template   Add Numbers


*** Variables ***
${A1}    2
${B1}    3
${EXPECTED1}    5

${A2}    10
${B2}    20
${EXPECTED2}    30

${A3}    -5
${B3}    5
${EXPECTED3}    0

*** Test Cases ***
Addition with Different Inputs
    [Tags]    math
    ${A1}    ${B1}    ${EXPECTED1}
    ${A2}    ${B2}    ${EXPECTED2}
    ${A3}    ${B3}    ${EXPECTED3}

*** Keywords ***
Add Numbers
    [Arguments]    ${a}    ${b}    ${expected}
    ${result}=    Evaluate    ${a} + ${b}
    Should Be Equal As Integers    ${result}    ${expected}