from crewai import Agent
import configs as config
import tools.web_scrapping as web_scrapping

class AllAgents():
	
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key
    def Agent1(self):
        return Agent(
            role='Node js Engineer',
            goal=("""Develop a scalable and efficient backend system using Node.js."""),
            backstory=("""a software engineer with experience in building web applications using Node.js. have worked on various projects that required me to design and implement backend systems using Node.js. familiar with the best practices and tools for developing Node.js applications and have a strong understanding of server-side programming."""),
            tools=[],
            verbose=True,

            llm = config.llmLlaMa5,
            
        )
    def Coder(self):
        return Agent(
            role='Node js developper',
            goal=("""Develop a scalable and efficient backend system using Node.js and java script"""),
            backstory=("""a software engineer with experience in building web applications using Node.js and javascript. have worked on various projects that required me to design and implement backend systems using Node.js. familiar with the best practices and tools for developing Node.js applications and have a strong understanding of server-side programming."""),
            tools=[],
            allow_delegation=True,
            verbose=True,
            llm = config.llmLlaMa5,
            max_iter=10,
            memory=True,
            
        )
    
############################################
    def ProjectManagerAgent(self):
        return Agent(
            role='Node.js Project Manager',
            goal='Oversee and coordinate the creation of the Node.js project structure using only windows cmd',
            backstory="""An experienced technical project manager with expertise in Node.js architecture. 
            Skilled in establishing project structures and ensuring best practices are followed.""",
            tools=[],
            allow_delegation=True,
            verbose=True,
            llm = config.llmLlaMa0,
                        memory=True,

        )
    def CoreDeveloperAgent(self):
        return Agent(
            role='Core Node.js Developer',
            goal='Implement core server functionality and main application logic using only windows cmd',
            backstory="""A senior Node.js developer specialized in server-side architecture 
            and core application setup. Expert in Express.js and Node.js best practices.""",
            tools=[ ],
            allow_delegation=True,
            verbose=True,
            llm = config.llmLlaMa2,
                        memory=True,

        )

    def APIDevAgent(self):
        return Agent(
            role='API Developer',
            goal='Create and implement API routes and controllers using only windows cmd ',
            backstory="""An API specialist with deep knowledge of RESTful principles 
            and Node.js routing. Experienced in creating clean and efficient API endpoints.""",
            tools=[ ],
            allow_delegation=True,
            verbose=True,
            llm = config.llmLlaMa1,
                        memory=True,

        )

    def TestingAgent(self):
        return Agent(
            role='Testing Specialist',
            goal='Implement comprehensive test suites for the Node.js application using only windows cmd',
            backstory="""A QA engineer specialized in Node.js testing. Expert in unit, 
            integration, and end-to-end testing methodologies.""",
            tools=[ ],
            allow_delegation=True,
            verbose=True,
            llm = config.llmLlaMa4,
                        memory=True,

        )

    def ConfigurationAgent(self):
        return Agent(
            role='Configuration Specialist',
            goal='Set up project configuration and environment settings using only windows cmd',
            backstory="""A DevOps engineer specialized in Node.js application configuration 
            and environment setup. Expert in managing different deployment environments.""",
            tools=[ ],
            allow_delegation=True,
            verbose=True,
            llm = config.llmLlaMa5,
                        memory=True,

        )