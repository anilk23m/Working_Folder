*** Settings ***
Library   SeleniumLibrary


*** Variables ***
${url}       https://www.google.com/
${browser}   chrome

*** Test Cases ***
TC01- Login Test
    open browser   ${url}   ${browser}

    input text   //textarea[@class='gLFyf']        Hrithik Roshan
    #Press Keys      name:q    ENTER
    Click Element    //input[@value='Google Search']
    sleep   60
    Capture Page Screenshot
    Close Browser
