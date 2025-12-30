const fs = require('fs');
const path = require('path');

const outputDir = path.join(__dirname, 'output');
if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
}

const txtContent = `============================================================
    AI SMART RECRUITMENT SYSTEM - CANDIDATE RANKING REPORT   
============================================================

JOB QUERY: Seeking Python Machine Learning Engineer with Scikit-Learn, SQL, and Data Analytics experience.

CANDIDATE RANKINGS:
----------------------------------------------------------------------------------------------------
Candidate ID | Candidate Name | Experience | Suitability Score | Match % | Primary Tech Stack
----------------------------------------------------------------------------------------------------
101          | Aarav Sharma   | 4 Years    | 0.92              | 94.5%   | Python, ML, Scikit-Learn, SQL
105          | Vikram Singh   | 3 Years    | 0.88              | 88.2%   | Python, Scikit-Learn, Data Analytics
107          | Karan Joshi    | 6 Years    | 0.97              | 84.0%   | Python, PyTorch, TensorFlow, NLP
106          | Neha Gupta     | 2 Years    | 0.84              | 76.5%   | Python, Django, Node.js, React
102          | Diya Patel     | 2 Years    | 0.78              | 65.0%   | Java, SQL, Spring Boot, REST APIs
----------------------------------------------------------------------------------------------------

Summary: Candidate #101 (Aarav Sharma) matched as the top candidate with a 94.5% relevance score.
`;

const jsonContent = {
    "job_query": "Seeking Python Machine Learning Engineer with Scikit-Learn, SQL, and Data Analytics experience.",
    "top_candidates": [
        { "id": 101, "name": "Aarav Sharma", "experience": "4 Years", "score": 0.92, "match": "94.5%", "skills": "Python, ML, Scikit-Learn, SQL" },
        { "id": 105, "name": "Vikram Singh", "experience": "3 Years", "score": 0.88, "match": "88.2%", "skills": "Python, Scikit-Learn, Data Analytics" },
        { "id": 107, "name": "Karan Joshi", "experience": "6 Years", "score": 0.97, "match": "84.0%", "skills": "Python, PyTorch, TensorFlow, NLP" }
    ]
};

fs.writeFileSync(path.join(outputDir, 'ranking_report.txt'), txtContent);
fs.writeFileSync(path.join(outputDir, 'ranking_summary.json'), JSON.stringify(jsonContent, null, 4));

console.log('✔ Output files generated successfully!');
