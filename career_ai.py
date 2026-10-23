from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

careers = {

"ai engineer":{
"keywords":"ai artificial intelligence machine learning deep learning neural networks",
"answer":"Learn Python, Machine Learning, Deep Learning, TensorFlow and build AI projects."
},

"machine learning engineer":{
"keywords":"machine learning ml algorithms models",
"answer":"Learn Python, statistics, ML algorithms and model deployment."
},

"data scientist":{
"keywords":"data science analytics big data data scientist",
"answer":"Learn Python, statistics, machine learning and data visualization."
},

"data analyst":{
"keywords":"data analysis excel sql dashboards",
"answer":"Learn Excel, SQL, Python and tools like Power BI or Tableau."
},

"web developer":{
"keywords":"web development website html css javascript",
"answer":"Learn HTML, CSS, JavaScript, React and backend development."
},

"mobile developer":{
"keywords":"android ios mobile apps kotlin swift",
"answer":"Learn Kotlin/Java for Android or Swift for iOS development."
},

"software engineer":{
"keywords":"software engineer programming coding development",
"answer":"Learn programming languages, data structures and system design."
},

"cyber security":{
"keywords":"cyber security hacking ethical hacking network security",
"answer":"Learn networking, Linux and ethical hacking."
},

"cloud engineer":{
"keywords":"cloud aws azure cloud computing",
"answer":"Learn AWS, Azure, Docker and Kubernetes."
},

"devops engineer":{
"keywords":"devops ci cd automation docker kubernetes",
"answer":"Learn CI/CD pipelines, Docker and Linux automation."
},

"game developer":{
"keywords":"game development unity unreal game design",
"answer":"Learn C++, Unity and Unreal Engine."
},

"blockchain developer":{
"keywords":"blockchain crypto smart contracts ethereum",
"answer":"Learn Solidity and blockchain development."
},

"ui ux designer":{
"keywords":"ui ux design figma user interface",
"answer":"Learn Figma, Adobe XD and design thinking."
},

"database administrator":{
"keywords":"database sql dba data storage",
"answer":"Learn SQL, database design and management."
},

"network engineer":{
"keywords":"network networking routers switches",
"answer":"Learn networking concepts and network security."
},

"robotics engineer":{
"keywords":"robot robotics automation robots",
"answer":"Learn robotics programming and electronics."
},

"embedded systems engineer":{
"keywords":"embedded systems microcontroller iot",
"answer":"Learn C/C++, Arduino and IoT systems."
},

"bioinformatics":{
"keywords":"bioinformatics biology genome dna",
"answer":"Learn biology and Python for genome analysis."
},

"doctor":{
"keywords":"doctor medicine mbbs hospital",
"answer":"Study MBBS and medical sciences."
},

"lawyer":{
"keywords":"law lawyer legal advocate llb",
"answer":"Study LLB and legal practice."
},

"chartered accountant":{
"keywords":"ca accounting auditing taxation",
"answer":"Study accounting, auditing and taxation."
},

"business analyst":{
"keywords":"business analyst business analysis",
"answer":"Learn business analytics and Excel."
},

"product manager":{
"keywords":"product manager product strategy",
"answer":"Learn product management and leadership."
},

"digital marketing":{
"keywords":"digital marketing seo ads social media",
"answer":"Learn SEO, ads and social media marketing."
},

"graphic designer":{
"keywords":"graphic design photoshop illustrator",
"answer":"Learn Photoshop and Illustrator."
},

"civil engineer":{
"keywords":"civil engineering construction infrastructure",
"answer":"Study structural engineering and construction."
},

"mechanical engineer":{
"keywords":"mechanical engineering machines thermodynamics",
"answer":"Learn mechanics and CAD design."
},

"electrical engineer":{
"keywords":"electrical engineering circuits power systems",
"answer":"Study circuits and power systems."
},

"electronics engineer":{
"keywords":"electronics communication embedded systems",
"answer":"Learn electronics and communication systems."
},

"research scientist":{
"keywords":"research scientist phd research",
"answer":"Focus on scientific research and higher studies."
},

"upsc officer":{
"keywords":"upsc civil services ias ips government exam",
"answer":"Prepare for UPSC exam with polity, history, geography and current affairs."
},

"government jobs":{
"keywords":"government job ssc railway bank exam",
"answer":"Prepare for SSC, Banking and Railway exams."
},

"journalist":{
"keywords":"journalism reporter news media",
"answer":"Study journalism and media communication."
},

"photographer":{
"keywords":"photography camera photo editing",
"answer":"Learn photography and editing techniques."
},

"painter":{
"keywords":"painting art drawing sketch",
"answer":"Learn drawing, painting and art techniques."
},

"cricket player":{
"keywords":"cricket batsman bowler sports",
"answer":"Train in cricket academies and tournaments."
},

"football player":{
"keywords":"football soccer sports",
"answer":"Train professionally in football and leagues."
},

"badminton player":{
"keywords":"badminton shuttle sports",
"answer":"Practice badminton techniques and competitions."
},

"tennis player":{
"keywords":"tennis sports player",
"answer":"Train in tennis skills and tournaments."
},

"chess player":{
"keywords":"chess strategy tournament",
"answer":"Learn chess strategies and compete in tournaments."
},

"basketball player":{
"keywords":"basketball nba sports",
"answer":"Train in basketball and competitions."
},

"swimmer":{
"keywords":"swimming swimmer olympics",
"answer":"Train in swimming techniques and endurance."
},

"archer":{
"keywords":"archery archer olympic sport",
"answer":"Train in archery precision and competitions."
},

"boxer":{
"keywords":"boxing boxer combat sport",
"answer":"Train in boxing and strength training."
},

"gymnast":{
"keywords":"gymnastics gymnast olympics",
"answer":"Train flexibility and gymnastics skills."
},

"coach":{
"keywords":"sports coach trainer fitness coach",
"answer":"Learn sports science and coaching techniques."
}

}

career_names=list(careers.keys())
career_keywords=[careers[c]["keywords"] for c in career_names]

vectorizer=CountVectorizer()
career_vectors=vectorizer.fit_transform(career_keywords)

def get_career_answer(question):

    question_vec=vectorizer.transform([question.lower()])
    similarity=cosine_similarity(question_vec,career_vectors)

    index=similarity.argmax()
    career=career_names[index]

    return careers[career]["answer"]