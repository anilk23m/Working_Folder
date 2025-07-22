*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
#@{Name}       Alice    Bob    Charlie

#${Name} =  Create List    Alice    Bob    Charlie

${name}     Anil
${age}      30

*** Test Cases ***

#Create a list with multiple names
    #Log    ${Name}

Create and access dictionary
    ${person}=  Create Dictionary       name=${name}      age=${age}      city=NewYork
    Log     ${person}

    ${name}=    Get From Dictionary     ${person}       name
    ${age}=     Get From Dictionary     ${person}       age
    Log     Name is ${name}, Age is ${age}