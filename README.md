# 📘 **ATS Resume Expert** 
**1. Introduction**

The ATS Resume Expert is an AI-powered web application designed to evaluate resumes using the Google Gemini 2.5 Flash Vision Model.
Users can upload their resume in PDF format and provide a job description, and the system analyzes:
- Resume strengths and weaknesses
- Missing skills
- ATS keyword match percentage
- Overall job-fit evaluation
- This tool helps candidates improve their resumes and increases their chances of passing ATS screening systems used in modern recruitment.

**2. Objective**

**The main objectives of this project are:**
- To analyze resume content using a vision-based LLM
- To compare resume skills with job description requirements
- To generate an ATS percentage match score
- To identify missing keywords or gaps
- To assist job seekers in optimizing their resumes

**3. Technologies Used**
| Component              | Technology                       |
| ---------------------- | -------------------------------- |
| Framework              | Streamlit                        |
| Language               | Python                           |
| AI Model               | Google Gemini 2.5 Flash (Vision) |
| Image/PDF Processing   | pdf2image, PIL                   |
| Environment Management | python-dotenv                    |
| Deployment Ready       | Streamlit Cloud / Render         |


**4. System Architecture**
1. Upload Resume (PDF)
2. Convert PDF → Image (using pdf2image)
3. Convert image → Base64
4. Gemini Vision Model analyzes the first page
5. System Prompt + Job Description → AI processing

**Outputs:**
   - Resume analysis report
   - ATS percentage match
   - Missing keywords
   - Strengths & weaknesses

**5. Features**
**✔ Resume Analysis**

The model gives a detailed evaluation, including:
- Alignment with the job role
- Strong areas
- Weak areas
- Skill coverage

**✔ ATS Percentage Match**

- Outputs a numerical match score based on:
- Skill keywords
- Job description alignment
- Role relevance

**✔ Keyword Gap Analysis**

Lists keywords missing from the resume that recruiters expect.

**✔ PDF → Image Processing**

Uses pdf2image to convert the resume page into an AI-readable format.

**✔ Easy-to-use Web Interface**

**Streamlit UI enables:**
- Resume upload
- Job description input

**6. Prompt Design**

Two carefully designed prompts ensure accurate results:

**A. Analysis Prompt**

Used for candidate evaluation:

Profile alignment

Strengths & weaknesses

Missing skills

**B. ATS Matching Prompt**

Used to compute:

Percentage match

Missing keywords

Final suggestions

This structured prompting ensures the model outputs relevant and consistent results.

**7. Processing Workflow**

User uploads resume (PDF)

PDF converted → image → Base64 encoded

Input prompt + job description fed into Gemini Vision

AI analyzes resume content

Output displayed in Streamlit UI

**8. Results**

The system returns:

**Sample Output**
ATS Match: 78%
Missing Keywords: Python, Power BI, Agile
Strengths: Clear work history, relevant projects
Weaknesses: Missing certifications, no metrics in achievements
Final Recommendation: Add technical keywords and quantify results.


**The output is:**

Clear

Professional

Recruiter-style evaluation

**9. Limitations**

Only analyzes the first page of the PDF

Not a replacement for human HR screening

Can only evaluate visible text (no deep parsing)

**10. Future Improvements
**
Multi-page PDF parsing

Resume rewriting suggestions

JSON-structured output

Downloadable ATS report as PDF

Integration with job portals

Support for multiple resumes comparison

**11. Conclusion**

The ATS Resume Expert demonstrates an effective use of AI vision models to automate resume evaluation.
It improves the job preparation process by offering:

Skill gap insights

ATS readiness scores

Structured professional analysis

This tool can be scaled for:

Job portals

Recruitment agencies

Career coaching platforms

Resume-building applications
