*** Settings ***
Library           RequestsLibrary
Library           JSONLibrary
Library           Collections
Library           os
Library           BuiltIn
Library           OperatingSystem
*** Variables ***
${BASE_URL}       https://jsonplaceholder.typicode.com
${ENDPOINT}       /posts/1

*** Test Cases ***
Validate Get API Response
    Create Session    mysession    ${BASE_URL}
    ${response}=      Get Request  mysession    ${ENDPOINT}

    Should Be Equal As Integers    ${response.status_code}    200

    ${response_body}=    To Json    ${response.content}
    Dictionary Should Contain Key    ${response_body}    title
    Dictionary Should Contain Key    ${response_body}    userId

    Should Be Equal As Strings    ${response_body['id']}    1

    ${json_data}=       Get File     sample_data.json
    ${data}=        Evaluate    json.loads('''${json_data}''')      modules=json
    log    ${data}

    FOR     ${i}    IN      @{data}
        Run Keyword If     ${i["id"]} == 10     Set To Dictionary      ${i}    price     100
    END

    ${updated_data}=        Evaluate    json.dumps(${data}, indent=2)    modules=json
    Create File     updated_data.json       ${updated_data}