*** Settings ***
Library		RequestsLibrary
#Library  	JsonLibrary
Library  	Collections


*** Variables ***
${Base_Url}  	https://restful-booker.herokuapp.com



*** Test Cases ***
TC_001_Get_Request
	Create Session  	Get_details  	${Base_Url}
	${resp} = 			GET On Session  Get_details  	/booking
	log to console 		${resp} 