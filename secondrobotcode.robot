*** Settings ***
Library		RequestsLibrary
#Library  	JsonLibrary
Library  	Collections


*** Variables ***
${Base_Url}  	https://restful-booker.herokuapp.com


*** Test Cases ***
TC_001_Get_Request_003
	Create Session  	Get_details  	${Base_Url}
	${resp} = 			GET On Session  Get_details  	/booking/003
	log to console 		${resp.content} 
	log to console 		${resp.status_code}
	


	#validations
	${status_code}= 	convert to string 	${resp.status_code}
	should be equal 	${status_code}		200
	
	${body}= 	convert to string 	${resp.content}
	should contain 	${body}		Mark
	

TC_002_Get_Request_172
	Create Session  	Get_details  	${Base_Url}
	${resp} = 			GET On Session  Get_details  	/booking/172
	log to console 		${resp.content} 
	log to console 		${resp.status_code}
	


	#validations
	${status_code}= 	convert to string 	${resp.status_code}
	should be equal 	${status_code}		200
	
	${body}= 	convert to string 	${resp.content}
	should contain 	${body}		Doe	