"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["Welcome to Binary Smith! How can we help you today?"]
  },
  {
    "role": "model",
    "parts": ["Hello! Thank you for welcoming me to Binary Smith. I'm interested in learning more about your services and how they can benefit my business. Could you provide me with some information on your specialties and the types of projects you typically handle?"]
  },
  {
    "role": "user",
    "parts": ["1. Web App Development\n2. Mobile App Development\n3.Digital Transformation\n4. Technology Consulting\n5. Cloud Services"]
  },
  {
    "role": "model",
    "parts": ["That's a comprehensive range of services! To help me understand how Binary Smith can best assist me, could you elaborate on each of these areas?  For instance, what technologies and frameworks do you use for web and mobile app development? What does digital transformation look like in your approach, and what types of businesses do you typically consult for?"]
  },
  {
    "role": "user",
    "parts": ["1. Technologies we use for Web and Mobile App development are Java, Java EE, Spring Boot, Kotlin, Android and GCP.\n2. Our digital transformation services will help you leverage new technologies to modernize your applications. Whether it’s migrating legacy infrastructure, integrating a new platform, or reimagining your customer experience with AI, we’ll optimize your tech stack and get you to market faster.\n3. Businesses we consult for are like SMEs, Banking, Insurance, eCommerce and Automobile etc."]
  },
  {
    "role": "model",
    "parts": ["Thank you for the detailed explanation. It seems like Binary Smith has a strong focus on Java-based technologies and cloud solutions, which aligns well with my current needs. I'm particularly interested in your digital transformation and cloud services. \n\nCould you share some examples of successful digital transformation projects you've undertaken? Additionally, what cloud platforms do you specialize in, and how do you approach cloud migration for existing applications?"]
  },
  {
    "role": "user",
    "parts": ["We delivered various digital transformation projects like IoT, analytics, productivity applications etc..\nWe are well-versed in AWS, GCP, Microsoft Azure and few other Cloud services.\nRegarding our cloud migration approach, we migrate individual services to Cloud. For example, Databases, deployments etc. We also specialised in transforming a Monolithic Applications into Microservices based architectures."]
  },
  {
    "role": "model",
    "parts": ["Your experience with IoT, analytics, and productivity applications is impressive, and your expertise in major cloud platforms like AWS, GCP, and Azure is reassuring. I'm particularly intrigued by your approach to cloud migration, especially the focus on microservices architecture.\n\nI'd like to discuss a potential project involving migrating our existing monolithic application to a cloud-based microservices architecture. Could you provide more information on your process for such a migration, including the tools and technologies you utilize, and the typical timeline for a project of this nature?"]
  },
  {
    "role": "user",
    "parts": ["We use Spring Boot, AWS Lambda, Micronaut etc for Microservices development, Apache Kafka or AWS SQS for Messaging and Asynchronous communication between the Microservices, GKE or AWS EKS for Container Orchestration and few other technologies.\n\nFor more details, visit binarysmith.co.za or Contact us at sound4peace@gmail.com"]
  },
  {
    "role": "model",
    "parts": ["Thank you for outlining the technologies you use for microservices development and cloud migration. Your expertise in Spring Boot, AWS Lambda, and container orchestration tools like GKE and AWS EKS is exactly what I'm looking for.\n\nI'll definitely visit binarysmith.co.za for further information and reach out to the provided email address to discuss our project in more detail.\n\nI appreciate your time and comprehensive responses. I'm confident that Binary Smith has the expertise and experience to help us successfully modernize our application and leverage the benefits of the cloud."]
  },
  {
    "role": "user",
    "parts": ["Thank you. Looking forward for your email."]
  },
  {
    "role": "model",
    "parts": ["You're most welcome! I'll be in touch soon. Have a great day."]
  },
])

convo.send_message("YOUR_USER_INPUT")
print(convo.last.text)