
## happy path               <!-- name of the story - just for debugging -->
* greet              
  - utter_greet
* mood_great               <!-- user utterance, in format intent[entities] -->
  - utter_happy
* mood_affirm
  - utter_happy
* mood_affirm
  - utter_goodbye
  
## sad path 1               <!-- this is already the start of the next story -->
* greet
  - utter_greet             <!-- action the bot should execute -->
* mood_unhappy
  - utter_ask_picture
* mood_affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_ask_picture
* mood_deny
  - utter_goodbye
  
## sad path 3
* greet
  - utter_greet
* mood_affirm
  - utter_happy
  
## strange user
* mood_affirm
  - utter_happy
* mood_affirm
  - utter_unclear

## course launch issue
* Course_Launch_Issue
  - utter_course_launch_issue
* Course_Creation
  - utter_course_creation
* User_Login_Issue
  - utter_user_login_issue

## user login issue
* User_Login_Issue
  - utter_user_login_issue

## course next button
* Course_Next_Button
  - utter_course_next_button
* Asssessmet_Page_Activity
  - utter_assesment_page_activity

## course creation
* Course_Creation
  - utter_course_creation

## assesment page activity 
* Asssessmet_Page_Activity
  - utter_assesment_page_activity
  
## Live wire
* LIVEWIRE
  - utter_livewire
  
## access livewire
*acces_livewire
  - utter_access_livewire
  
## livewire_cours
*livewire_cours
  -utter_livewire_cours
  
## application Livewire
* app_LiveWire
  - utter_app_livewire

## say goodbye
* goodbye
  - utter_goodbye
  
##asking bot name
* botname
  - utter_botname

## user helping
* helpuser
  - utter_helpuser

## bot language
* botlanguage
  - utter_botlang

## age of bot
*botage
  - utter_botage

## all course
* allcourse
 - utter_all_course

## my enroll course
* my_enroll_course
 - utter_my_enroll_Course

## technical course
* technical_course
 - utter_technical_Course

## my completed course
* comp_training
 - utter_completed_Course

## softskill course
* softskill_course
 - utter_softskill_course

## launch course
* launch_course
 - utter_launch_course

## enroll course
* enroll_course
 - utter_enroll_course

## start course
* start_course
 - utter_start_course
 
## course register-----------------------------------------

* course_register
  - utter_course_register
* self_register
  - utter_self_register
* already_reg
  - utter_already_reg
  
## self_register
* self_register
  - utter_self_register
  
## already_reg
* already_reg
  - utter_already_reg
  
## course search

* course_search
  - utter_course_search
* specific_cours
  - utter_specific_cours
* global_search
  - utter_global_search

##specific course
* specific_cours
  - utter_specific_cours

##global search
* global_search
  - utter_global_search

## certificate

* certificate
  - utter_certificate
* list_certificate
  - utter_list_certificate

## list_certi
* list_certificate
  - utter_list_certificate

## certificate issue
* certificate_issue
  - utter_certificate_issue

## Transcript
* transcript
  - utter_transcript
  
## mood happy 
* mood_affirm
  - utter_happy

## course complete issue 
* course_complt_issue
  - utter_course_complt_issue

## issue complete course 
* issue_comp_course
  - utter_issue_comp_course
  
## Course_Prerequisite
* Course_Prerequisite
  - utter_Course_Prerequisite

## course_engine
* course_engine
  - utter_course_engine  

## Recommended_Course 
* Recommended_Course
  - utter_Recommended_Course
  
## Course_Create
* Course_Create
  - utter_Course_Create 
  
## Email_Trigger 
* Email_Trigger
  - utter_Email_Trigger
  
## Training_Request
* Training_Request
  - utter_Training_Request  
  
## Enrolment
* Enrolment
  - utter_Enrolment
  
  
## Course_Assignment 
* Course_Assignment
  - utter_Course_Assignment
  
  
## Suggestion path 9-----------------------------------------
* greet
  - utter_greet
* paper_search{"paper_type":"physics"}
  - action_paper_search
  - utter_happy
* mood_affirm
  - utter_happy
  
## enroll course  path
* greet
  - utter_greet 
* enroll{"enroll_type":"id enroll"}
  - action_enroll
  - utter_happy
* mood_affirm
  - utter_happy

## fallback
  - utter_unclear

