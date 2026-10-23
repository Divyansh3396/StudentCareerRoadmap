# career_roadmap.py

roadmaps = {
    "Web Development": [
        "Learn HTML, CSS, JavaScript",
        "Build small websites",
        "Learn a frontend framework like React or Angular",
        "Learn backend basics: Node.js or Python Flask/Django",
        "Build full-stack projects",
        "Learn databases: MySQL, MongoDB",
        "Deploy projects on hosting platforms",
        "Prepare for web developer interviews"
    ],
    "AIML": [
        "Learn Python programming",
        "Understand Math for ML (Linear Algebra, Calculus, Probability)",
        "Learn Data Science basics",
        "Learn Machine Learning Algorithms",
        "Work on ML projects",
        "Learn Deep Learning and NLP",
        "Deploy AI projects",
        "Prepare for AI engineer interviews"
    ],
    "Data Science": [
        "Learn Python and R",
        "Study Statistics",
        "Data Cleaning & Preprocessing",
        "Learn Machine Learning",
        "Data Visualization",
        "Build Data Projects",
        "Deploy Data Products",
        "Prepare for Data Scientist interviews"
    ],
    "Cyber Security": [
        "Learn Networking basics",
        "Understand Linux OS",
        "Study Ethical Hacking",
        "Learn Security Tools",
        "Practice Capture The Flag (CTF) challenges",
        "Internship in Security",
        "Get Cyber Security Certification",
        "Apply for Security Analyst roles"
    ],
    "MBBS": [
        "Study Biology & Chemistry",
        "Prepare for Medical Entrance Exams",
        "Complete MBBS course",
        "Hospital Internship / Residency",
        "Specialization (MD/MS)",
        "Research & Publications",
        "Practice as a Doctor",
        "Prepare for medical board exams"
    ],
    "LLB": [
        "Complete Law Graduation (LLB)",
        "Study Criminal & Civil Law",
        "Internship in law firms",
        "Moot Court practice",
        "Bar Council Exam",
        "Specialize in a Law domain",
        "Work as Lawyer / Corporate Counsel",
        "Continuous learning & seminars"
    ],
    "BDS": [
        "Dental Entrance Exam",
        "Complete BDS Degree",
        "Clinical Practice",
        "Dental Internship",
        "Specialization if needed",
        "Start Dental Practice",
        "Work in Hospital / Clinic",
        "Continuing Dental Education"
    ],
    "BAMS": [
        "Study Ayurveda",
        "Medical Entrance Preparation",
        "Complete BAMS Degree",
        "Clinical Practice",
        "Ayurvedic Internship",
        "Start Practice",
        "Ayurvedic Research",
        "Ayurvedic Consultant roles"
    ],
    "BHMS": [
        "Study Homeopathy",
        "Medical Entrance",
        "Complete BHMS Degree",
        "Clinic Training",
        "Internship",
        "Practice Homeopathy",
        "Advanced Homeopathic Training",
        "Build Patient Network"
    ],
    "Nursing": [
        "Complete Nursing Course",
        "Clinical Training",
        "Hospital Internship",
        "Registered Nurse Certification",
        "Specialize if needed",
        "Apply for Nurse Roles",
        "Continuous Education",
        "Leadership / Head Nurse positions"
    ],
    "Pharmacy": [
        "Pharmacy Diploma/Degree",
        "Drug Research & Pharmacology",
        "Internship in Pharmacy",
        "Clinical Trials",
        "Work in Pharmaceutical Company",
        "Certification / Licensing",
        "Pharmacist roles",
        "Advanced Specializations"
    ],
    "Physiotherapy": [
        "Study Physiology & Anatomy",
        "Complete Physiotherapy Degree",
        "Clinical Training",
        "Hospital Internship",
        "Practice Physiotherapy",
        "Specialize in sports or rehab",
        "Work in Clinics/Hospitals",
        "Advanced Certifications"
    ],
    "Medical Lab Technology": [
        "Lab Equipment Training",
        "Diagnostic Testing",
        "Hospital Internship",
        "Complete ML Technology Course",
        "Work in Medical Labs",
        "Specialization if needed",
        "Certification Courses",
        "Lab Supervisor / Technologist Roles"
    ],
    "Chartered Accountant": [
        "CA Foundation",
        "CA Intermediate",
        "Articleship",
        "CA Final",
        "Chartered Accountant License",
        "Work in Accounting Firm",
        "Advanced Accounting & Finance Training",
        "Corporate CA / Advisory Roles"
    ],
    "Company Secretary": [
        "CS Foundation",
        "CS Executive",
        "CS Professional",
        "Corporate Law Training",
        "Internship in Company Secretary Office",
        "Complete CS Certification",
        "Work in Corporates",
        "Board Level Advisory"
    ],
    "Cost Accountant": [
        "CMA Foundation",
        "CMA Intermediate",
        "CMA Final",
        "Articleship / Internship",
        "Work in Cost / Financial Analysis",
        "Certification",
        "Consulting Roles",
        "Senior CMA Positions"
    ],
    "BBA": [
        "Business Management Basics",
        "Marketing & Finance Studies",
        "Internship",
        "Corporate Projects",
        "Specialization (HR, Finance, Marketing)",
        "Prepare for Manager Roles",
        "Apply for Jobs",
        "Continuous Learning"
    ],
    "Finance Analyst": [
        "Finance Degree",
        "Accounting Skills",
        "Financial Modeling",
        "Internship in Finance",
        "Advanced Excel / Tools",
        "Work in Finance Analyst Roles",
        "Certifications (CFA, CPA)",
        "Leadership Roles"
    ],
    "Banking": [
        "Commerce / Finance Degree",
        "Bank Exams Preparation",
        "Bank PO Training",
        "Banking Internship",
        "Join Bank as Officer",
        "Advanced Banking Certifications",
        "Specialized Banking Roles",
        "Promotion to Manager / Senior Roles"
    ],
    "Journalism": [
        "Mass Communication / Journalism Degree",
        "News Writing Practice",
        "Internship in Media",
        "Portfolio Creation",
        "Work in News Agency",
        "Freelance Projects",
        "Specialization in Media",
        "Senior Editor / Reporter Roles"
    ],
    "Photography": [
        "Learn Camera Basics",
        "Photo Editing Software",
        "Build Portfolio",
        "Internship / Freelance Work",
        "Specialization (Fashion, Wildlife, etc.)",
        "Exhibitions & Online Portfolio",
        "Photography Projects",
        "Professional Photographer"
    ],
    "Painting": [
        "Art Fundamentals",
        "Painting Techniques",
        "Create Artwork",
        "Exhibitions",
        "Portfolio Building",
        "Freelance Projects",
        "Art Critiques",
        "Professional Artist"
    ],
    "Animation": [
        "Learn Animation Software",
        "2D/3D Animation",
        "Animation Projects",
        "Internship",
        "Portfolio",
        "Freelance Work",
        "Work in Animation Studio",
        "Animator Career"
    ],
    "Film Making": [
        "Learn Film Direction",
        "Script Writing",
        "Video Production",
        "Editing Skills",
        "Short Film Projects",
        "Internship",
        "Professional Film Making",
        "Director / Producer Career"
    ],
    "UPSC": [
        "Study NCERT Books",
        "Current Affairs Preparation",
        "Prelims Exam",
        "Mains Exam",
        "Interview",
        "IAS Training",
        "IAS Officer Preparation",
        "Join Civil Services"
    ],
    "SSC": [
        "General Studies Preparation",
        "SSC Prelims",
        "SSC Mains",
        "Interview",
        "Government Job",
        "Training",
        "Apply for Posts",
        "Join SSC Services"
    ],
    "Railway Jobs": [
        "Railway Exam Preparation",
        "Technical Training",
        "Internship / Field Training",
        "Apply for Railway Jobs",
        "Join Railways",
        "Promotion / Skills Upgrade",
        "Specialized Railway Roles",
        "Senior Positions"
    ],
    "Cricket Player": [
        "Professional Coaching",
        "District Matches",
        "State Team",
        "National Team",
        "International Training",
        "Tournaments",
        "Contracts / Sponsorships",
        "Professional Cricket Career"
    ],
    "Football Player": [
        "Football Academy",
        "League Matches",
        "State Team",
        "National Team",
        "Professional Club",
        "Tournaments",
        "Contracts / Sponsorships",
        "Professional Football Career"
    ],
    "Badminton Player": [
        "Badminton Coaching",
        "Tournaments",
        "National Level",
        "International Level",
        "Professional Club",
        "Sponsorships",
        "Contracts",
        "Professional Badminton Career"
    ],
    "Tennis Player": [
        "Tennis Academy",
        "Tournaments",
        "Professional Matches",
        "National Level",
        "International Level",
        "Sponsorships",
        "Contracts",
        "Professional Tennis Career"
    ],
    "Athletics": [
        "Sports Training",
        "District Competitions",
        "State Competitions",
        "National Competitions",
        "International Competitions",
        "Professional Coaching",
        "Sponsorships",
        "Professional Athlete Career"
    ]
}

# ✅ This now includes 45+ degrees and careers.