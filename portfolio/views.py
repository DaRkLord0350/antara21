from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'name': 'Antara Shaw',
        'title': 'Data Engineer & Analytics Expert',
        'location': 'Howrah, West Bengal',
        'email': 'antarashaw.914@gmail.com',
        'phone': '+91-9142986573',
        'linkedin': 'LinkedIn',
        'github': 'GitHub',
        'birth_date': 'Nov 2021',
        'nationality': 'Indian',
        'education': [
            {
                'year': '2021-2025',
                'institution': 'National Institute of Technology, Durgapur',
                'degree': 'Bachelor of Technology in Biotechnology',
                'grade': 'CGPA: 7.2'
            },
            {
                'year': '2018-2020',
                'institution': 'BNS DAV Public School',
                'degree': 'Higher Secondary',
                'grade': '95%'
            },
            {
                'year': '2016-2018',
                'institution': 'BNS DAV Public School',
                'degree': 'Secondary',
                'grade': '91.6%'
            }
        ],
        'experience': [
            {
                'year': '2024',
                'position': 'Data Engineering Projects',
                'company': 'Smart Disaster Response & Sales Analytics',
                'description': 'Built scalable data pipelines using AWS and Google Cloud'
            },
            {
                'year': '2022-2025',
                'position': 'Assistant General Secretary & IT Wing Head',
                'company': 'SPIC MACAY, NIT Durgapur',
                'description': 'Led IT initiatives and organized cultural events'
            }
        ],
        'skills': {
            'software': ['Python', 'SQL', 'AWS', 'Docker'],
            'coding': ['Apache Spark', 'ETL Development', 'Data Pipeline Architecture', 'Cloud Computing']
        },
        'languages': [
            {'name': 'English', 'level': 'Fluent'},
            {'name': 'Hindi', 'level': 'Native'},
            {'name': 'Bengali', 'level': 'Native'}
        ],
        'activities': [
            {
                'year': '2024',
                'activity': 'Myntra HackerRamp Phase 2',
                'description': 'Selected in top 70 teams from 30,000+ registrations'
            },
            {
                'year': '2024',
                'activity': 'LeetCode Problem Solving',
                'description': 'Solved 100+ problems focused on SQL & Pandas'
            }
        ],
        'hobbies': [
            {'name': 'Data Analytics', 'icon': '📊'},
            {'name': 'Cloud Computing', 'icon': '☁️'},
            {'name': 'Problem Solving', 'icon': '🧩'},
            {'name': 'Technology', 'icon': '💻'}
        ]
    }
    return render(request, 'portfolio/home.html', context)
    # Render the home template with the context data
    # This will display the portfolio information dynamically
    # return render(request, 'portfolio/home.html')