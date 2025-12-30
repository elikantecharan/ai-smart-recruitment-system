import os
import sys
from src.ranker import SmartRecruitmentSystem

def main():
    print("=" * 60)
    print("      AI-POWERED SMART RECRUITMENT & RANKING SYSTEM")
    print("=" * 60)
    
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'candidates.csv')
    if not os.path.exists(data_path):
        print(f"Error: Dataset not found at {data_path}")
        return

    print("[+] Initializing Machine Learning Model & Vectorizers...")
    system = SmartRecruitmentSystem(data_path)
    print("[+] Model loaded successfully!\n")

    sample_job_descriptions = [
        "Python Machine Learning Engineer with Scikit-Learn, Pandas, and SQL skills.",
        "Full-Stack Web Developer with React, Node.js, and MongoDB experience.",
        "Deep Learning AI Researcher proficient in PyTorch, Computer Vision, and NLP."
    ]

    for i, job in enumerate(sample_job_descriptions, 1):
        print(f"\n👉 SAMPLE JOB QUERY #{i}:")
        print(f"   \"{job}\"")
        print("-" * 60)
        ranked = system.rank_candidates(job, top_n=3)
        for idx, row in ranked.iterrows():
            print(f"   Score: {row['final_match_score']:.1f}% | ID: {row['candidate_id']} | Name: {row['name']} ({row['experience_years']} yrs exp) | Skills: {row['skills']}")
        print("-" * 60)

    print("\n✅ AI Recruitment Screening Process Completed Successfully!")

if __name__ == "__main__":
    main()
