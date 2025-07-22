*** Settings ***
Library           RequestsLibrary
Library           Collections

*** Variables ***
${BASE_URL}       https://example.com/api
${GET_TOKEN_ENDPOINT}    /auth/token
${POST_ENDPOINT}         /submit/data
${USERNAME}       your_username
${PASSWORD}       your_password

*** Test Cases ***
Get Token And Post Data
    [Documentation]    Get an auth token and use it for a POST request.

    # Step 1: Create a session
    Create Session    api    ${BASE_URL}

    # Step 2: Send GET request to get the token
    ${headers}=       Create Dictionary    Content-Type=application/json
    ${params}=        Create Dictionary    username=${USERNAME}    password=${PASSWORD}
    ${response}=      Get Request    api    ${GET_TOKEN_ENDPOINT}    headers=${headers}    params=${params}

    Should Be Equal As Integers    ${response.status_code}    200
    ${json}=           To Json    ${response.content}
    ${TOKEN}=          Get From Dictionary    ${json}    token

    Log    Token received: ${TOKEN}

    # Step 3: Use the token to make a POST request
    ${auth_headers}=    Create Dictionary    Content-Type=application/json    Authorization=Bearer ${TOKEN}
    ${post_data}=       Create Dictionary    key1=value1    key2=value2
    ${response2}=       Post Request    api    ${POST_ENDPOINT}    headers=${auth_headers}    json=${post_data}

    Should Be Equal As Integers    ${response2.status_code}    200
    Log    Response: ${response2.content}
