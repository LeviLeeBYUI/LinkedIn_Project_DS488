import requests
import pandas as pd
import time

api_key = '-oYp4KfVe-mGo5h4PX1cTw'
headers = {'Authorization': 'Bearer ' + api_key}

students_api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/school/students/'
students_params = {
    'linkedin_school_url': 'https://www.linkedin.com/school/byu-idaho/', 
    'page_size': '1',
    'student_status': 'current',
    'sort_by': 'recently-matriculated',    
}

students_response = requests.get(students_api_endpoint, params=students_params, headers=headers)

print(f"API Status Code: {students_response.status_code}")  
print(f"API Response: {students_response.text[:500]}")

if students_response.status_code == 200:
    students_data = students_response.json().get("students", [])
    
    if not students_data:
        print("API returned an empty list. Try adjusting filters or increasing page size.")
        exit()  
else:
    print(f"Error in Students API: {students_response.status_code} - {students_response.text}")
    exit()

person_api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
filtered_students = []

for student in students_data:
    profile_url = student.get("profile_url", "")

    person_params = {
        'linkedin_profile_url': profile_url,
        'inferred_salary': 'include',
        'extra': 'include',
        'use_cache': 'if-present',
        'fallback_to_cache': 'on-error',
    }

    person_response = requests.get(person_api_endpoint, params=person_params, headers=headers)

    if person_response.status_code == 200:
        person_data = person_response.json()
        
        full_name = person_data.get("full_name", "Unknown")
        inferred_salary = person_data.get("inferred_salary", "N/A")
        
        education = person_data.get("education", [])
        school_names = [edu.get("school", "") for edu in education]

        filtered_students.append({
            "full_name": full_name,
            "profile_url": profile_url,
            "inferred_salary": inferred_salary,
            "education": ", ".join(school_names)
        })
    
    else:
        print(f"Error in Person API for {profile_url}: {person_response.status_code} - {person_response.text}")

    time.sleep(1)

df = pd.DataFrame(filtered_students)

df.to_csv("byui_students_final.csv", index=False)
print("Filtered data saved to byui_students_final.csv")
