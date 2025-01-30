import json
import pandas as pd
data = {
    'employees': [
        {'profile_url': 'https://www.linkedin.com/in/darya-mazandarany-0078975', 'profile': None, 'last_updated': None},
        {'profile_url': 'https://www.linkedin.com/in/dave-dadoun-02003425', 'profile': None, 'last_updated': None},
        {'profile_url': 'https://www.linkedin.com/in/bhawanikatyal', 'profile': None, 'last_updated': None},
        {'profile_url': 'https://www.linkedin.com/in/bill-campman-a84b8b5', 'profile': None, 'last_updated': None},
        {'profile_url': 'https://www.linkedin.com/in/bill-spencer-5913765', 'profile': None, 'last_updated': None},
        {'profile_url': 'https://www.linkedin.com/in/davidqiao', 'profile': None, 'last_updated': None},
        {'profile_url': 'https://www.linkedin.com/in/debinanda', 'profile': None, 'last_updated': None},
        {'profile_url': 'https://www.linkedin.com/in/debra-epperson-29ba6915', 'profile': None, 'last_updated': None},
        {'profile_url': 'https://www.linkedin.com/in/deepads', 'profile': None, 'last_updated': None},
        {'profile_url': 'https://www.linkedin.com/in/deepthihari', 'profile': None, 'last_updated': None}
    ],
    'next_page': 'https://nubela.co/proxycurl/api/linkedin/company/employee/search/?linkedin_company_profile_url=https%3A%2F%2Fwww.linkedin.com%2Fcompany%2Fmicrosoft%2F&keyword_regex=ceo%7Ccto&page_size=10&country=us&query=Brigham+Young+University-Idaho&limit=10&after=derek-mehlhorn-3024b927'
}

# 직원 데이터만 추출
employees = data["employees"]

# DataFrame 변환
df = pd.DataFrame(employees)

# CSV 저장
df.to_csv("linkedin_employees.csv", index=False)
print("Data saved to linkedin_employees.csv")