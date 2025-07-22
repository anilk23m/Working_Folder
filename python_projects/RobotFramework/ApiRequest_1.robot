*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}    https://jsonplaceholder.typicode.com

*** Test Cases ***

Send POST Request
    Create Session    mysession    ${BASE_URL}

    # Define JSON payload as a dictionary
    &{payload}=    Create Dictionary    title=foo    body=bar    userId=1

    # Send POST request with JSON payload
    ${response}=    Post Request    mysession    /posts    json=${payload}

    # Verify response status code is 201 Created
    Should Be Equal As Integers    ${response.status_code}    201

    # Log the response JSON
    Log    ${response.json()}
