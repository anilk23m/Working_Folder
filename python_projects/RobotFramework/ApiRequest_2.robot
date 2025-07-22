*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${BASE_URL}    https://jsonplaceholder.typicode.com

*** Test Cases ***
Validate GET Response And Body
    Create Session    mysession    ${BASE_URL}

    # Send GET request to /users/1
    ${response}=    Get Request    mysession    /users/1

    # Verify status code is 200 OK
    Should Be Equal As Integers    ${response.status_code}    200

    # Parse JSON response
    ${response_json}=   set variable  ${response.json()}

    # Verify some fields in the response JSON
    Should Be Equal As Strings   ${response_json['id']}    1
    Should Be Equal    ${response_json['username']}    Bret
    Should Contain    ${response_json['email']}    @
